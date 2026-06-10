# yuv-video-director

**Yuval's all-in-one AI video pipeline — one agent, every engine, broadcast-grade output.**

Turns an idea, a script, or a real video file into a finished, on-brand MP4 by orchestrating
**HyperFrames** (HTML → deterministic render) · **Lottie** (content-synced transparent motion
graphics) · **ManimCE** (math / neural-net animation) · **faster-whisper** (Hebrew/English
transcription + approval gate) — wrapped in the **YUV.AI Neon Phoenix** brand via `frame.md`.

Real outputs shipped with this exact skill:
- 📺 **Channel-12 news clip, branded** — Hebrew karaoke captions + 6 transparent Lotties that
  illustrate each spoken term at the exact moment it's said (16:9 + 9:16).
- 🎬 **"What is a neural network" cinematic teaser** — 46s Netflix-promo pacing: cold-open slams,
  Manim bursts, brain-vs-machine face-off, FOMO montage, cliffhanger.
- 🚀 **Multi-engine brand promos** — neural-net field + Lottie + Manim + GSAP in one composition.

---

## Install

| Where | How |
|---|---|
| **Claude Code** (this machine) | already installed at `~/.claude/skills/yuv-video-director` |
| **Copilot / Cursor / Hermes / all agents** | already installed at `~/.agents/skills/yuv-video-director` |
| **Claude Desktop (Cowork)** | synced into the Cowork skills dir (see Sync section) |
| **Any new machine** | `npx skills add hoodini/yuv-video-director` (standalone) or `npx skills add hoodini/ai-agents-skills` (whole library) |

**Prerequisites:** Node 22+, FFmpeg (always) · Python 3.11+ **with pip** for Manim/transcription.
⚠️ On Yuval's machine use the **`py` launcher** (`py -m pip`, `py -m manim`) — bare `python` is a
venv without pip. ManimCE: `py -m pip install manim` (no LaTeX needed — scenes use `Text()` only).
Captions: `py -m pip install faster-whisper`. The skill degrades gracefully if Manim is absent.

---

## How to use — three playbooks

### 1 · Brand-edit a real video (the Channel-12 playbook)
> *"קח את הסרטון הזה מהריאיון, תמתג אותו: כתוביות קריוקי, לוטי שממחישים את מה שנאמר, 16:9 ו-9:16"*

1. Transcribe (faster-whisper `large-v3`, `language="he"`, word timestamps) → **show the user
   `transcript_review.txt` and WAIT for corrections** (Hebrew mishears are guaranteed).
2. Read the transcript like an editor → hard-code **director beats**: (start, end, lottie, label)
   for each spoken concept. Generate content Lotties with
   [assets/gen_content_lotties.py](assets/gen_content_lotties.py) or author new ones in its pattern.
3. Overlays are **fully transparent** (no chips — drop-shadow only); the thesis concept gets a
   bigger, longer **hero beat**. Captions: ≤2 lines (char-budget per ratio), below any chyron,
   karaoke per word, punch-words pink.
4. Name-super open + phoenix/links outro ([references/brand-kit.md](references/brand-kit.md)) +
   synthesized music bed under the voice. Render both ratios. Gates: lint 0 errors → validate
   (catches missing-lottie 404s!) → render → Read spot frames.

### 2 · Cinematic teaser-explainer (the neural-net playbook)
> *"תסביר מה זה X בסרטון — אבל בסגנון טיזר נטפליקס, FOMO, קליפהנגר"*

Follow [references/teaser-explainer.md](references/teaser-explainer.md) exactly: cold-open
statement slams (~1.1s each) → word-slam + **Manim BURSTS** (scrub the rendered scene, window the
4–5 most active seconds with `data-media-start` — never play it through) → split-screen face-off →
FOMO montage of real-life examples → quiet cliffhanger question → brand outro. Synthesized teaser
music (kick / bass hits on cuts / risers / tension drone). ManimCE scene template:
[assets/what_is_nn.py](assets/what_is_nn.py).

### 3 · Multi-engine brand promo
> *"Make a 30s promo for my new skill — full palette, code on screen, mind-blowing effects"*

[references/composition-pattern.md](references/composition-pattern.md) +
[references/editing.md](references/editing.md) (teaser rhythm, kinetic slams) +
[references/cinematic.md](references/cinematic.md) (psychological arc, the drop, brand must-haves).

---

## File map

```
SKILL.md                          router — the one law (seekable vs pre-rendered), engine routing, workflow
references/
  teaser-explainer.md             ★ the cinematic teaser formula + content-lottie beats + seek-modulo fix
  lottie.md                       lottie-web wiring, Skottie trap, seek-clamp gotcha, transparency standard
  manim.md                        ManimCE setup/gotchas (py launcher, no LaTeX, fade-swap, z_index)
  editing.md                      teaser cutting rhythm, kinetic slams, stabs
  cinematic.md                    psychological/cliffhanger arc + brand must-haves
  brand-kit.md                    logo + canonical link set + end-card rule
  frame-md.md                     the frame.md design layer
  composition-pattern.md          multi-engine index.html pattern
  gates.md                        self-verify loop (lint → validate → render → Read frames)
  prereqs.md                      environment + graceful degradation
assets/
  gen_content_lotties.py          ★ generator: 6 content lotties (transparent, persistent+continuous)
  wa-collapse / decode-beam / eye-read / ghost-line / orb-extract / brain-fire .json
  lottie-burst-generator.py       phoenix-burst generator
  phoenix-burst.json / neural-pulse.json
  what_is_nn.py                   ★ neuron→network→training ManimCE scene (34.5s)
  manim-scene-template.py         brain-vs-network ManimCE scene
  neural-net-field.js             seekable neural-net phoenix canvas background
  FRAME.md                        Neon Phoenix video frame spec
  logo-phoenix.png / Anton-Regular.woff2
```

## Critical gotchas (hard-won — read before building)

1. **Lottie seek-clamp**: HyperFrames seeks lotties to *composition* time; a section starting past
   the lottie's duration freezes it on the last frame. **Always use the modulo `L()` wrapper**
   from teaser-explainer.md.
2. **Missing lottie = silent failure**: lint won't catch a missing JSON — **`validate` will**
   (console 404). Run it before every render.
3. **Transparency check**: render the lottie grid over an odd-colored page (`#2d1a3a`); any opaque
   canvas box shows instantly.
4. **Hebrew fonts**: the renderer doesn't auto-resolve Rubik/Anton — fetch woff2 with a
   `text=<full alphabet>` Google-Fonts subset and `@font-face` it. New strings ⇒ refetch.
5. **Track-index collisions**: same-track clips must not overlap (captions 20+, lotties 60+).
6. **PowerShell cwd resets every call** — `Set-Location` in every command; use `py`, never `python`.
7. **Determinism**: no `Date.now()` / `Math.random()` — mulberry32 + GSAP-proxy-driven canvas only.

## Scaling tip
For big builds, fan out a **Workflow**: one agent authors+renders the Manim scene, one authors+
screenshot-verifies the Lottie pack — in parallel, each self-verifying with rendered frames —
while the main loop builds the composition. This is how the shipped teaser was made.

---
Maintained by [@hoodini](https://github.com/hoodini) · [yuv.ai](https://yuv.ai) · *Let's fly high.* 🚀
