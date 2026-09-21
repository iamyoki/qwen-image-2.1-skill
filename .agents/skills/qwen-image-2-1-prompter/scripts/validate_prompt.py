#!/usr/bin/env python3
"""
Prompt validator for Qwen-Image-2.1 prompt rewriting specifications.
Verifies JSON structure, aspect ratio formatting, mutual exclusivity,
single-paragraph continuity, and quote balance.
"""

import sys
import json
import re
from typing import Dict, Any, List, Tuple

# Ensure stdout uses utf-8 on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

RATIO_REGEX = re.compile(r"^\d+:\d+$")
IMAGE_TAG_REGEX = re.compile(r"^<image\d+>$")
FORBIDDEN_BOOSTERS = ["8k", "4k", "masterpiece", "award-winning", "photorealistic masterpiece"]

def validate_qwen_prompt(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
    errors = []
    
    # 1. Check required fields
    if "rewritten_prompt" not in payload:
        errors.append("Missing required field 'rewritten_prompt'.")
    
    prompt = payload.get("rewritten_prompt", "")
    if not isinstance(prompt, str):
        errors.append("'rewritten_prompt' must be a string.")
    else:
        # 2. Check no newlines in rewritten_prompt
        if "\n" in prompt or "\r" in prompt:
            errors.append("'rewritten_prompt' must be a single continuous paragraph without newline characters.")
        
        # 3. Check for empty string
        if not prompt.strip():
            errors.append("'rewritten_prompt' is empty.")
            
        # 4. Check straight double quotes balance
        quote_count = prompt.count('"')
        if quote_count % 2 != 0:
            errors.append(f"Unbalanced double quotes detected in 'rewritten_prompt' (found {quote_count} double quotes).")
            
        # 5. Check for forbidden quality booster words
        lower_prompt = prompt.lower()
        for booster in FORBIDDEN_BOOSTERS:
            if re.search(r'\b' + re.escape(booster) + r'\b', lower_prompt):
                errors.append(f"Forbidden quality booster '{booster}' detected in prompt. Describe observable visual elements instead.")

    # 6. Check size fields: wh_ratio and ratio_follow
    has_wh_ratio = "wh_ratio" in payload
    has_ratio_follow = "ratio_follow" in payload

    if not has_wh_ratio and not has_ratio_follow:
        errors.append("Payload must contain 'wh_ratio' (for T2I) or both 'wh_ratio' and 'ratio_follow' (for Edit).")

    wh_ratio = payload.get("wh_ratio", "")
    ratio_follow = payload.get("ratio_follow", "")

    # Mutual exclusivity check if ratio_follow is present (Edit mode)
    if has_ratio_follow:
        if wh_ratio and ratio_follow:
            errors.append(f"Mutual exclusivity violation: 'wh_ratio' ('{wh_ratio}') and 'ratio_follow' ('{ratio_follow}') cannot both be non-empty.")
        if not wh_ratio and not ratio_follow:
            errors.append("At least one of 'wh_ratio' or 'ratio_follow' must be specified.")
            
        if ratio_follow and not IMAGE_TAG_REGEX.match(ratio_follow):
            errors.append(f"Invalid 'ratio_follow' format '{ratio_follow}'. Must match '<imageX>' (e.g., '<image1>').")

    if wh_ratio:
        if not RATIO_REGEX.match(wh_ratio):
            errors.append(f"Invalid 'wh_ratio' format '{wh_ratio}'. Must match 'W:H' (e.g. '16:9', '3:2').")

    return len(errors) == 0, errors

def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_prompt.py <json_string_or_filepath> [--test]")
        print("Running internal self-tests...")
        run_self_tests()
        sys.exit(0)

    arg = sys.argv[1]
    if arg == "--test":
        run_self_tests()
        sys.exit(0)

    try:
        if arg.startswith("{"):
            data = json.loads(arg)
        else:
            with open(arg, "r", encoding="utf-8") as f:
                data = json.load(f)
    except Exception as e:
        print(f"❌ Failed to parse JSON: {e}")
        sys.exit(1)

    passed, errors = validate_qwen_prompt(data)
    if passed:
        print("✅ Validation successful: prompt complies with Qwen-Image-2.1 specifications.")
        sys.exit(0)
    else:
        print("❌ Validation failed:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)

def run_self_tests():
    test_cases = [
        (
            "T2I valid case",
            {"rewritten_prompt": 'The image is a wide cinematic photograph of a cat sitting on a windowsill. Outside, gentle rain falls across the glass. The lighting is soft ambient daylight. The overall composition feels tranquil and balanced.', "wh_ratio": "16:9"},
            True
        ),
        (
            "Edit valid single-image follow",
            {"rewritten_prompt": '把图片中人物的黑色外套替换为深红色羊毛西装外套，保持人物的面部五官、发型、姿态以及室内背景与原图完全一致。', "wh_ratio": "", "ratio_follow": "<image1>"},
            True
        ),
        (
            "Edit valid multi-image compositing",
            {"rewritten_prompt": '将<image2>中的经典复古手表佩戴在<image1>中男士的左手手腕上，保持<image1>的人物形态、光影与背景完全不变。', "wh_ratio": "", "ratio_follow": "<image1>"},
            True
        ),
        (
            "Invalid mutual exclusivity",
            {"rewritten_prompt": '把背景换成雪山。', "wh_ratio": "16:9", "ratio_follow": "<image1>"},
            False
        ),
        (
            "Invalid newline in prompt",
            {"rewritten_prompt": "First line.\nSecond line.", "wh_ratio": "3:2"},
            False
        ),
        (
            "Invalid forbidden booster",
            {"rewritten_prompt": "A 8K masterpiece portrait of an owl.", "wh_ratio": "1:1"},
            False
        )
    ]

    all_ok = True
    for name, payload, expected in test_cases:
        passed, errors = validate_qwen_prompt(payload)
        status = (passed == expected)
        symbol = "✅" if status else "❌"
        print(f"{symbol} Test: {name}")
        if not status:
            all_ok = False
            print(f"   Expected passed={expected}, got {passed}. Errors: {errors}")

    if all_ok:
        print("\nAll self-tests passed successfully!")
    else:
        print("\nSome self-tests failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
