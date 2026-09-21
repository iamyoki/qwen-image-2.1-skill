# qwen-image-2.1-skill

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
   - **Default Interactive Mode**: Provides Optimization Breakdown (with aspect ratio) + clean copy-ready Prompt block (`#### 📋 提示词（可直接复制）`) + Tweak Suggestions. Omit duplicate JSON to prevent token bloat and reduce generation latency.
   - **API / Pipeline Mode**: Outputs pure single-line JSON (`{"rewritten_prompt": "...", "wh_ratio": "..."}`) only upon explicit user request for programmatic and ComfyUI pipelines.

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
            └── validate_prompt.py         # Offline developer & CI prompt validator
```

---

## 🚀 Usage Examples

### 1. Text-to-Image (T2I)
**User Input**:
> "帮我用千问画一张暴雨夜赛博朋克街头的小吃摊，要有浓厚的烟火气和霓虹倒影，电影质感。"

**Agent Output (Default Interactive Mode)**:

#### 💡 提示词优化解析
- **主体概念**：暴雨夜赛博朋克街头小吃摊，浓郁烟火气与霓虹电影质感。
- **画幅比例**：`16:9`（宽银幕电影构图）。
- **构图与光影**：小吃摊置于右侧前景，左侧纵深延伸雨夜湿滑街道；暖黄白炽灯与背景青蓝、紫红色霓虹灯形成冷暖侧逆光交织。

#### 📋 提示词（可直接复制）
```text
The image is a wide cinematic photograph of a vibrant food stall nestled into a rain-drenched cyberpunk alleyway at night. In the right foreground, an open-front wooden and stainless steel food cart emits billowing plumes of translucent white steam that catch the glow of suspended warm incandescent bulbs. The middle-aged vendor, wearing a grease-stained dark apron, tends sizzling metal pans loaded with skewers. Across the wet asphalt ground plane in the lower third, puddles reflect distorted vertical stripes of electric cyan, magenta, and amber neon signage. To the left, the narrow alley recedes into the distance under tangled overhead cables and layered vertical holographic advertisements in English and Japanese. Along the upper edge, towering utilitarian concrete facades rise into an inky rain-streaked night sky. The lighting is dominated by high-contrast directional rim lights from ambient neon signs balanced against the warm incandescent glow radiating from the stall. The overall composition is atmospheric and layered, balancing human warmth against cold industrial grit with rich tonal contrast.
```

#### 🎨 进阶微调建议
1. **画幅切换**：若作为移动端壁纸，可调整为 `9:16` 竖屏构图。
2. **文字招牌**：若需在摊位上方加入特定发光招牌，可指定如 `"CYBER NOODLES"` 字样。

*(Note: If the user explicitly asks for "API format" or "JSON", the agent outputs strictly: `{"rewritten_prompt": "...", "wh_ratio": "16:9"}`)*

### 2. Multi-Image Editing (Compositing)
**User Input**:
> "把 <image2> 中的古代汉服换到 <image1> 中的人物身上，背景和脸不要动。"

**Agent Output**:

#### 💡 提示词优化解析
- **编辑目标**：主体汉服替换，精准属性解耦。
- **Canvas 画布**：`<image1>`（锁定人物五官面部特征与背景环境）。
- **画幅比例**：继承 `<image1>`（`ratio_follow: <image1>`）。

#### 📋 提示词（可直接复制）
```text
将<image2>中的传统青色刺绣交领汉服替换到<image1>中人物身上，保持<image1>人物的面部五官、发型、姿态表情以及原图背景完全一致，汉服的面料光泽自然贴合<image1>的环境光照。
```

#### 🎨 进阶微调建议
1. 可进一步细化汉服在领口与袖口的刺绣金线细节。

---

## 🧪 Developer Testing & Offline Validation

The repository provides an offline schema testing tool for developers and CI pipelines:

> [!NOTE]
> Autonomous agents are configured via `SKILL.md` **never** to execute this script in conversational chat. It is strictly reserved for manual developer testing and CI workflows.

Run the bundled test suite:
```bash
python skills/qwen-image-2-1-prompter/scripts/validate_prompt.py --test
```

Validate a custom JSON payload:
```bash
python skills/qwen-image-2-1-prompter/scripts/validate_prompt.py "{\"rewritten_prompt\": \"...\", \"wh_ratio\": \"16:9\"}"
```

---

## 📄 License

This project is licensed under the Apache License 2.0.
Official prompt rules copyright Alibaba Qwen Team.
