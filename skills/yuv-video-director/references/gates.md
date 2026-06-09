# Gates — self-verify & self-heal loop

Run after every authoring change. Fix → re-run until clean. This is what makes the pipeline agentic.

## Per-stage gates
1. **Manim** (before compositing): test-render `-ql` first to catch API errors fast; verify the MP4
   exists + duration matches the beat; spot-check 2 frames. Then `-qh` final.
2. **Lottie**: after wiring, **screenshot a mid-intro frame** and confirm it actually renders shapes
   (the Skottie↔lottie-web trap). Blank → fix the JSON (group-wrap, keyframe `i`/`o` handles).
3. **Composition lint**: `npx hyperframes lint` → **0 errors**. Common fixes:
   - `overlapping_gsap_tweens` → add `overwrite: "auto"`
   - `font_family_without_font_face` → Anton isn't auto-resolved; download the woff2 + add `@font-face`
     (Inter/JetBrains Mono auto-resolve). Use the **latin** subset woff2.
   - remove Google Fonts `<link>` (fails in sandboxed render) — go local for Anton.
4. **Validate**: `npx hyperframes validate` → **0 console errors** (proves Lottie loaded + video
   resolved) + **WCAG AA** on all text. Failing contrast → adjust the failing color within the
   palette (brighten on ink), or add a radial ink `scrim` behind text. Judge badge/decorative warnings.
5. **Render** → spot-check **5 frames** across the timeline (cover, each engine beat, closing). Confirm
   each engine is actually visible (field, Lottie, Manim clip, captions) and nothing overlaps/clips.

## Determinism check (for any live canvas/adapter)
Seeking the same `t` twice must produce the same frame. No `Date.now()`/`Math.random()` (seed a
mulberry32), no `setTimeout`, no `.play()`. The neural-net field is driven by a GSAP proxy
`onUpdate` — that's seekable.

## Don't silently cap
If you drop a beat, shorten the video, or skip an engine (e.g. Manim not installed), say so —
don't present a reduced video as if it were the full ask.
