# 03 — Typography & Rendered Text

Diffusion models perceive text as **pixel-shapes, not language** — hence doubled letters, invented characters, garbled background signage. Two decisions outrank all prompt tricks: **pick a text-capable model**, and **decide whether to let the model render text at all.**

## A. THE RULES
1. **Quote the exact string, always:** `a sign that reads "OPEN"`. Quoted text is treated as a verbatim string, not a concept to interpret. Highest-leverage technique on every model.
2. **Keep it SHORT.** Reliability collapses with length. 1–3 words safe; a short headline workable; full sentences fail. Longer than a headline → plan to composite in post.
3. **Prefer simple casing.** ALL-CAPS short words ('OPEN', 'SALE', 'SHELTER') are most robust — unambiguous glyphs, simpler kerning. Avoid punctuation + mixed case for hard cases; use mixed case only on strong models (GPT-image, Flux, Reve) with short strings.
4. **You cannot request fonts by name.** Describe stylistic properties: `bold sans-serif`, `thin formal script with flourishes`, `retro condensed lettering`, `chrome serif`.
5. **Position text early; simplify the background.** Quoted text near the start; high-contrast simple backgrounds slash spelling/glyph errors. Busy backgrounds steal capacity from letterforms.
6. **Budget ~150 words / one text block per generation.** Multiple independent text zones multiply failure. Render the hero text; add secondary text in post.
7. **Turn off prompt rewriters** ("Magic Prompt" / "enhance") when text accuracy matters — they rewrite your string.

## B. COPY-PASTE PATTERNS
- **Single sign/label (most reliable):** `A [scene]. A [material] sign that reads "OPEN" in bold sans-serif white letters, centered, high contrast, clean kerning.`
- **Multi-line structured:** `...the title "La Pasta" at the top, and "Fresh handmade Italian dishes" below.`
- **Poster/cover:** `A vintage travel poster. Large headline "RIVIERA" in the upper third, retro serif, sun-faded colors, negative space below.`
- **Logo/wordmark:** `A sleek logo with "REVE AI" in glowing neon blue, centered, crisp legible letterforms.`
- **Neon (material language):** `A neon sign reading "DINER" in warm pink glowing tube lettering on brick, reflections on wet pavement.`
- **Surface cues that keep glyphs clean:** `painted in large brush strokes across a mural`, `handwritten white letters on a chalkboard`, `embossed gold foil on a black cover`, `etched into the metal plaque`.
- **Inpaint fix:** mask tightly → `text reading "SALE" in bold sans-serif white letters, sized to fill the sign, matching its color and perspective.`

## C. PER-MODEL TEXT RELIABILITY (2025–2026)
| Model | Strength | Notes |
|---|---|---|
| GPT-image / GPT Image 2 | Highest (~95–100%) | best for logos/signage integration, mixed-case, longer strings |
| Flux 2 / Kontext | Very strong (~88–92%) | best open option; good small-text placement |
| Ideogram 3.0/4.0 | Specialist (~90–95%) | go-to for posters/decorative/multi-line; quote text, simple background |
| Reve 2.0 | Strong; dedicated typography pass | signs/labels/posters clean & legible in correct perspective; weak on complex multi-line/stylized; keep prompts concise |
| Imagen 3/4 | Strong | reliable clean signage |
| Midjourney v7 | Weak (~20–52%) | "shapes that look like letters" — use for art, not text; add text in post |

## D. ARTIFACTS — PREVENT & FIX
- **Doubled/invented letters:** shorten, switch to ALL-CAPS, simplify the word, raise contrast, regenerate (partly stochastic).
- **Background/small signage — leave VAGUE on purpose.** Do NOT specify exact text for distant/tiny signs (guaranteed gibberish). Say `storefront signs`, `neon signs in the background` with no quoted strings — the eye reads "text" without the model committing to broken glyphs. Reserve quoted text for the large hero element only.
- **Negative (where supported):** `warped text, garbled text, extra letters, misspelled text, watermark`. GPT-image/Reve ignore negatives → phrase positively (`clean legible letters, correct spelling`).
- **Mangled small text:** if it must be legible, it must be large in-frame, or composited.

## E. WORKFLOW
1. **Decide up front: model-rendered vs composited.** Pixel-perfect, longer than a headline, brand-exact, precise font → generate the scene **without text** (or placeholder) and set real type in Figma/Photoshop/Canva.
2. If the model renders text and it's ~90% right, **finish it in a design tool** — spelling/spacing/alignment are faster and fully controllable there.
3. **Inpaint only short text (1–3 words):** tight mask, exact quoted string, font style + size relative to surface + color + perspective.
4. **Fix text BEFORE upscaling.** Upscaling a garbled glyph just sharpens the wrong letter; upscaling a correct glyph improves crispness.
5. **Hybrid composite is the professional default** for any text-critical deliverable (logos, covers, UI, ads).

## F. MULTILINGUAL / HEBREW
- English short phrases are by far the most reliable.
- **No model reliably renders Hebrew** — RTL, final-form letters (sofit), and niqqud are routine failure points. **Do not let the model render Hebrew.** Generate the text area blank (or English placeholder) and set Hebrew type in a design tool with a proper RTL font. Only reliable path to clean Hebrew today.
- **Proven (Reve, 2026):** an in-scene shelter sign rendered as "מכל מוגן" — gibberish; should read "מרחב מוגן" / "מקלט". In an Israel scene, keep ALL in-scene signage **ENGLISH** ("BOMB SHELTER", "SHELTER") or leave it blank — never let the model write Hebrew.

---
*Sources: blog.reve.com (Reve 2.0); morphic & reveai.org (Reve); Ideogram official docs (text & typography, prompting fundamentals); imagetoprompt.dev & picassoia (Ideogram); p20v & stockimg & makeuseof & artlist (text accuracy across models); aipure (Flux vs MJ vs GPT-4o vs Ideogram); arXiv Glyph-ByT5-v2 (multilingual visual text). Verified 2025–2026.*
