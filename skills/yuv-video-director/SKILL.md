---
name: yuv-video-director
description: >
  Yuval's all-in-one AI video pipeline. Turns an idea/script into a finished, on-brand MP4 by
  orchestrating HyperFrames (HTML→deterministic video render), Lottie (branded motion graphics),
  ManimCE (math / neural-network / concept animations), and a transcribe→approve caption flow —
  all wrapped in the YUV.AI Neon Phoenix brand via a frame.md. Use whenever Yuval wants to make,
  edit, or explain something as a video: promo, explainer, launch, social reel, "make a video
  about X", "explain X as a video", "neural network animation", "turn this into a video",
  captioned tutorial, 16:9 or 9:16. Triggers: video, explainer, promo, reel, manim, lottie,
  hyperframes, animation, "make a video", "explain ... as a video", מצגת וידאו, סרטון, הסבר וידאו.
  Routes each beat to the right engine, wraps in brand, self-verifies, and renders.
---

# yuv-video-director

The conductor for YUV.AI video. You (the agent) decide **what each beat needs**, route it to the
right **engine**, compose everything into **one HyperFrames composition**, wrap it in the **YUV.AI
Neon Phoenix** brand, **self-verify**, and **render** to MP4. This skill is the router + the
working reference implementations; load a reference file only when that engine is in play.

> **Design source of truth:** the `yuv-design-system` skill (Neon mode — pink `#FF1464`, cyan
> `#00E5FF`, rich-black/white, Anton+Inter+JetBrains Mono, neural-net phoenix motif). The video
> form of it is **`frame.md`** — see [references/frame-md.md](references/frame-md.md). Bundled
> template: [assets/FRAME.md](assets/FRAME.md). Drop it in the project root; HyperFrames reads it.

## The one law (decides everything)

HyperFrames renders by **seeking each frame in headless Chrome → FFmpeg** (`frameIndex = floor(t·fps)`,
same input → same output). So every visual is one of two kinds:

| Pattern | Runs… | Engines | Rule |
|---|---|---|---|
| **Live seekable adapter** | *inside* the render, driven to time `t` per frame | GSAP, Lottie (`window.__hfLottie`), Three.js, a canvas driven by a GSAP proxy `onUpdate` | must be **clock-driven** — no `Date.now()`, `Math.random()` (seed a mulberry32), `setTimeout`, or `.play()` |
| **Pre-rendered asset** | *offline*, outputs a file, imported as a clip | **ManimCE** (Python→MP4/alpha), TTS audio, background-removal | render first, then drop in as a `<video>`/asset clip |

**If it can be seeked, it's an adapter. If it can't, pre-render it.** Manim is *always* a pre-rendered clip — it has its own renderer and runs in Python; it can never be a live adapter.

## Route each beat to an engine

```
"explain a concept / math / neural network / algorithm / training"  → ManimCE   (pre-rendered clip)
"branded motion: logo sting · stat reveal · icon pop · pulse"        → Lottie    (live, lottie-web)
"kinetic captions · titles · reveals · transitions · data callouts"  → GSAP      (live)  ← default
"3D / spatial"                                                       → Three.js  (live)   (Babylon NOT used)
speech → captions                                                    → transcribe + approve webapp (see video-edit skill)
no voiceover provided                                                → TTS (Kokoro: npx hyperframes tts)
brand colors / fonts / motifs                                        → frame.md  (picked up front)
```

GSAP is the reliable default for text/motion. Reach for Lottie for *designed* branded graphics, Manim for *explaining* an idea.

## Workflow

1. **Plan the beats.** Narrative arc + which engine each beat needs. Pick 16:9 and/or 9:16.
2. **Set the brand.** Ensure `FRAME.md` is in the project root (copy [assets/FRAME.md](assets/FRAME.md)). All colors/fonts/motifs come from it — never invent. **Three brand must-haves on every video** (see [references/brand-kit.md](references/brand-kit.md) + [references/cinematic.md](references/cinematic.md)): the **real phoenix logo** ([assets/logo-phoenix.png](assets/logo-phoenix.png)) at the reveal + end card, a **real featured Lottie** (generate one — [assets/lottie-burst-generator.py](assets/lottie-burst-generator.py)), and the **link end-card** (logo + "LET'S FLY HIGH" + the full link set + CTA). For teaser/social pacing see [references/editing.md](references/editing.md); for psychological/cliffhanger/FOMO cuts see [references/cinematic.md](references/cinematic.md).
3. **Pre-render the asset beats first** (so they exist as clips):
   - **Manim** → [references/manim.md](references/manim.md) + [assets/manim-scene-template.py](assets/manim-scene-template.py). Render `py -m manim render -qh --fps 30 scene.py SceneName`, copy the MP4 into `assets/`.
   - **Captions/TTS** → reuse the `video-edit` skill (transcribe → approve webapp → sync) and `npx hyperframes tts`.
4. **Scaffold + compose.** `npx hyperframes init <slug> --non-interactive`. Author `index.html` (the `hyperframes` skill is the contract). Use:
   - the seekable **neural-net field** background → [assets/neural-net-field.js](assets/neural-net-field.js)
   - **Lottie** the brand way → [references/lottie.md](references/lottie.md) + [assets/neural-pulse.json](assets/neural-pulse.json)
   - the **Manim** render as a `<video class="clip" muted playsinline>` body clip
   - GSAP entrances per scene, a neon **flash** transition on each boundary, fade-out only on the final scene
   - for **teaser / social** pacing (fast hard cuts, kinetic word-slams, a hook montage, glitch/chromatic stabs) → [references/editing.md](references/editing.md) — cut it like a producer, not a slideshow
5. **Self-verify (gates).** [references/gates.md](references/gates.md): `npx hyperframes lint` (0 errors) → `validate` (0 console errors, WCAG AA) → render → spot-check 5 frames across the timeline. Fix → re-run. Lottie MUST be screenshot-verified (the Skottie-vs-lottie-web trap).
6. **Render.** `npx hyperframes render --fps 30 --output renders/<name>_FINAL.mp4`. For vertical, clone with a 1080×1920 layout (see `video-edit`).

## Prerequisites (check first; degrade gracefully)

See [references/prereqs.md](references/prereqs.md). Need **Node 22+**, **FFmpeg**, **Python 3.11+ with pip** (Manim/captions). On this machine: real Python is **`py` → `C:\Python313`** (the bare `python` is Hermes' venv with NO pip — don't use it). ManimCE installs via `py -m pip install manim` (no LaTeX needed if you author with `Text()`/`MarkupText`, not `Tex`/`MathTex`). If Manim isn't available → skip math beats or offer to install; never hard-fail the whole video.

## What this skill bundles (reference implementations that lint + render)

| File | What it is |
|---|---|
| [assets/FRAME.md](assets/FRAME.md) | YUV.AI Neon Phoenix video frame spec (rebranded from HeyGen's Coral pack) |
| [assets/neural-net-field.js](assets/neural-net-field.js) | Deterministic, seekable neural-net phoenix canvas background |
| [assets/neural-pulse.json](assets/neural-pulse.json) | Hand-authored Bodymovin Lottie (renders in lottie-web, not just Skottie) |
| [assets/manim-scene-template.py](assets/manim-scene-template.py) | ManimCE scene template, neon brand styling, Text-only (no LaTeX) |
| [assets/Anton-Regular.woff2](assets/Anton-Regular.woff2) | Local Anton (renderer doesn't auto-resolve it; declare `@font-face`) |
| [references/composition-pattern.md](references/composition-pattern.md) | The full multi-engine `index.html` pattern (field + Lottie + Manim clip + GSAP + flash) |

## Companion skills

`hyperframes` (composition contract — always invoke when authoring), `hyperframes-cli`, `lottie`,
`video-edit` (transcribe + approve webapp), `yuv-design-system` (brand). This skill orchestrates them.
