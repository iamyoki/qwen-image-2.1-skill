# 0001. Unified Skill with Progressive Disclosure

We decided to implement Qwen-Image-2.1 prompt optimization as a single unified skill (`qwen-image-2-1-prompter`) rather than two disconnected skills for Text-to-Image (T2I) and Image Editing. The core `SKILL.md` serves as a lightweight intent router, loading detailed specifications from `references/t2i_rules.md` and `references/edit_rules.md` as needed.

## Context
Qwen-Image-2.1 has distinct official prompt specifications for text-to-image generation (8-step observer prose, English descriptions) and image editing (attribute disentanglement, dual-track language, multi-image `<imageN>` tagging). Splitting them into two separate skills would force users to know upfront which skill to trigger and increases cognitive load and triggering ambiguity for AI agents.

## Consequences
- End users can make natural requests ("用千问画图" or "帮我把图里的衣服换了") under a single unified skill invocation.
- Keeps `SKILL.md` under 200 lines, conforming to the progressive disclosure pattern recommended for `skills.sh`.
