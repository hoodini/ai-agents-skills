# Teaser-Explainer — the cinematic "Netflix promo" formula

For "explain X" requests that must feel like a **TV/film teaser** (FOMO, dopamine, cliffhanger) —
not a lecture. Worked example shipped: the 46.3s "מה זה רשת נוירונים" teaser.

## The arc (timing table from the shipped cut)
```
0.0–6.4   COLD OPEN     5 statement slams, ~1.1s each, hard cuts + glitch/flash stabs.
                        Question → number → image-beat (lottie) → counter-question → 3-word answer
                        ("המוח שלך?" / "86 מיליארד נוירונים." / brain lottie / "ומכונה?" / "בדיוק. באותה. דרך.")
6.4–21.9  CONTENT BURSTS word-slam ("נוירון.") → 4s of the BEST manim moment → slam ("רשת.") → 4s →
                        slam ("אימון.") → 5s. Each burst gets ONE short caption pill.
21.9–29.4 FACE-OFF      split screen: brain lottie | machine lottie, alternating lines
                        (cyan vs pink), then the unifier ("אותו רעיון.") in gradient.
29.4–34.6 FOMO MONTAGE  3 real-life examples, 1.3s each, text + small lottie, hard cuts
                        ("הטלפון מזהה פנים / הרופא מאבחן מוקדם / המכונית רואה"), then "וזה רק ההתחלה."
34.6–40.8 CLIFFHANGER   soft dip → SLOW (the contrast IS the drama): question → hero lottie +
                        thesis line → final open question alone on screen ("מה עוד היא תלמד?")
40.8–end  OUTRO         phoenix burst + name + brand + links, fast, fade.
```
Rules: statements ≥0.9s (readable) ≤1.4s (urgent); stabs on every hard cut EXCEPT into the
cliffhanger (dip instead); zoom-drift (scale 1→1.05 linear) on every held statement; one idea per cut.

## Manim BURSTS, not playthroughs
Never play an explainer scene start-to-finish in a teaser. Scrub the rendered MP4 (ffmpeg frames →
Read), pick the 4–5 most ACTIVE seconds per chapter, and window them with `data-media-start`:
```html
<video class="mv clip" data-start="7.1" data-duration="4.0" data-media-start="7.4"
       data-track-index="0" src="assets/WhatIsNN.mp4" muted playsinline></video>
```
Sequential windows can share track 0. Introduce each window with a 0.7s word-slam.
Bundled scene: [../assets/what_is_nn.py](../assets/what_is_nn.py) (neuron → 4-6-6-2 network →
training/LOSS, 34.5s, no LaTeX, Segoe UI, brand palette).

## Content-synced transparent Lottie beats (the core craft)
The Lotties must ILLUSTRATE WHAT IS BEING SAID, exactly when it is said — that is the whole point.
1. Read the transcript like an editor; list the spoken concepts and their timestamps.
2. Hard-code DIRECTOR BEATS (start, end, lottie, label, position) — don't keyword-auto-match blindly.
3. Overlays are FULLY TRANSPARENT: no chip, no border — just the animation + label with
   `filter: drop-shadow(...)` for separation. Give the thesis concept a bigger, longer "hero" beat.
4. Every animation must be PERSISTENT + CONTINUOUS (icon always drawn, accent motion loops) so any
   window reads. Generator with 6 production-grade examples (WhatsApp-collapse, decode-beam,
   eye-read, ghost-line hero, orb-extract, brain-fire):
   [../assets/gen_content_lotties.py](../assets/gen_content_lotties.py) → JSONs in assets/.
5. VERIFY transparency: render a test grid over an ODD-colored page (#2d1a3a) — any opaque canvas
   bg shows instantly. Sample 3 timestamps; every animation must read in all three.

## The seek-modulo fix (CRITICAL gotcha)
HyperFrames' lottie adapter seeks every player to COMPOSITION time. A lottie whose total duration
is shorter than the section's start time clamps to its last frame (often invisible). Wrap every
loadAnimation:
```js
const L=(id,p)=>{
  const a=lottie.loadAnimation({container:document.getElementById(id),renderer:"svg",loop:true,autoplay:false,path:p});
  const o=a.goToAndStop.bind(a);
  a.goToAndStop=(v,f)=>{const d=a.getDuration(false)*1000;o(f?v:(d>0?v%d:v),f);};
  window.__hfLottie.push(a);
};
```
Deterministic (pure modulo). Use it in EVERY composition — it is harmless when not needed.

## Teaser music (synthesized, royalty-free)
No VO → the music drives. numpy-synthesize: kick every ~0.46s through the rush sections; 40Hz
bass hits on every hard cut; 1.8s noise+sweep risers ending AT each drop; kill the kick + quiet
high-tremolo drone during the cliffhanger (duck the pad ~0.45); swell into the outro; mix
`data-volume` ~0.5. Working generator pattern: the project's gen_music_teaser.py.

## Self-audit before delivery (run it like an editor)
Extract 10+ frames across the cut and Read them: every slam readable? every lottie PRESENT
(missing asset = silent failure — run `validate`, it catches the 404 as a console error)? stabs on
cuts? cliffhanger slow and clean? outro has logo+name+links? Fix and re-render until yes.
