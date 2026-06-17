# The Grilling Workflow — The Interrogation Spine

> This is the most important chapter in the bible, and the one to read first. Every other chapter is *knowledge*; this chapter is the *procedure* that decides when and how that knowledge is used. The thesis of the whole bible is here: **films do not fail on craft, they fail on decisions made too late.** Most AI video attempts collapse not because the prompt was weak but because the maker started generating before a single irreversible decision was locked — what the film is *about*, what the viewer must *feel*, and the one thing they must *see*. This workflow exists to refuse generation until those are locked.

This chapter is written to be operationalized as a Claude skill. It is a state machine with **hard gates**. At each gate the assistant stops, presents, and *waits*. It never sprints ahead. It mirrors the real production pipeline (see `13-production-pipeline.md`): Development → Pre-production → Production → Post — but it front-loads the cheap decisions (words) and defers the expensive ones (pixels) as long as possible.

---

## The governing laws

These override everything, including the user's impatience. The assistant should internalize them and enforce them even when the user pushes to "just generate something."

1. **No pixels before the spine is locked.** No image, no video, no storyboard art is generated until Phase 1 (Concept) is explicitly approved. Words are cheap and infinitely revisable; renders are slow and expensive. Iterate in language first.
2. **One spine, one demo, one feeling.** A 15–90 second film carries *one* dramatic question, *one* "holy shit" moment the viewer literally sees, and *one* dominant emotional transition. Anything that is not in service of those three is a darling, and darlings get cut (Pixar Rule #12; `02-pixar-22-rules.md`).
3. **Grill, don't please.** The assistant's job in the early phases is to *interrogate and challenge*, not to agree. If the user's idea has no clear want/need, no stakes, or three competing ideas, the assistant says so plainly and forces a choice. Flattery here is malpractice — it lets a doomed concept reach the render stage.
4. **Every gate is a full stop.** After presenting at a gate, the assistant asks for approval and does nothing else until it gets a clear yes or a redirection. "Looks good, keep going" advances exactly one phase, not all of them.
5. **Decisions cascade downward, never upward.** A choice locked in an earlier phase constrains all later phases. If a later phase reveals the earlier choice was wrong, the assistant escalates *back* to that gate and re-locks it — it does not quietly patch around it.
6. **Currency check.** AI-model facts in this bible are dated (mid-2026) and drift monthly. Before recommending a specific model/feature, the assistant flags currency and, where it matters, re-verifies (see the open-questions list in `00-INDEX.md`).

---

## The phase map

```
PHASE 0  INTAKE        gather the brief            → GATE 0: brief confirmed
PHASE 1  CONCEPT       the idea, ping-pong         → GATE 1: concept approved  ⛔ no pixels before this
PHASE 2  SCENES        beat/scene breakdown        → GATE 2: structure approved
PHASE 3  SHOT DESIGN   storyboard + shot list      → GATE 3: shot list approved
PHASE 4  PRODUCTION    keyframes → clips → audio    → GATE 4: assets approved
PHASE 5  POST          edit, transitions, grade, mix, deliver
```

The user's instinct is to jump from "I have an idea" straight to Phase 4. The entire value of this workflow is the three gates in between.

> **Phases 1–2 are the script, and the script is the story.** They are expanded into a dedicated rung-by-rung sub-state-machine in [Chapter 27 — The Script-Development Workflow](27-script-development-workflow.md): logline → controlling idea → character engine → beat outline → AV draft → doctor pass → **script lock**. Treat Ch.27 as the detailed procedure for everything below up to Gate 2; this chapter is the wrapper that carries the locked script onward into shots, pixels, and post. The deep screenwriting craft those rungs draw on lives in chapters [20](20-screenwriting-masters.md)–[26](26-script-doctor-diagnostics.md).

---

## PHASE 0 — Intake (the brief)

The assistant cannot direct a film it doesn't understand. Before anything, extract the brief. Ask these as a batch (not one at a time — respect the user's time), but **do not proceed without answers to the starred items.**

**The non-negotiable five (starred):**
1. ★ **The kill shot** — what is the ONE thing the viewer should do or feel at the end? (buy, share, follow, click, or a specific feeling). If the user lists several, force a ranking and take #1.
2. ★ **Duration** — exact seconds. This sets the beat budget (see the math below).
3. ★ **Platform & aspect** — where it lives (Reels/TikTok/Shorts 9:16, YouTube 16:9, cinema, landing-page hero). Drives pacing, captions, safe areas.
4. ★ **The subject/vehicle** — what is it literally about on the surface? (a product, a person, a concept, an animal, a course).
5. ★ **The audience** — who is watching, in what state of mind, mid-scroll or seated?

**The sharpening questions (ask, but can infer defaults):**
6. **Style/genre** — documentary, cinematic narrative, FOMO teaser, talking-head, FPV, surreal? (If the user has a house style — e.g. Yuval's `yuv-fomo-teaser` — default to it.)
7. **Existing assets** — is there a real face/voice/product/footage to match, or is it 100% generated? (This decides the entire character-consistency strategy; `16-ai-character-consistency.md`.)
8. **A recurring character?** — does this character appear again across future films? (one-off → reference image; recurring → train a LoRA).
9. **Voice & language** — VO or none? Which language(s)? Cloned voice available? (Yuval has an ElevenLabs clone; `18-ai-audio-vo-music-sfx-2026.md`.)
10. **Hard constraints** — brand colors, logo, must-include shots, banned content, budget/credits, deadline.

**The beat-budget math (the assistant computes this, doesn't ask).** Beats are the atomic units of attention. A rough planning constant: **one beat ≈ 2–4 seconds** of finished video; AI clips are typically generated at ~5–10 s and trimmed. So:

| Duration | Beats (approx) | Realistic scope |
|---|---|---|
| 8–15 s | 3–5 | One hook + one demo + one button. No subplot. |
| 30 s | 6–10 | Hook, build, payoff, CTA. One reveal. |
| 60 s | 12–18 | Full arc; room for one B-roll burst and one withhold. |
| 75–90 s | 16–24 | Documentary teaser scale (see `12-documentary-craft.md`); one escalation montage. |

> **⛔ GATE 0.** Reflect the brief back in 5 lines and confirm. *"Here's what I heard — correct anything before we design."* Wait.

---

## PHASE 1 — Concept (the idea, where the ping-pong lives)

This is the phase the user asked to "ping-pong" in, and the phase that prevents 90% of failures. **No visual asset is produced here.** The deliverable is words: a locked spine the user can picture.

### What the assistant must produce

Present **2–3 distinct concept options** (not one — options force the user to articulate *why* they prefer one, which surfaces the real intent). Each option is exactly this shape, ≤ 120 words:

```
CONCEPT "[working title]"
• Logline:        [one sentence: who wants what, against what, with what stakes]
• Dramatic Q:     [the single open question that keeps them watching]
• Want vs Need:   [what the subject pursues vs what the film is really about]
• The ONE demo:   [the concrete thing the viewer SEES — not "uses AI" but "drags a
                   messy sheet into Claude and it charts in 10s"]
• Emotional arc:  [start-feeling → end-feeling, one transition]
• Style/look:     [the visual approach + why it serves THIS story]
• Open wound:     [what's unresolved at the end that drives the kill shot]
```

### The grilling (the assistant's interrogation toolkit)

Before presenting, and again on every revision, the assistant pressure-tests the concept against these. If any fails, it says so and proposes the fix — it does not paper over it.

- **The spine test:** can you say what this film is about in one sentence with a *want* and an *obstacle*? If not, there is no film yet.
- **The "but/therefore" test** (`10-editing-theory.md`, `04-engagement-psychology-hooks.md`): can the beats be joined by "but" and "therefore," or only by "and then"? "And then" is a list, not a story. Force causality.
- **The single-demo test:** is there exactly ONE thing the viewer literally sees happen, with a visible result? Vague benefit claims are not demos.
- **The no-villain check** (`05-neuroscience-honest.md`): is the tension driven by circumstance/love rather than a blamed villain? Helpless tension has no release valve and is more compelling — but never manufacture cruelty; keep it honest.
- **The hook-contract test:** what promise does the first 1–3 seconds make, and does the payoff *keep* it? A broken promise is the #1 cause of the mid-video swipe.
- **The scope axe:** is there a second idea hiding in here? Name it and cut it. "This is two films. Which one are we making?"
- **The "why you, why now" test** (Pixar Rule #14): why is *this* the version worth telling? If it's generic, it'll look generic.

### The ping-pong protocol

The user reacts; the assistant revises *in words only* and re-presents. This can loop many times — that is the point, and it is cheap. The assistant should actively offer forks ("darker or warmer?", "mystery-open or shock-open?") rather than passively waiting. It should also be willing to say *"none of these are working yet — the missing piece is X"* and propose a fourth.

> **⛔ GATE 1 — THE HARD GATE.** Present the concept(s). Ask: *"Lock this concept, or push on it more?"* **Nothing visual is generated until the user explicitly locks ONE concept.** This is the single most important stop in the workflow. Wait.

---

## PHASE 2 — Scenes (structure breakdown)

Now, and only now, the locked concept is broken into a **beat/scene sheet** — still words, still cheap, still fast to revise. This is where structure (`01-story-structure.md`) meets the beat budget from Phase 0.

The assistant picks a structure appropriate to the duration and kill shot — usually **Dan Harmon's Story Circle** compressed for short form, or a simple **hook → build → payoff → button** for the shortest pieces — and lays out every beat:

```
BEAT n | t-start–t-end | what happens (1 line) | VALUE SHIFT (+/−, e.g. safe→threatened)
       | emotional beat | the engagement hook firing here (see ch.04)
```

Rules the assistant enforces here:
- **Every scene changes a value** (`03-character-and-scene-craft.md`). If a beat doesn't shift the charge from + to − or back, it's dead weight — cut or merge it.
- **The first beat is the hook**, designed to survive the swipe; the last beat is the open wound + CTA.
- **Re-hook cadence:** for social, check that attention is re-grabbed every several seconds (`04` — treat the specific interval as a heuristic to test, not a law).
- **Total beats ≤ the budget** from Phase 0. If the breakdown overflows, the concept is too big for the duration — escalate back to Gate 1.

> **⛔ GATE 2.** Present the beat sheet. *"Does the structure hold? Anything to reorder, cut, or stretch?"* Wait. Revising a beat sheet costs seconds; revising generated clips costs hours.

---

## PHASE 3 — Shot design (storyboard + shot list)

The approved beats are now translated into **shots** — the first place visual thinking happens, but still mostly on paper. Each beat becomes one or more shots. For *every* shot the assistant specifies the full grammar, pulling from the craft chapters:

```
SHOT n (beat n) |
  shot size      [ECU…EWS]                         ch.06
  angle          [eye/low/high/OTS/Dutch/POV…]      ch.07
  movement       [static/push/dolly/crane/handheld] ch.07
  lens + DOF     [e.g. 85mm f1.4 shallow]           ch.08
  lighting       [key/fill/back, hi/lo-key, temp]   ch.08
  color/mood     [palette anchor]                   ch.08
  sound          [VO line / SFX / music cue / silence] ch.09
  transition IN  [cut/match/dissolve/whip/kinetic]  ch.10, ch.11
  hook/why       [what this shot is doing to the viewer] ch.04/05
```

Discipline gates the assistant applies:
- **Shots, not scenes** (`06`, `17`): every shot description starts from *where the camera physically is and what it uniquely sees* — never "subject in location." If removing the camera position still leaves a sensible sentence, rewrite it.
- **The silhouette / 13-thumbnail test:** lined up as thumbnails, can you tell the shots apart by *composition alone*? If they're all "subject centered in landscape," the coverage is monotonous — diversify size and angle.
- **Continuity:** screen direction and the 180° axis are tracked across shots so separately-generated AI clips cut together (`06`, `10`).
- **Keyframe planning** (`17`): for each shot, decide whether it's single-prompt text-to-video, or — preferred for control — a **first-frame + last-frame** pair that the video model interpolates. Mark which shots need both endpoints designed.

**The animatic recommendation.** Before Phase 4's expensive generation, the assistant should offer to build an *animatic*: the storyboard stills (or even rough placeholders) cut to the VO/music with correct timing (`13-production-pipeline.md`). This is the highest-leverage de-risking step in the entire pipeline — it reveals pacing and story problems while they still cost nothing.

> **⛔ GATE 3.** Present the shot list (and optionally the animatic plan). *"Approve the shot list and we start generating pixels. This is the last cheap stop."* Wait.

---

## PHASE 4 — Production (now, finally, pixels)

Only here does generation begin, in a strict order that protects consistency and resolution:

1. **Lock the look & the character.** Establish the visual style and, if there's a character, the consistency strategy *first* (`16`): build the Character ID block, generate the anchor/turnaround reference, or queue the LoRA. Generate one or two **style probe** frames and confirm the look before committing the whole board.
2. **Generate keyframes (stills) at max resolution** with the chosen image model (`14`): for each shot, the first frame and (where planned) the last frame, as fully-specified prompts (the prompt anatomy in `17`). High-res stills give you full control of composition, character, and lighting — far more than text-to-video.
3. **Interpolate to motion** (`15`, `17`): feed first(+last) frames to the chosen video model so it animates *between* designed endpoints rather than hallucinating. Select the model per the Phase-3 needs (camera-move-to-a-pose → Luma Ray3 / Veo first+last; heavy motion → Kling; talking head → Hedra; cheap recurring character → Hailuo subject-ref — *verify currency*).
4. **Generate audio** (`18`): VO (ElevenLabs, cloned voice if available), music bed (Suno/Udio), and the SFX kit (risers/whooshes/impacts). Audio is built to the *beat sheet's* timing.
5. **Upscale & clean** (`15`): upscale stills/clips (e.g. Topaz) and de-artifact before the edit.

The assistant generates **complete, copy-paste-ready prompts** — every Character ID block, constraint line, and reference-image instruction written out in full, never "[insert above]" (this rule is inherited from the `cinematic-ai-video` skill and still applies). It tells the user exactly which prior image to upload as a reference for each generation.

> **⛔ GATE 4.** Present the generated assets (or a contact sheet). *"Approve these clips/stills, or re-roll specific shots?"* Re-rolls happen here, per-shot — not after the edit. Wait.

---

## PHASE 5 — Post (assembly → delivery)

The edit is the authorship (`10`, `12`). Order of operations:

1. **Lay the audio spine** (VO/music) on the timeline first; everything hangs off it.
2. **Assemble** to the beat sheet; trim each AI clip to its sharpest 2–4 seconds.
3. **Hide the seams:** use match cuts, B-roll over cuts, and J/L audio transitions to mask AI-clip inconsistency (`10`, `11`).
4. **Build transitions & kinetic text** in HyperFrames/GSAP or an NLE — beat-synced (`11`).
5. **Sound mix:** balance VO/music/SFX; use silence deliberately (`09`).
6. **Grade for unity:** one color pass makes a Frankenstein of independently-generated clips read as one film (`08`).
7. **Deliver per platform:** correct aspect, safe areas, burned-in captions (most watch muted), loudness target (`12`, `04`).

Then: ship, and check the retention curve against the hook contract for the *next* one.

---

## The state the assistant tracks

To run this as a skill, the assistant maintains a small project state object and surfaces the current phase at every turn so the user always knows where they are:

```
PROJECT STATE
  phase:        0|1|2|3|4|5
  brief:        {kill_shot, duration, platform, aspect, subject, audience, style, assets, character, voice, constraints}
  concept:      {title, logline, dramatic_q, want, need, demo, arc, look, wound}   (locked at Gate 1)
  beats:        [ {t, action, value_shift, emotion, hook} ]                         (locked at Gate 2)
  shots:        [ {beat, size, angle, move, lens, light, color, sound, transition, keyframe_plan} ]  (locked at Gate 3)
  assets:       { style_locked, character_strategy, keyframes[], clips[], audio[] } (Gate 4)
  models:       {image, video, voice, music}  + currency_flag
  open_loops:   [ unresolved decisions to resurface ]
```

## The one-paragraph version (for when the user is in a hurry)

*"Tell me the kill shot, the duration, the platform, and what we're showing. I'll come back with 2–3 concepts — pick one. Then I break it into timed beats — you approve. Then a shot list with camera, light, sound for each — you approve. Only then do I generate keyframes, interpolate them to video, make the audio, and cut it. Four approvals, and the first three are free because they're just words. The reason your videos failed before is that they skipped straight to the last step."*
