# 06 — Tool Adapters

One concept, many engines. Build the 8-block stack once, then translate per the tool's parser and quirks.

## REVE 2.0 (the contest tool) — deep notes
- **Architecture: layout-first.** Builds a structured, editable node graph (each element addressable with position/size/local description) *then* renders. Think "editing a document," not "re-rolling a prompt." → **You can fix one hand/sign/face without disturbing lighting or the rest of the scene.** This is the unfair advantage over MJ/Flux entrants.
- **Strengths:** best-in-class **legible text** (dedicated typography pass); **native 4K (up to 4096²), print-ready** (no upscale dice-roll); **extreme prompt adherence** (~9.5/10 — "one of the most obedient models tested" — honors horizon placement, spatial relationships, composition almost literally).
- **Weaknesses:** fine organic micro-detail (~7.7/10); **dense multi-subject scenes, crowds, physical interactions (pouring liquid), and complex hands** falter; crowds lack individual faces; faces/complex hands still trail GPT Image 2. **"Studio-photograph" bias** — it simulates *the world as photographed in a controlled studio*; natural/physics-heavy light can falter outside familiar photographic archetypes. Opinionated house aesthetic — push against it for "originality."
- **Prompting:** natural language, structured like a **camera setup** — open with a fixed spatial anchor (camera angle → environment → subject) THEN layer detail. Opposite of Midjourney keyword-soup. Vague prompts waste its biggest strength.
- **Settings:** native ~2048²; optional 4K upscale; supports 3:2, 16:9, etc.; <20s gen.
- **Turn "enhance prompt" OFF** for serious work — keep deterministic control; write the full prompt yourself.
- **Negatives:** no reliable negative field — use **positive layout specification + targeted edits**; state what you DO want, then edit out what slips in.
- **References + conversational edits** are first-class and lossless across iterations.
- **Contest tactic:** 1–2 hero subjects; make any crowd/hand the *editable element* you refine separately; frame the concept as a deliberate photographic setup.

## Cross-tool quick table
| Tool | Prompt style | Negatives | Text | Notes |
|---|---|---|---|---|
| **Reve 2.0** | natural, camera-setup order | ignored | excellent | layout-first edits; 4K; studio bias; 1–2 heroes |
| **Midjourney v7** | keyword + `--ar --no --style raw --stylize` | `--no` | weak | strong aesthetic; `--style raw` + low `--stylize` for realism; 1:1 fewer distortions |
| **Flux / Flux 2** | natural language, long descriptive | yes | very strong | rewards texture detail; great hands vs SDXL; open-weight |
| **GPT-image / Image 2** | literal natural-language instructions | ignored→describe positively | highest | follows detailed briefs; best text integration |
| **Imagen 3/4** | descriptive natural language | limited | strong | clean faces/hands/light/text; weak on small faces in busy scenes |
| **Nano Banana 2 (Gemini)** | conversational, multi-reference | ignored | strong | up to 14 refs; Google-Search-grounded; iterate across turns; see nano-banana-2 skill |
| **Stable Diffusion / SDXL** | tag + weighted negatives | strong | weak | ControlNet/inpaint/LoRA control; the neg-heavy workflow |

## Translating one prompt across tools
- **Reve / GPT-image / Imagen / Nano Banana:** write the 8-block stack as flowing natural language; convert every "no X" to its positive opposite; drop weighted-negative syntax.
- **Midjourney:** compress to comma keywords; move forbidden items to `--no`; add `--style raw --stylize 50-150 --ar W:H`; for realism avoid `--stylize 600+`.
- **SD/SDXL/Flux:** keep the positive stack, ADD the universal weighted negative block (ch.01 §7), use ControlNet/OpenPose for pose/hand control, inpaint failures at 0.35–0.5 denoise.
- **Realism floor that ports everywhere:** real camera+lens+aperture, ONE named light + shadow direction, anti-plastic texture callouts, kill the blacklist words.

## Routing by job
- **Text-critical (logo, poster, signage):** GPT-image or Ideogram or Reve. Never Midjourney for exact text.
- **Skin/portrait realism:** Reve, Seedream 4.5, Flux, or SD+inpaint.
- **Wildlife/nature:** Reve or Imagen or Flux with the NatGeo template (ch.02 §3).
- **Multi-reference compositing / real-world grounding:** Nano Banana 2.
- **Maximum surgical control / consistent character:** SD/Flux + ControlNet + LoRA.
- **Hebrew text:** none — composite in post (ch.03 §F).

---
*Sources: curiousrefuge & decrypt & felloai & theplanettools & wavespeed & bestimageprompts (Reve 2.0 architecture/specs/prompting); venturebeat (Reve 1.0); artlist & z-image (Seedream); allaboutai (Imagen); nano-banana-2 skill (Gemini). Tool layer drifts monthly — re-verify before relying.*
