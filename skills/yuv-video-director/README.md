# yuv-video-director

**Yuval's all-in-one AI video pipeline — one agent, every engine.**
Turn an idea or a script into a finished, on-brand MP4: the skill plans the beats, routes each one
to the right engine (HyperFrames · Lottie · ManimCE · captions), wraps it in the **YUV.AI Neon
Phoenix** brand via a `frame.md`, self-verifies, and renders.

![hero](assets/FRAME.md)

---

## Install

```bash
# from the ai-agents-skills monorepo (canonical), or standalone:
npx skills add hoodini/yuv-video-director
```
It installs into your agents' skill dirs (Claude Code, Copilot, Cursor, Hermes, …). Then just ask
your agent for a video — the skill self-selects.

**Prerequisites:** Node 22+, FFmpeg (always); Python 3.11+ with pip + ManimCE (`py -m pip install
manim`) for math/neural-net beats; the skill degrades gracefully if Manim is absent. See
[`references/prereqs.md`](references/prereqs.md).

---

## What it does

HyperFrames renders by **seeking each frame in headless Chrome → FFmpeg** (deterministic). So every
visual is either a **live seekable adapter** (runs inside the render, clock-driven) or a
**pre-rendered asset** (made offline, imported as a clip). The skill routes each beat accordingly:

| Beat | Engine | Pattern |
|---|---|---|
| Explain a concept / math / **neural network** / algorithm | **ManimCE** | pre-rendered clip |
| Branded motion — logo sting, stat reveal, pulse | **Lottie** (lottie-web) | live |
| Kinetic captions, titles, reveals, transitions | **GSAP** | live (default) |
| 3D / spatial | **Three.js** | live |
| Speech → captions | transcribe → **approve webapp** → sync | (via `video-edit`) |
| Narration with no VO | **TTS** (Kokoro) | pre-rendered |
| Brand colors / fonts / motifs | **`frame.md`** | picked up front |

Brand = **Neon Phoenix**: pink `#FF1464` + cyan `#00E5FF` on rich-black/white, the rainbow
phoenix gradient + neural-net field, Anton + Inter + JetBrains Mono. Cut it like a **teaser**
(fast shots, kinetic slams, a montage, hard cuts + stabs) — see [`references/editing.md`](references/editing.md).

---

## Examples

Just talk to your agent:

```
"Using yuv-video-director, make a 30s explainer on how a neural network learns
 vs. the human brain — on-brand, with a Manim animation."

"Make a punchy 20s social teaser for my new skill — full palette, code on screen,
 lots of effects."

"Turn this script into a 16:9 + 9:16 promo with captions and a logo sting."
```

What the agent does (the shipped reference video, `neural-explained`):
1. Drops [`assets/FRAME.md`](assets/FRAME.md) in the project → brand locked.
2. Writes + renders a **Manim** scene (`assets/manim-scene-template.py`) → `manim.mp4`.
3. Scaffolds HyperFrames, composes `index.html`: the seekable **neural-net field**
   (`assets/neural-net-field.js`) + a **Lottie** pulse (`assets/neural-pulse.json`) + the Manim
   clip + GSAP slams + glitch/flash stabs.
4. Runs the **gates** ([`references/gates.md`](references/gates.md)): `lint` (0 errors) → `validate`
   (0 console errors, WCAG AA) → `render` → spot-check 5 frames.
5. Outputs `renders/<name>_FINAL.mp4`.

---

## What's inside

```
SKILL.md                         the router — read first
references/
  frame-md.md                    the design layer (frame.md) + how it's consumed
  manim.md                       ManimCE setup, brand rules, render (no LaTeX needed)
  lottie.md                      lottie-web wiring + the Skottie↔lottie-web trap
  editing.md                     teaser/commercial cutting rhythm + kinetic slams
  gates.md                       the self-verify / self-heal loop
  prereqs.md                     environment + graceful degradation
  composition-pattern.md         the full multi-engine index.html pattern
assets/
  FRAME.md                       YUV.AI Neon Phoenix video frame spec
  neural-net-field.js            deterministic, seekable phoenix-field canvas
  neural-pulse.json              Bodymovin Lottie (verified in lottie-web)
  manim-scene-template.py        neural-net-vs-brain ManimCE scene
  Anton-Regular.woff2            local display font (renderer doesn't auto-resolve it)
```

Every asset is a **working reference implementation** — it lints and renders as-is.

## Companion skills
`hyperframes` (composition contract — always invoke when authoring), `hyperframes-cli`, `lottie`,
`video-edit` (transcribe + approve webapp), `yuv-design-system` (brand). This skill orchestrates them.

---
Maintained by [@hoodini](https://github.com/hoodini) · [yuv.ai](https://yuv.ai) · *Let's fly high.*
