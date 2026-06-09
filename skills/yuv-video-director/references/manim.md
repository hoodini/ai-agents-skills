# Manim — math / concept / neural-network beats (pre-rendered clip)

ManimCE renders its **own** video offline → import the MP4 as a `<video>` clip in HyperFrames.
It is **never** a live adapter.

## Why ManimCE (not 3b1b/manimgl)
Both MIT/free. **ManimCE** has stable API + far more examples (the model writes correct scenes more
often), clean `pip install`, and clean transparent export. ManimGL's only edge (live OpenGL preview)
is useless in an automated render pipeline. Use **ManimCE**.

## Install (Windows)
Real Python here is `py` → `C:\Python313` (bare `python` is Hermes' venv, **no pip**). Then:
```
py -m pip install manim
```
pycairo + manimpango ship wheels — **no LaTeX needed** if you author with `Text()` / `MarkupText`
(Pango), NOT `Tex` / `MathTex` (those need a TeX distro). Avoid LaTeX to dodge the Windows hurdle.

## Authoring rules (brand + reliability)
- `config.background_color = "#0A0A0A"`; colors pink `#FF1464`, cyan `#00E5FF`, rainbow stops for nodes.
- **Fonts:** `Text.set_default(font="Segoe UI")` at the top of `construct` — the Pango default is a
  serif and reads off-brand. (Anton via Pango needs a .ttf registered; Segoe UI is a clean always-present sans.)
- Build neural nets from `Dot` + `Line`; fake glow with a larger low-opacity `Dot` behind each node;
  set `z_index` so edges < glows < dots < labels.
- **Swap notes by fade, not `Transform`** — morphing different-length `Text` looks garbled.
- Avoid `corner_radius=` on `SurroundingRectangle`; avoid `get_stroke_opacity()*x` (use a fixed value);
  bars use `set_color_by_gradient(PINK, CYAN)` not `set_fill(color=[...])`.
- **Numbers come from the script** — don't fabricate stats; the user supplied 7B/70B/175B → 14/140/350 GB.

## Render
```
py -m manim render -ql --fps 15 scene.py SceneName     # fast test — catch API errors first
py -m manim render -qh --fps 30 scene.py SceneName     # final 1080p30
```
Output: `media/videos/<scene>/1080p30/SceneName.mp4`. Copy it into the project `assets/` and wire as
a `<video class="clip" muted playsinline data-start=.. data-duration=.. data-track-index=0>`.

Template: **[../assets/manim-scene-template.py](../assets/manim-scene-template.py)** — the
neural-network-vs-human-brain explainer (weights training then freezing; knowledge-as-structure in
the brain; params → size/accuracy/hallucinations). Adapt copy/structure per topic.
