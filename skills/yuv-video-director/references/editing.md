# Editing — cut it like a teaser, not a slideshow

The difference between "AI made a video" and "a producer made a teaser" is the **edit**: shot
length, rhythm, hard cuts, kinetic slams, a montage, a build → reveal. Default to this for any
social/promo/teaser; relax to longer holds for explainers.

## Shot rhythm
- **Hook in the first ~1s.** Open on the boldest thing (logo slam + particle burst), not a slow fade.
- **Short shots.** Montage shots **0.4–0.9s**; statement slams **0.6–0.9s**; a "rest" beat (terminal,
  code, the Manim clip) can run **3–5s** so the eye recovers. Alternate fast/slow — that contrast IS the pacing.
- **Hard cuts are the default.** A teaser is mostly hard cuts (clip ends → next clip starts). Don't
  put a transition on every cut — that reads slow. Reserve effects for **hits**.
- **Stabs on the hits.** A quick **glitch + chromatic flash** (~0.08–0.16s) on the big beats (logo,
  each engine slam, the brain beats, the title) punctuates without slowing.

## Kinetic slams (the teaser staple)
Single word, full-screen, Anton uppercase, scale-punch in, **hard cut out** (no exit anim):
```js
const slam = (sel, t) => tl.from(sel, { scale:0.35, opacity:0, duration:0.2, ease:"back.out(2.2)", overwrite:"auto" }, t);
slam("#e1 .slam", 6.7);   // "HYPERFRAMES"
```
Each slam is its own ~0.6–0.9s clip. Rainbow-`grad` the brand words, neon-glow the punch words.
Alternate color/size between consecutive slams so they don't blur together.

## Structure that works (the shipped teaser)
```
0.0  HOOK montage — YUV.AI slam+burst · code flash · palette flash · "VIDEO" slam   (4 shots, ~0.5s each)
2.25 PROMISE — "ONE PROMPT" slam → terminal types the command + agent steps          (rest beat ~3.7s)
6.7  ENGINES — HYPERFRAMES · MANIM · LOTTIE · FRAME.MD                                (4 slams, ~0.85s)
10.2 BRAIN  — "TRAIN" / "FREEZE" slams → Manim clip beat                              (2 slams + 5s clip)
16.4 PROOF  — code editor reveals the real HTML                                       (rest beat ~3.6s)
20.0 CLIMAX — "LET'S FLY HIGH" rainbow slam + burst + CTA → fade                      (~7s payoff)
```
Build → rest → build → rest → payoff. Stabs at: every slam-in, the clip-ins, the title.

## Two-track caption hint
Don't put exit anims on shots (rule). The hard cut between clips IS the exit. Only the final clip fades.

## Real WebGL shader transitions (optional, heavier)
The catalog's `glitch`, `swirl-vortex`, `gravitational-lens`, `chromatic-radial-split`, `light-leak`,
`cinematic-zoom` etc. (`npx hyperframes add <name>`) install as **showcase blocks** (full demo
compositions with their own content) — not drop-in A→B transitions. True frame-to-frame shader
transitions use the **`@hyperframes/shader-transitions`** package API (capture from/to textures).
For most teasers, the hand-built **glitch + chromatic flash stab** above is faster, deterministic,
and reads just as punchy. Reach for the shader package only when a specific hero transition demands it.

## Pacing checklist
- [ ] Hook in ≤1s. [ ] No shot the eye can't read (slams ≥0.5s on screen). [ ] Fast/slow alternation.
- [ ] Hard cuts default; stabs only on hits. [ ] One idea per shot. [ ] Climax is the longest hold.
- [ ] Spot-check at 30fps that no slam samples mid-entrance as the *only* visible frame.
