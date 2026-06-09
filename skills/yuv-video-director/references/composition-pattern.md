# The multi-engine composition pattern

The canonical `index.html` that combines all engines (this is exactly what shipped as the
"How AI Learns" video — it lints 0/0, validates WCAG AA, renders clean).

## Layer stack (z-index, NOT track-index)
```
z0   #net      — neural-net phoenix field (full duration, canvas, seekable)
z5   #mvid     — Manim render as <video class="clip" muted playsinline>  (body beat)
z10  .scene    — HyperFrames intro/outro clips (transparent bg, .scrim for contrast)
z50  #flash    — neon pink→cyan flash transition on each scene boundary
z60  #fade     — black, fades in only on the final 0.6s
```
The Manim video is opaque, so it covers the field during its window — run the field full-duration
behind everything; it only shows in the intro/outro gaps.

## Skeleton
```html
<div id="root" data-composition-id="main" data-start="0" data-duration="D" data-width="1920" data-height="1080">
  <canvas id="net" width="1920" height="1080"></canvas>
  <div id="intro" class="scene clip" data-start="0"   data-duration="4.5"  data-track-index="1">…+ #pulse Lottie…</div>
  <video id="mvid" class="clip" data-start="4.5" data-duration="27.8" data-track-index="0"
         src="assets/scene.mp4" muted playsinline crossorigin="anonymous"></video>
  <div id="outro" class="scene clip" data-start="32.3" data-duration="5.2" data-track-index="2">…</div>
  <div id="flash"></div><div id="fade"></div>
</div>
```

## Timeline (single GSAP timeline, registered on window.__timelines["main"])
- Field: `tl.to(proxy, {t:D, ease:"none", onUpdate:()=>drawNet(proxy.t)}, 0)` — see [../assets/neural-net-field.js](../assets/neural-net-field.js).
- Lottie: load via lottie-web, push to `window.__hfLottie` (adapter seeks it). See [lottie.md](lottie.md).
- Each scene: `gsap.from()` entrances at the scene's start (offset ~0.2s, vary eases). **No exit
  tweens** — the flash handles the cut. Only the final scene may fade out (`#fade`).
- Transitions: per boundary `b`, `tl.to("#flash",{opacity:0.92,duration:0.22,overwrite:"auto"}, b-0.24)` then back to 0 at `b+0.02`.

## Fonts
`@font-face { font-family:"Anton"; src:url("fonts/Anton-Regular.woff2") }` (latin subset, bundled).
Inter + JetBrains Mono auto-resolve — just name them. No Google Fonts `<link>`.

## Rules carried from the `hyperframes` skill
Standalone root = `data-composition-id` div directly in `<body>` (no `<template>`). Timed elements
need `class="clip"` + `data-start`/`data-duration`/`data-track-index`. Deterministic only. Always
invoke the `hyperframes` skill when authoring; run the [gates.md](gates.md) loop before done.
