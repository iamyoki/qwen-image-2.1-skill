# Qwen-Image-2.1 Prompter Skill

[English](README.md) | [简体中文](README_zh.md)

[![Skills.sh Compatible](https://img.shields.io/badge/skills.sh-compatible-blue.svg)](https://skills.sh)
[![Model](https://img.shields.io/badge/Target_Model-Qwen--Image--2.1-orange.svg)](https://qwen.ai/blog?id=qwen-image-2.1)
[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](LICENSE)

An agentic skill that rewrites, optimizes, and structures image generation and editing prompts specifically tailored for Alibaba's **Qwen-Image-2.1** diffusion model.

Built strictly upon Alibaba's official prompt rewriting system specifications:
- **Text-to-Image (T2I)**: [system_prompt_t2i.txt](https://github.com/QwenLM/Qwen-Image-2.1/blob/main/prompt_rewrite/prompts/system_prompt_t2i.txt)
- **Image Editing (Edit)**: [system_prompt_edit.txt](https://github.com/QwenLM/Qwen-Image-2.1/blob/main/prompt_rewrite/prompts/system_prompt_edit.txt)
- **Technical Blog**: [Qwen-Image-2.1 Announcement](https://qwen.ai/blog?id=qwen-image-2.1)

---

## ⚡ Quick Install

### Method 1: Ask Your AI Agent (Recommended / Zero-Setup)

Copy and paste this instruction directly to your AI coding assistant (Claude Code, Cursor, Windsurf, Roo, Trae, etc.):

```text
Please install the Qwen-Image-2.1 prompter skill from https://github.com/iamyoki/qwen-image-2.1-skill or by running `npx skills add iamyoki/qwen-image-2.1-skill`.
```

### Method 2: One-Line CLI (via skills.sh)

```bash
npx skills add iamyoki/qwen-image-2.1-skill
```

<details>
<summary><b>Method 3: Manual Installation & All Supported Agents</b></summary>

Alternatively, copy or symlink the `skills/qwen-image-2-1-prompter` directory into your agent's skill directory:

| Agent / IDE / Tool | Target Skill Path |
|---|---|
| **Claude Code** | `.claude/skills/qwen-image-2-1-prompter` or `~/.claude/skills/` |
| **Cursor** | `.cursor/skills/qwen-image-2-1-prompter` or `.agents/skills/` |
| **Windsurf** | `.windsurf/skills/qwen-image-2-1-prompter` or `.agents/skills/` |
| **Roo Code / Cline** | `.roo/skills/qwen-image-2-1-prompter` or `.cline/skills/` |
| **Trae / Copilot Workspace** | `.trae/skills/qwen-image-2-1-prompter` or `.agents/skills/` |
| **OpenDevin / Devin / Codex** | `.agents/skills/qwen-image-2-1-prompter` |
| **Antigravity / Gemini CLI** | `.agents/skills/qwen-image-2-1-prompter` |
| **Any Agent with skills.sh standard** | Compatible with all autonomous agents supporting standard Markdown skills |

</details>

---

## 🌟 Key Capabilities

1. **Official 8-Step T2I Rewriting**:
   - Turns terse user requests into a single, cohesive, ~400–500-word English descriptive paragraph.
   - Strictly enforces observer perspective, 8–14 border-reaching spatial positional phrases, dedicated lighting sentences, and precise aspect ratios (`wh_ratio`).
   - Rejects empty quality buzzwords (no "8K", "masterpiece").

2. **Attribute Disentanglement for Image Editing**:
   - High-strength edit execution with zero attribute leakage on untouched content.
   - Dual language protocol: Decision (A) for descriptive prose (Chinese/English) and Decision (B) for literal text rendered in images.
   - Multi-image condition tagging (`<image1>`, `<image2>`, ...) and automatic canvas resolution tracking (`ratio_follow` vs `wh_ratio`).
   - Specialized rules for outpainting, panoramas, and three-view grid generation.

3. **Dual-Track Multi-Modal Adaptation**:
   - Inspects input images directly in Vision-enabled Agent environments (Claude Code, GPT-4o, Gemini).
   - Gracefully infers visual attributes when running in text-only terminal environments.

4. **Adaptive Output Presentation**:
   - **Default Mode**: Provides decision breakdowns + copy-ready WebUI Prompt + official single-line JSON payload + tweak suggestions.
   - **API / Pipeline Mode**: Outputs pure single-line JSON upon request for ComfyUI and programmatic pipelines.

---

## 📂 Repository Structure

```text
qwen-image-2.1-skill/
├── LICENSE                                # Apache License 2.0
├── CONTEXT.md                             # Domain modeling glossary & language protocol
├── README.md                              # Main documentation (English)
├── README_zh.md                           # Chinese documentation (简体中文)
├── docs/
│   └── adr/                               # Architecture Decision Records
└── skills/
    └── qwen-image-2-1-prompter/
        ├── SKILL.md                       # Core entry point & intent router
        ├── references/
        │   ├── t2i_rules.md               # Official 8-step T2I rewriting specification
        │   ├── edit_rules.md              # Official Edit & multi-image specification
        │   └── cheat_sheet.md             # Vocabulary lookup (styles, materials, ratios)
        └── scripts/
            └── validate_prompt.py         # Offline prompt & JSON schema validator
```

---

## 🚀 Usage Examples

### 1. Text-to-Image (T2I)
**User Input**:
> "帮我用千问画一张暴雨夜赛博朋克街头的小吃摊，要有浓厚的烟火气和霓虹倒影，电影质感。"

**Agent Output (Default Mode)**:
- **优化解析**：选定 `16:9` 宽银幕电影画幅，将小吃摊作为主体置于右侧下三分之一，左侧展开雨夜霓虹纵深街道。
- **WebUI 提示词**：生成约 450 词的高精度英文客观观察段落，明确描述雨水反光、摊位蒸汽、食材质感、暖光灯泡与远处青紫冷色霓虹的冷暖交织。
- **API JSON**：输出 `{"rewritten_prompt": "...", "wh_ratio": "16:9"}`。

### 2. Multi-Image Editing (Compositing)
**User Input**:
> "把 <image2> 中的古代汉服换到 <image1> 中的人物身上，背景和脸不要动。"

**Agent Output**:
- **优化解析**：设定 `<image1>` 为 Canvas，锁定人物面部、发型特征与背景环境，将 `<image2>` 汉服的布料质感与刺绣纹样无缝迁移。
- **API JSON**:
  ```json
  {
    "rewritten_prompt": "将<image2>中的传统青色刺绣交领汉服替换到<image1>中人物身上，保持<image1>人物的面部五官、发型、姿态表情以及原图背景完全一致，汉服的面料光泽自然贴合<image1>的环境光照。",
    "wh_ratio": "",
    "ratio_follow": "<image1>"
  }
  ```

---

## 🧪 Testing & Validation

Run the bundled test suite to verify prompt compliance with Qwen 2.1 schema requirements:

```bash
python skills/qwen-image-2-1-prompter/scripts/validate_prompt.py --test
```

Validate any custom JSON output file or string:

```bash
python skills/qwen-image-2-1-prompter/scripts/validate_prompt.py "{\"rewritten_prompt\": \"...\", \"wh_ratio\": \"16:9\"}"
```

---

## 📄 License

This project is licensed under the Apache License 2.0.
Official prompt rules copyright Alibaba Qwen Team.
