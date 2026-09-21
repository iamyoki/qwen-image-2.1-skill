# 0002. Adaptive Output Formatting

We decided to support an adaptive output presentation: by default, providing an optimization breakdown, a clean copy-pasteable prompt block with inline aspect ratio guidance, and tweak suggestions—completely omitting duplicate JSON payloads; while providing strict single-line JSON only when the user explicitly requests an API, JSON, or automated pipeline response.

## Context
Alibaba's official prompt rewrite specification expects strict single-line JSON payloads (`{"rewritten_prompt": "...", "wh_ratio": "..."}`). In an earlier design, both raw text and the full JSON payload were output in interactive chat sessions. However, user feedback revealed that duplicating the ~500-word English prompt inside a JSON string roughly doubled generation time, wasted token budget, and cluttered chat responses. Furthermore, labeling prompt headers with client-specific terms like "Qwen WebUI" was overly restrictive for users pasting into DashScope, ComfyUI, or other interfaces.

## Decision & Amendments
- **Default Mode (Interactive)**: Output strictly three sections: `💡 提示词优化解析` (which explicitly specifies the aspect ratio), `📋 提示词（可直接复制）` (clean code block only, without duplicate aspect ratio subtitles), and `🎨 进阶微调建议`. The JSON payload is completely removed from default responses.
- **API / Pipeline Mode (Strict JSON Only)**: When users explicitly ask for JSON, API, or automated pipelines, return ONLY the raw single-line JSON string without markdown wrappers.
- **Skill Manifest Cleanliness**: Removed long few-shot example blocks from `SKILL.md` to prevent token bloat and avoid biasing models toward emitting redundant JSON structures.

## Consequences
- Interactive users receive responses faster with zero duplicate text and clean one-click copy blocks.
- The aspect ratio is clearly stated once in the breakdown, keeping the prompt section completely distraction-free.
- System token consumption when activating `qwen-image-2-1-prompter` is reduced by ~35%.

