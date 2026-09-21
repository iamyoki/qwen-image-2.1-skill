# 0002. Adaptive Output Formatting

We decided to support an adaptive output presentation: by default, providing an optimization breakdown, a clean copy-pasteable prompt block for WebUI users, an official API JSON block, and tweak suggestions; while providing strict single-line JSON only when the user explicitly requests an API or automated pipeline response.

## Context
Alibaba's official prompt rewrite specification expects strict single-line JSON payloads (`{"rewritten_prompt": "...", "wh_ratio": "..."}`). However, interactive users chatting with an AI agent benefit greatly from understanding the camera/lighting/layout choices made, and WebUI users need raw unquoted text strings to paste into generation forms.

## Consequences
- Interactive users get full transparency, easy copy-pasting, and actionable tweak suggestions.
- Automated API and ComfyUI pipeline users can request pure JSON without having to strip markdown fences or explanations.
