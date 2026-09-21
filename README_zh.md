# qwen-image-2.1-skill

[English](README.md) | [简体中文](README_zh.md)

[![Skills.sh Compatible](https://img.shields.io/badge/skills.sh-compatible-blue.svg)](https://skills.sh)
[![Model](https://img.shields.io/badge/目标模型-Qwen--Image--2.1-orange.svg)](https://qwen.ai/blog?id=qwen-image-2.1)
[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](LICENSE)

一个专为阿里巴巴最新 **Qwen-Image-2.1** 图像生成模型量身定制的 Agent 技能。用于将用户简短、模糊或复杂的想法，重写重构为符合 Qwen 2.1 底层语义与渲染空间的高精度提示词。

严格基于阿里官方提示词重写系统规范实现：
- **文生图规范 (T2I)**：[system_prompt_t2i.txt](https://github.com/QwenLM/Qwen-Image-2.1/blob/main/prompt_rewrite/prompts/system_prompt_t2i.txt)
- **图像编辑与多图规范 (Edit)**：[system_prompt_edit.txt](https://github.com/QwenLM/Qwen-Image-2.1/blob/main/prompt_rewrite/prompts/system_prompt_edit.txt)
- **官方技术博客**：[Qwen-Image-2.1 发布说明](https://qwen.ai/blog?id=qwen-image-2.1)

---

## ⚡ 快速安装

### 方式 1：一键发给你的 AI Agent（推荐 / 小白零配置首选 ⭐）

直接将下方提示词复制发送给你的 AI 编程助手（Claude Code、Cursor、Windsurf、Roo Code、Trae 等）：

```text
请帮我安装 Qwen-Image-2.1 提示词专家技能：从 https://github.com/iamyoki/qwen-image-2.1-skill 安装，或直接在终端运行 `npx skills add iamyoki/qwen-image-2.1-skill`。
```

### 方式 2：终端一行命令（通过 skills.sh）

```bash
npx skills add iamyoki/qwen-image-2.1-skill
```

<details>
<summary><b>方式 3：手动安装与全主流 Agent 路径支持</b></summary>

也可以直接将 `skills/qwen-image-2-1-prompter` 目录复制或软链接到对应 Agent 的技能目录中：

| Agent / IDE / 工具 | 目标技能路径 |
|---|---|
| **Claude Code** | `.claude/skills/qwen-image-2-1-prompter` 或 `~/.claude/skills/` |
| **Cursor** | `.cursor/skills/qwen-image-2-1-prompter` 或 `.agents/skills/` |
| **Windsurf** | `.windsurf/skills/qwen-image-2-1-prompter` 或 `.agents/skills/` |
| **Roo Code / Cline** | `.roo/skills/qwen-image-2-1-prompter` 或 `.cline/skills/` |
| **Trae / Copilot Workspace** | `.trae/skills/qwen-image-2-1-prompter` 或 `.agents/skills/` |
| **OpenDevin / Devin / Codex** | `.agents/skills/qwen-image-2-1-prompter` |
| **Antigravity / Gemini CLI** | `.agents/skills/qwen-image-2-1-prompter` |
| **所有支持 skills.sh 标准的 Agent** | 理论兼容所有支持通用 Markdown 技能规范的智能体环境 |

</details>

---

## 🌟 核心能力

1. **官方 8 步文生图重写分析法 (T2I)**：
   - 将极简输入展开为约 400~500 词、约 20 句的单段高精度英文客观描述。
   - 贯彻客观观察者视角（绝无 "8K", "masterpiece" 等无效修饰空词）。
   - 强制使用 8~14 处触及画面四角与边缘的精确定位词，配备专属光影描述句与精准画幅比例（`wh_ratio`）。

2. **图像编辑“强力属性解耦” (Edit & Multi-Image)**：
   - 满格执行修改指令，对未提及区域实行强力锚定与保留（杜绝属性泄露/偏色/走样）。
   - 严格的双语言决策树：决策 (A) 描述性文字语言（中文/英文分轨），决策 (B) 图片内渲染文字严格保持单语。
   - 多图输入（$N \ge 2$）自动采用 `<image1>`、`<image2>` 显式标签，自动识别 Canvas 画布并执行 `ratio_follow` 与 `wh_ratio` 互斥逻辑。
   - 针对扩图（Outpainting）、全景（Panorama）、三视图与多宫格排版拥有自适应长宽比推演算法。

3. **双模态视觉感知适配 (Dual-Track Vision)**：
   - 在具备 Vision 工具的 Agent（如 Claude Code、GPT-4o、Gemini）中，主动审阅用户提供的参考图，精准抓取原图文字、五官、服饰与环境；
   - 在纯文本终端中自动降级为基于上下文语义的逻辑推导。

4. **自适应输出呈现 (Adaptive Mode)**：
   - **交互模式（默认）**：提供“优化决策解析（含画幅比例） + 复制即用的提示词纯代码块（`#### 📋 提示词（可直接复制）`） + 进阶微调建议”。彻底剔除冗余 JSON 字符串，杜绝长文本重复生成并降低生成延迟。
   - **API / Pipeline 模式**：满足自动化与 ComfyUI 调用需求，仅在用户显式要求时纯净输出单行标准 JSON。

---

## 📂 仓库目录结构

```text
qwen-image-2.1-skill/
├── LICENSE                                # Apache License 2.0
├── CONTEXT.md                             # 领域术语表与规范定义
├── README.md                              # 英文主说明文档
├── README_zh.md                           # 中文说明文档
├── docs/
│   └── adr/                               # 架构决策记录 (ADRs)
└── skills/
    └── qwen-image-2-1-prompter/           # 技能包主目录
        ├── SKILL.md                       # 技能核心入口、意图路由与自适应格式
        ├── references/
        │   ├── t2i_rules.md               # 官方 T2I 8步重写完整规范
        │   ├── edit_rules.md              # 官方 Edit 语言分轨、属性解耦与多图规范
        │   └── cheat_sheet.md             # 材质、镜头、风格、方位词与比例速查表
        └── scripts/
            └── validate_prompt.py         # 开发者离线测试与 CI 验证脚本
```

---

## 🚀 实际使用示例

### 1. 文生图 (T2I)
**用户指令**：
> "帮我用千问画一张暴雨夜赛博朋克街头的小吃摊，要有浓厚的烟火气和霓虹倒影，电影质感。"

**Agent 响应（默认自适应模式）**：

#### 💡 提示词优化解析
- **主体概念**：暴雨夜赛博朋克街头小吃摊，浓郁烟火气与霓虹电影质感。
- **画幅比例**：`16:9`（宽银幕电影构图）。
- **构图与光影**：小吃摊置于右侧前景，左侧展开雨夜湿滑街道与反光沥青；暖黄白炽灯与背景青蓝、紫红霓虹灯形成鲜明冷暖侧逆光。

#### 📋 提示词（可直接复制）
```text
The image is a wide cinematic photograph of a vibrant food stall nestled into a rain-drenched cyberpunk alleyway at night. In the right foreground, an open-front wooden and stainless steel food cart emits billowing plumes of translucent white steam that catch the glow of suspended warm incandescent bulbs. The middle-aged vendor, wearing a grease-stained dark apron, tends sizzling metal pans loaded with skewers. Across the wet asphalt ground plane in the lower third, puddles reflect distorted vertical stripes of electric cyan, magenta, and amber neon signage. To the left, the narrow alley recedes into the distance under tangled overhead cables and layered vertical holographic advertisements in English and Japanese. Along the upper edge, towering utilitarian concrete facades rise into an inky rain-streaked night sky. The lighting is dominated by high-contrast directional rim lights from ambient neon signs balanced against the warm incandescent glow radiating from the stall. The overall composition is atmospheric and layered, balancing human warmth against cold industrial grit with rich tonal contrast.
```

#### 🎨 进阶微调建议
1. **画幅切换**：若作为移动端壁纸，可建议切换为 `9:16` 竖屏构图。
2. **文字招牌**：若需在摊位上方加入特定发光招牌，可指定如 `"CYBER NOODLES"` 字样。

*(注：当且仅当用户明确要求“API 格式”或“JSON”时，Agent 才会纯净输出：`{"rewritten_prompt": "...", "wh_ratio": "16:9"}`)*

### 2. 多图参考与编辑 (Compositing)
**用户指令**：
> "把 <image2> 中的古代汉服换到 <image1> 中的人物身上，背景和脸不要动。"

**Agent 响应**：

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

## 🧪 开发者离线测试与校验

技能包内自带了离线校验脚本，供开发者自测与 GitHub Actions CI 流水线运行：

> [!NOTE]
> 在 `SKILL.md` 中已明文约束，自主 Agent 在日常交互对话中**绝不**调用此脚本，避免无意义的命令行子进程开销与依赖风险。该脚本仅供开发者手动执行或 CI 测试使用。

运行内置测试套件：
```bash
python skills/qwen-image-2-1-prompter/scripts/validate_prompt.py --test
```

校验任意自定义输出 JSON 字符串：
```bash
python skills/qwen-image-2-1-prompter/scripts/validate_prompt.py "{\"rewritten_prompt\": \"...\", \"wh_ratio\": \"16:9\"}"
```

---

## 📄 开源许可证

本项目遵循 Apache License 2.0 开源协议。
官方系统提示词规范版权归阿里巴巴 Qwen 团队所有。
