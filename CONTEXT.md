# Qwen Image 2.1 Prompt Engineering Context

The domain of structuring, optimizing, and evaluating generation and editing directives for Alibaba's Qwen-Image-2.1 diffusion model across autonomous coding agents.

## Language

### Core Prompt Concepts

**Observer Perspective**:
A descriptive prose mode where the prompt reports only what is visibly present in the frame as an impartial witness, rather than instructing a renderer or talking to a user.
_Avoid_: Imperative instructions to AI, quality buzzwords, conversational remarks

**Attribute Disentanglement**:
An image editing principle where only explicitly targeted attributes are altered at maximum intensity while all untargeted visual features are preserved at original input fidelity.
_Avoid_: Leakage, under-editing, style drift, unintended re-rendering

**Language Dual-Track (Decision A & B)**:
The protocol separating the descriptive prose language (Decision A: Chinese or English) from the language of text physically rendered inside the image (Decision B: exact target script, strictly monolingual).
_Avoid_: Mixed-language rendered text, arbitrary translation of image text

**Blanket Preservation**:
A high-level declaration naming untargeted content by role and position to keep it fixed, without describing its detailed visual appearance.
_Avoid_: Detailed repainting, walking untargeted regions

### Artifacts & Structure

**Prompt Skill**:
A portable agent instruction bundle conforming to the `skills.sh` standard containing a `SKILL.md` manifest, reference rules, and auxiliary scripts.
_Avoid_: Agent plugin, system prompt snippet, workflow script

**Canvas Image**:
In multi-image editing, the primary input image whose composition, framing, and untargeted content form the foundation of the output.
_Avoid_: Base image, reference image, background photo

**wh_ratio vs ratio_follow**:
The mutually exclusive aspect ratio specification fields in Qwen 2.1, where `wh_ratio` defines a geometric ratio and `ratio_follow` binds to a specific input image tag.
_Avoid_: Pixel dimensions in prompt text, combined ratio tags

**Adaptive Output Modes (Default vs API)**:
The presentation protocol separating human-centric interactive dialogue (Optimization Breakdown with aspect ratio + clean copy-pasteable Prompt + Tweak Suggestions, omitting redundant JSON payloads) from machine-centric automated execution (strict single-line JSON only).
_Avoid_: Duplicating 500-word JSON payloads in interactive chat, markdown wrappers in API responses

