---
name: yuv-reel-covers
description: >
  Generate unified, on-brand Instagram Reel covers for Yuval (YUV.AI Neon Phoenix system) — the
  signature look is a giant Hebrew headline BEHIND the subject cutout + a punch line IN FRONT
  (depth effect), on rich black with a dim neural-net field, series-colored chip + phoenix mark.
  Use whenever Yuval asks for an Instagram/Reel/TikTok/YouTube cover, thumbnail, עטיפה, קאבר,
  תמבנייל, cover image for a video, or wants his Instagram grid to look consistent. One command
  per cover; background removal included in the pipeline.
---

# yuv-reel-covers

Unified Reel-cover system so the Instagram grid reads as ONE brand. Canvas 1080×1920, all key
content inside the **3:4 grid-crop safe zone (y 285–1635)**. Two templates, one DNA.

## The formula (what makes the grid uniform)
- **Always**: rich-black `#0A0A0A` ground + dim neural-net field + vignette. Never white, never a raw screenshot.
- **Series chip** (top-left, mono, outline pill) + **phoenix mark** (top-right) — SAME positions every cover.
- **Series colors** (this is the variety inside the uniformity):
  pink `#FF1464` = news / hot takes / Claude · cyan `#00E5FF` = tutorials / dev · amber `#F9AD45` = fun / wildlife.
- **`behind` template** (the signature): giant Rubik-900 headline (1–3 words, auto-sized), one word
  in the series color, partially BEHIND the subject cutout; punch line IN FRONT at chest level
  (`--front-top`, default 1285). Cutout gets a series-color rim glow.
- **`stack` template** (no photo): giant glowing Anton/Rubik stacked text + Rubik subtitle — for
  tool/code covers (e.g. "CLAUDE CODE / המדריך המלא").
- Handle `@yuval_770 · YUV.AI` bottom-center, small mono.

## How to run (from this skill's folder or any project with assets/+fonts/ copied)
```powershell
# 0) prereqs: Node 22+, FFmpeg. Builder is pure-stdlib Python (py on Windows, python3 on Mac).
# 1) one-time per new photo — local AI background removal:
npx --yes hyperframes@latest remove-background photo.png -o assets/cutout.png
# 2) generate a cover (renders headless via HyperFrames -> PNG):
py gen_cover.py behind --img assets/cutout.png --back "קלוד דסקטופ" --front "משנה הכל!" `
   --accent-back 1 --color pink --tag "CLAUDE · AI" --out my-cover
py gen_cover.py stack --back "CLAUDE CODE" --sub "המדריך המלא" --accent-back -2 --color cyan --tag DEV --out cc
```
Args: `--accent-back N` = which word of the BACK text gets the series color (-1 none, -2 all);
`--size-back` overrides auto-fit; `--front-top` moves the front line (keep at chest, never the face).
A default cutout of Yuval (studio) ships in `assets/yuval-cutout.png`.

## Rules for the agent
1. Headline ≤3 words back + ≤2 words front. If longer — rewrite tighter; this is a poster, not a caption.
2. Pick the series color by content type (mapping above) — don't mix colors in one cover.
3. Front text must NOT cover the face — chest level only; adjust `--front-top` if the photo differs.
4. New photo ⇒ remove-background FIRST (step 1); never paste a rectangular photo.
5. Read the rendered PNG and check: headline readable behind the head, chip+phoenix inside safe zone,
   nothing critical above y=285 or below y=1635.
6. Hebrew glyphs come from the bundled Rubik subset — exotic punctuation may be missing; refetch with
   builders/fetch_hebrew_fonts.py from yuv-video-director if needed.
