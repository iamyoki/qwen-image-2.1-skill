# 0003. Skill Directory and Name Alignment

We decided to place the skill in `skills/qwen-image-2-1-prompter/` with the exact matching frontmatter `name: qwen-image-2-1-prompter`, versioned explicitly for Qwen-Image-2.1.

## Context
When distributing skills via `skills.sh`, naming collisions and discovery ambiguity can occur if generic names like `image-prompter` are used. Furthermore, having the package folder name match the YAML `name` identifier ensures deterministic packaging, installation path discovery, and symlinking across Claude Code, Cursor, Windsurf, Roo Code, and Antigravity.

## Consequences
- Clean directory hierarchy supporting future skills under `skills/` in the same repo if desired.
- Zero mismatch between skill name and directory path during `npx skills add` installations.
