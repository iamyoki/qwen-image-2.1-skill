# Qwen-Image-2.1 Vocabulary & Parameter Cheat Sheet

This cheat sheet provides quick vocabulary lookups for composing precise prompts matching Qwen-Image-2.1's semantic latent space.

---

## 1. Medium & Style Vocabulary

Used primarily in **Step 3 (Opening Sentence)** for T2I:

| Category | Recommended Terms | Notes |
|---|---|---|
| **Mediums** | photograph, poster, illustration, scene, portrait, infographic, close-up, graphic, page, card, sheet, logo, editorial | Medium is NEVER omitted. |
| **Photographic Styles** | photorealistic, editorial fashion, cinematic, documentary, macro close-up, tilt-shift, vintage film (Kodak Portra, Fujifilm) | Avoid empty boosters ("8K", "masterpiece"). Describe optical traits instead. |
| **Illustration & Art** | flat-vector, watercolour, hand-drawn sketch, ink wash, woodcut, ukiyo-e, gouache, retro comic, storybook | Pair with paper/stroke texture. |
| **Digital & 3D** | isometric 3D render, claymation, octane render, low-poly, cyberpunk neon, stylized character model | Specify shader/material qualities. |

---

## 2. Materials & Physical Textures

Always give the material/texture, not just the bare noun:

- **Metals**: brushed stainless steel, anodized aluminum, tarnished brass, polished copper, cast iron, matte chrome.
- **Glass & Liquids**: frosted glass, fluted glass, leaded crystal, condensation droplets, murky puddle, glossy glaze.
- **Fabrics & Wearables**: coarse linen, ribbed cotton knit, distressed denim, supple lambskin leather, sheer silk chiffon, houndstooth wool.
- **Surfaces & Architecture**: weathered teak wood, exposed aggregate concrete, polished travertine marble, cracked asphalt, terracotta tiles.
- **Paper & Graphics**: matte recycled paper fibre, high-gloss coated cardstock, embossed vellum, aged parchment with deckled edges.

---

## 3. Spatial & Positional Phrases

Used in **Step 4 & 5 (Spatial Inventory & Walking the Frame)**. Aim for 8–14 positional anchors covering edges, corners, and centre:

```
[upper-left corner]      [across the top band]       [upper-right corner]
[along the left edge]    [in the absolute centre]    [along the right edge]
[lower-left corner]      [across the lower third]    [lower-right corner]
```

- **Relative positioning**: `directly in front of`, `tucked behind`, `nestled between`, `receding into the background`, `angled slightly toward the camera`, `jutting outward from the bottom edge`.
- **Compositional distribution**: Ensure positional phrases do not cluster solely in the center; anchor objects in the four quadrants and borders.

---

## 4. Lighting Descriptors

Used in **Step 7 (Lighting Sentence)**:

- **Natural Light**: soft diffused daylight filtering through an overcast sky, harsh midday summer sunlight casting sharp short shadows, warm golden-hour glow coming low from the left, cool blue twilight ambient light.
- **Interior & Studio**: three-point studio lighting with a large softbox, directional rim lighting accentuating edges, warm overhead incandescent pendant lamp, single dramatic spotlight cutting through darkness.
- **Atmospheric**: volumetric light rays (god rays) streaming through misty air, neon ambient spill from adjacent street signage, flickering firelight illuminating one side of the subject.

---

## 5. Aspect Ratio (`wh_ratio`) Quick Matrix

| Target Use Case | wh_ratio | Typical Resolution Range |
|---|---|---|
| Default Landscape | `3:2` | 1536×1024 / 2048×1365 |
| Default Portrait | `2:3` | 1024×1536 / 1365×2048 |
| Square (Badge, Icon, Avatar) | `1:1` | 1024×1024 / 2048×2048 |
| Presentation / Desktop / Cinematic | `16:9` | 1920×1080 / 2560×1440 |
| Mobile Screen / Story / Reel | `9:16` | 1080×1920 / 1440×2560 |
| Panoramic Landscape | `2:1` or `3:1` | 2048×1024 / 3072×1024 |
| Ultra-wide / Widescreen Film | `21:9` | 2560×1080 |
| Xiaohongshu / Standard ID Photo | `3:4` | 1080×1440 |
| A4 Paper Equivalent | `5:7` (vertical) / `7:5` (horizontal) | 1080×1512 / 1512×1080 |
