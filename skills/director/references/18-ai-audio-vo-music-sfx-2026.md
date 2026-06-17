# AI Audio — Voice, Music & SFX (2026)

Picture is only half a film. Walter Murch — the editor and sound designer of *Apocalypse Now* — argued that audiences "see with their ears," that we accept a shaky composite or a dodgy cut if the sound is locked, and reject a flawless image if the audio betrays it. This is not mysticism; it is perceptual. The auditory system has far lower latency than the visual system and is wired straight into the limbic structures that generate emotion and threat-detection. A picture tells you what is there. Sound tells you what it *means* — whether to lean in or brace.

For AI filmmaking this has a brutal practical consequence: the part of your pipeline that most cheaply buys "this feels real" is the audio bed, and it is the part most beginners skip. A Veo clip with no sound design reads as a tech demo. The same clip with a low braam, a designed whoosh on the cut, room tone underneath, and one line of directed VO reads as a trailer. This chapter is the audio half of the pipeline: voice, music, sound effects, and the native-audio video models that increasingly blur the line between "generate picture" and "generate the whole scene."

A structural note before tools. There are now two competing philosophies for getting sound into an AI film. **Native-audio generation** (Veo 3.x) produces lip-synced dialogue, SFX, and ambience *inside* the video model, in one pass. **Post-production assembly** generates each layer separately — VO from a TTS model, music from Suno, SFX from a text-to-SFX model — and mixes them on a timeline. They are not rivals so much as different tools for different shots; most serious work uses both, and the back half of this chapter shows where the seam goes. (For where this sits in the larger build, see `15-ai-video-models-2026.md` and `13-production-pipeline.md`.)

---

## 1. Voice & VO — The Narrator Is the Spine

### Why voice carries more than its words

A trailer narrator, a documentary VO, a character line — each is doing two jobs at once. The *semantic* job is the information in the words. The *paralinguistic* job is everything else: pace, pitch contour, breath, the micro-pause before a key word, the downward terminal inflection that signals authority ("In a world… *where nothing is as it seems*"). Humans read intent almost entirely from the paralinguistic channel; it is why sarcasm survives translation and why a flat read of a great line dies. The whole game in directing AI VO is getting control of that second channel, because early TTS gave you only the first.

The classic **documentary-narrator delivery** — Attenborough, the *Planet Earth* register — is built from specific paralinguistic choices: slow rate (~120–140 wpm vs ~160 conversational), generous pauses that let images breathe, a calm low pitch with small controlled rises on the noun that matters, and almost no vocal fry or upspeak. The classic **trailer voice** (the late Don LaFontaine) is the opposite extreme: slow, but with enormous dynamic range, long held pauses for dread, and a gravelled low register. Knowing *which* register you want is the prerequisite to prompting for it.

### The 2026 voice landscape

ElevenLabs remains the center of gravity for film-grade VO, and its **Eleven v3** model — generally available since March 2026, out of its earlier alpha — is the one that finally exposes the paralinguistic channel to text control. The mechanism is **audio tags**: bracketed instructions inline in the script, e.g. `[whispers]`, `[sighs]`, `[excited]`, `[sarcastic]`, even non-speech events like `[explosion]` or `[clapping]`, and persona shifts like `[French accent]`. Technically these are not post-hoc effects bolted on; v3 treats emotion, intent, and speaker dynamics as first-class tokens during generation, so the tag bends the whole delivery, not just one word. v3 also supports **multi-speaker dialogue** (tags like `[interrupting]` and `[overlapping]` let you script natural banter in one pass) and 70+ languages.

The important honest caveat: v3 trades latency and determinism for expressiveness. ElevenLabs itself recommends **v2.5 Turbo or Flash** for real-time/conversational use, not v3. For pre-rendered film VO you do not care about latency, so v3 is correct — but you *will* re-roll. v3 is more expressive and less predictable; the same script with the same tags gives different takes. Treat it like directing an actor: generate several takes, pick the read, don't expect take-one perfection.

Yuval's own cloned voice lives in this ecosystem. **Instant Voice Cloning** needs ~1 minute of clean audio; **Professional Voice Cloning** wants ~30 minutes and trains a dedicated model for higher fidelity. A cloned voice can drive any v3 read in any supported language — including Hebrew (`heb`) — which is exactly the bilingual EN/HE delivery the FOMO-teaser workflow depends on. Cloning your own voice is also the cleanest answer to the rights question below: you unambiguously own the consent.

| Model / provider | Best for | Notable trait (2026) | Watch-out |
|---|---|---|---|
| **ElevenLabs Eleven v3** | Film VO, character dialogue, trailers | Audio tags + multi-speaker; 70+ langs incl. Hebrew | Non-deterministic; re-roll takes |
| **ElevenLabs Flash / v2.5 Turbo** | Real-time, agents, bulk | ~75 ms TTFA, cheaper | Less expressive than v3 |
| **Cartesia Sonic** | Lowest latency, voice agents | ~40 ms time-to-first-audio | Tuned for conversation, not cinematic range |
| **OpenAI gpt-4o-mini-tts** | Quick utility VO, cheap | Steerable "speak like X" prompt; ~$0.015/min | Smaller voice library, less control depth |
| **PlayHT / PlayAI** | (legacy) long-form conversational | Acquired by Meta July 2025, **being wound down** | Do not build new pipelines on it |
| **Hume Octave** | Emotionally-aware reads | Infers emotion from context | Niche; smaller ecosystem |

### Directing the read: the control surface

Three levers, in order of power:

1. **Punctuation and line-breaking.** This is the most underused control. Ellipses force pauses. A period where a comma "should" be forces a full stop and resets the breath. Short lines on their own slow the read. Em-dashes create the trailer-voice mid-sentence cliff. Before you reach for any tag, *re-punctuate the script for rhythm* — write it the way you want it spoken, not the way grammar wants it written.
2. **Audio tags (v3).** `[slowly]`, `[whispers]`, `[serious]`, `[building intensity]` for the documentary/trailer registers; emotion tags for character work. Tags compound — `[whispers][nervous]` is a different read from either alone.
3. **Voice settings.** Stability (lower = more expressive and variable, higher = more consistent and flatter), similarity, and style exaggeration. For a steady documentary narrator, raise stability; for a volatile character, drop it.

A word on **SSML** (Speech Synthesis Markup Language — the XML standard with `<break>`, `<prosody>`, `<emphasis>` tags that traditional TTS engines like Google and Amazon use). ElevenLabs' newer models lean on natural-language audio tags rather than full SSML; only a limited subset of SSML (notably `<break>` for precise pauses) is honored. If you come from a Polly/Google background, do not assume your `<prosody rate>` will work — port your intent to v3 tags and punctuation instead.

> **→ AI APPLICATION.** For a 75-second teaser narrator: write the script in ElevenLabs Studio (the unified ElevenCreative Studio — the older Voiceover Studio sunsets May 15, 2026). Use the cloned voice. Set stability high-ish for control. Re-punctuate for rhythm first, then add v3 tags: open with `[slowly][serious]` on the hook, push `[building intensity]` into the mid-section, and drop to `[whispers]` on the final dare-line before the title card. Generate 3–4 takes per beat, audition, keep the best. Export with **word-level timestamps** — you will need them to snap captions and to time the cut (Section 5).

---

## 2. Music — The Emotional Carrier Wave

### Why score works (and the honest version of the science)

Music does to time what a bassline does to a room: it imposes a pulse and a forward expectation. The mechanism people invoke is the "dopamine hit" of musical anticipation — Salimpoor's 2011 study did show dopamine release at moments of peak musical pleasure, including in *anticipation* of the peak. But the popular telling ("music hacks your brain's reward system") is overstated. The robust, replicable finding is narrower and more useful to a filmmaker: **expectation and its resolution drive emotional response**. A build that withholds the downbeat, then lands it on your cut, *feels* like payoff because the brain was leaning forward. You do not need the neuro-myth. You need to control tension and release, and put the release on the edit.

The two practical jobs of score in a short film are **continuity** (a music bed glues a montage of disparate AI clips into one scene — without it, every cut feels like a new tab opening) and **arc** (the dynamics of the music are the dynamics of the emotion; a swell tells the audience *now*).

### Suno vs Udio vs ElevenLabs Music (2026)

| | Suno (v5.x) | Udio | ElevenLabs Music v2 |
|---|---|---|---|
| Strength | Fast, structured, huge community, best stems | Often cleaner audio fidelity / mixes | Trained on **licensed** data; commercial-cleared |
| Stems | Up to **12 stems** (vocals/drums/bass/etc.), Advanced Stem Separation (June 2026 v5.5) | Stem export available | MP3 export; no documented stem export |
| Structure control | Section tags, personas | Section control | Section-by-section composition (intro/verse/chorus), regen one section |
| Length | full songs | full songs | 3 s – 5 min, instrumental or vocal |
| Commercial rights | Paid tiers grant commercial use (Pro/Premier) | Paid tiers; licensing improving post-UMG/Warner deals | Broad commercial use under subscription, licensed training |

For **instrumental beds for a teaser** — which is what you almost always want, because lyrics fight VO — the move is: prompt for instrumental-only, name the genre and tempo, name the *function* ("cinematic trailer underscore, tense, rising"), and use structure control so you get a build that lands where your cut lands. Suno/Udio let you tag sections; ElevenLabs Music's section-by-section composition lets you build an intro/swell/drop independently and regenerate just the swell if its timing is off.

### Matching tempo to the cut

This is the single most amateur-vs-pro tell in AI montages. Cut rhythm and music tempo must agree. The math: at **120 BPM**, one beat = 0.5 s, one bar (4 beats) = 2 s. If your fast-cut section runs shots of ~1 s each, you want cuts on the half-beat or beat of a ~120 BPM bed and the dramatic cut on the downbeat of a bar. Decide tempo first (it dictates how fast your montage can legitimately move), or extract the bed's BPM and cut to it. Generate at a specific BPM where the tool allows; otherwise generate, detect BPM, and place your cuts on the grid. The braam/swell in the music should coincide frame-accurately with the title-card slam.

### The licensing reality — read this before you ship

This is currency-critical and genuinely unsettled. Two things to separate: **(a) do you have rights to the output**, and **(b) is the output legally clean**.

- **(a) Your license to use it.** Suno and Udio grant commercial-use rights on paid tiers; ElevenLabs Music grants broad commercial use under subscription. Free tiers typically do **not** grant clean commercial rights — do not ship a client/brand video off a free-tier Suno track.
- **(b) The training-data cloud.** The RIAA sued Suno and Udio (mid-2024) for training on copyrighted recordings. As of mid-2026: **UMG settled with Udio (Oct 2025)** establishing a per-generation royalty template (~$0.002–0.005/generation); **Warner settled with Suno (Nov 2025)** with a licensing partnership; **Sony has settled with neither**, and a pivotal fair-use summary-judgment hearing in Suno's case is scheduled for **July 2026**. Independent-artist class actions (Oct 2025) are early-stage. The practical read: the platform's *grant to you* is generally indemnified per their terms, but the underlying legality is being decided in court right now.
- **Copyrightability of the output itself.** Separately, the US Copyright Office position is that purely AI-generated output without sufficient human authorship is **not copyrightable** — meaning you may have a license to *use* your track but no exclusive *ownership* to stop others copying it.

**The de-risking move for high-stakes work:** prefer **ElevenLabs Music** (licensed training data, commercial-cleared) over Suno/Udio when the video is for a brand or paid client, accept that you may not own the output exclusively, keep your subscription receipts, and read the current Music Terms each time — these facts change monthly.

> **→ AI APPLICATION.** For the 75 s teaser bed: in ElevenLabs Music (for license safety) or Suno (for stems + community presets), prompt *"cinematic trailer underscore, instrumental, 120 BPM, tense low strings and a sub-pulse, slow build to a hit at ~0:55, then ringing decay."* Generate, audition, and if the build's timing is off, regenerate just that section (ElevenLabs) or re-roll with an explicit structure tag (Suno). Export stems if available so you can duck the music under VO automatically in the mix. Note the BPM and lock your cut grid to it.

---

## 3. SFX — The Layer Nobody Notices and Everybody Feels

Sound effects are where "real" is manufactured. A footstep, a cloth rustle, room tone, a distant traffic hum — these are **foley** and **ambience**, and their absence is what makes silent AI clips feel dead. Separately, the **trailer SFX kit** is a small, learnable vocabulary of designed sounds that do most of the dramatic lifting in modern teasers.

### The trailer kit, defined

| Element | What it is | Where it goes |
|---|---|---|
| **Riser** | A pitch/volume ramp that builds tension | Under a build, ending exactly at a cut/reveal |
| **Impact / Hit** | A short percussive slam | On the title-card frame, on a hard cut |
| **Whoosh** | Fast filtered noise sweep | On fast camera moves and transitions, sells motion |
| **Braam** | The deep brass/synth "BWAAAH" (the *Inception* sound) | The big dramatic stab; use sparingly or it's parody |
| **Sub-drop / Boom** | Low-frequency hit you feel more than hear | The deepest beat, often under a logo reveal |
| **Reverse / Pre-verb** | A sound swelling *backwards* into a hit | The half-second before an impact, creates inhale |
| **Room tone / ambience** | Continuous quiet bed | Under everything, so silence isn't dead air |

The craft principle: **transitions are sold by sound, not picture.** A whoosh on a cut makes the cut feel intentional and kinetic; the same cut dry feels like an error. A riser plus impact turns an ordinary reveal into a *reveal*. And the unsexy one — **room tone under every shot** — is what stops the audience's ear from noticing the joins between AI clips that were never in the same "room."

### Text-to-SFX in 2026

**ElevenLabs Sound Effects** generates high-fidelity SFX from text ("rain on a tin roof," "cinematic sci-fi explosion," "futuristic hovercraft engine idling in rain"). Best results come from descriptions roughly 10–60 words; it returns several candidates to audition, and you can upscale the keeper or re-roll. It is integrated into ElevenCreative Studio as a dedicated SFX track type, so you can place a generated effect directly on the timeline at a chosen moment. This is the fastest path to a bespoke effect that no stock library has.

The honest limit: generated SFX is excellent for *designed* sounds (risers, whooshes, abstract impacts, ambiences) and weaker for *tightly-synced foley* (each footstep landing on the exact frame). For frame-locked foley you either hand-place individual hits or — increasingly — let the native-audio video model generate them (Section 4).

> **→ AI APPLICATION.** Build a reusable **trailer SFX kit** once: generate a riser, two whooshes (one bright, one dark), an impact, a braam, a sub-drop, and a 60 s ambient room-tone bed in ElevenLabs Sound Effects, and save them. For the teaser, place a whoosh on every hard transition, a riser into the mid-build, the braam + sub-drop on the title slam (layer them — braam for body, sub-drop for the felt low end), and run room tone under the whole piece at low level so no cut lands in dead silence.

---

## 4. Native-Audio Video Models — When the Model Makes the Sound

**Veo 3 / Veo 3.1** (Google DeepMind; Veo 3.1 released Oct 14, 2025) is the first mainstream video model to natively generate **synchronized** audio — dialogue lip-synced to the character, SFX matched to on-screen action, and ambient soundscapes — in a single pass, at 24 fps with 48 kHz stereo audio, up to 4K. Architecturally it processes visual spacetime patches and temporal audio together, which is why footsteps actually land on the footfall and dialogue tracks the lips. As of mid-2026 it is essentially unique among major models in doing synced dialogue.

How to prompt for it: describe the sound *in the same prompt as the picture*. "A woman explains animatedly to camera" yields synced speech; naming "rain hammering the window, distant thunder" yields the ambience; describing the action yields matched SFX. Some pipelines quote spoken lines directly in the prompt to control dialogue content.

### The decision: native audio vs add-in-post

This is the seam of the whole chapter. Use **native audio** when:
- You need **lip-synced dialogue** and the character is AI-generated (no other tool syncs as cleanly in one pass).
- You want **physically-matched foley** (footsteps, impacts tied to motion) — the model knows the motion, so it nails sync that text-to-SFX can't.
- You want a fast one-shot for a single self-contained beat.

Add audio **in post** when:
- You need **continuity across many clips** — a single music bed and consistent ambience over a montage. Native audio is per-clip; eight Veo clips give you eight unrelated ambiences. Post-mix gives you one coherent soundscape.
- You need **a specific voice** (e.g. a cloned voice, or a directed trailer narrator) — native dialogue uses the model's voice, not yours.
- You need **frame-accurate music-to-cut** sync and a designed trailer SFX kit — native audio won't give you a braam on your title slam.
- You need **fine mix control** (ducking, EQ, levels) — native audio is baked in, hard to separate.

The mature workflow is hybrid: let Veo generate the *diegetic* layer (the sound that exists in the scene — dialogue, foley, ambience) per clip, then in post add the *non-diegetic* layer (score, trailer SFX, the cloned-voice narrator) that has to be coherent across the whole film. A common gotcha: if you're adding your own music and VO, you often want to **mute or de-emphasize** Veo's generated ambience so it doesn't clash with your bed — generate with sparse audio prompts when you know you'll re-score.

> **→ AI APPLICATION.** For a teaser beat that needs a character speaking one line to camera, generate it in Veo 3.1 and let it sync the line — then in post you still lay your music bed, your whooshes on the surrounding cuts, and your narrator over the *other* beats. For pure-montage beats with no on-screen speech, generate Veo clips with minimal/ambient audio prompts and build the entire soundscape in post for continuity.

---

## 5. Lip-Sync & Talking Heads — Avatars vs Generated Characters

When the job is **a specific person delivering a script** — a brand spokesperson, a presenter, a known face — you reach for a talking-head/avatar tool rather than a generative video model.

- **HeyGen** is the avatar workhorse. **Avatar IV** (Aug 2025) drives full-body motion, micro-expressions, natural head movement, and gestures that track the script's emotional tone from a single image + audio. It also does video translation into 172+ languages with re-synced lip movement and audio dubbing — the clean path to a Hebrew/English version of the *same* on-camera delivery. Pricing (2026): Creator ~$29/mo, Pro from ~$49/mo, Business ~$149/mo; Avatar IV ~20 credits/min, translation ~5 credits/min, dubbing ~2 credits/min.
- **Hedra** specializes in animating *any* image — including stylized/non-photoreal characters — into a talking character with synced lips and expression, across 15+ languages. Free tier is genuinely usable; Creator ~$10/mo. Reach for Hedra when your "talking head" is an illustrated or stylized character rather than a realistic human.

### The decision: avatar vs generated character

Use an **avatar tool (HeyGen/Hedra)** when you need a *consistent, controllable, identifiable* face saying *exact* words, when you need the same delivery in many languages (translation/dubbing), or when the face must match a real person/brand. Use a **generated character (Veo etc.)** when the shot is cinematic and the character doesn't need to be a fixed identity — when you want camera movement, environment, and a *cinematic* look more than a clean talking-head. Avatars give you control and identity; generative gives you cinema. (For consistency-of-identity across shots, see `16-ai-character-consistency.md`.)

Standalone **lip-sync tools** (which re-sync an existing video's mouth to new audio) are the bridge case: use them to dub footage you already have, or to fix a line, without regenerating the whole shot.

> **→ AI APPLICATION.** For a teaser's "spokesperson" beat in two languages, drive a HeyGen Avatar IV with the cloned-voice VO for EN, then use HeyGen's translation/dubbing to produce the HE version with re-synced lips — one delivery, two languages, matching the bilingual EN/HE deliverable. For a stylized character, route the same audio through Hedra instead.

---

## 6. Putting It Together — The Full 75 s Teaser Audio Bed, and HyperFrames

Here is the end-to-end audio assembly for the 75-second teaser, in order.

1. **Decide tempo first.** Pick the music BPM (say 120) before you cut — it sets your maximum honest cut speed (Section 2). Lock a cut grid: bar = 2 s, beat = 0.5 s.
2. **Generate the music bed.** Instrumental, the right register, with a build landing a hit at ~0:55 and decay after. ElevenLabs Music for license safety on brand work; Suno if you want stems. Export stems if you can.
3. **Generate and direct the VO.** ElevenLabs v3 with the cloned voice, re-punctuated for rhythm, tagged for register (Section 1). Export **word-level timestamps** — these are the spine for caption sync and for timing the cut.
4. **Build the SFX kit and place it.** Whoosh on every hard cut, riser into the build, braam + sub-drop on the title slam, room tone under everything (Section 3).
5. **Generate native-audio beats where needed.** Any on-screen speaking shot → Veo 3.1 for lip-sync; keep its ambience sparse if you're re-scoring (Section 4). Talking-head spokesperson → HeyGen/Hedra (Section 5).
6. **Mix.** Duck music under VO (sidechain or manual −6 to −10 dB while the narrator speaks), keep SFX peaking above the bed at the hits, ride room tone at the bottom. The braam and sub-drop own the title moment; everything else makes room for it.
7. **Sync to the cut.** Place visual cuts on the beat grid; land the braam/title-slam on a downbeat; align the VO's key word to a visual beat.

### How this plugs into HyperFrames

HyperFrames renders deterministic MP4 from HTML/CSS/seekable animations, and its audio model fits this bed directly. You attach audio with `<audio>` elements and data-attributes for timing/tracks; the pipeline mixes them into the final render. The integration specifics that matter:

- **VO + captions:** HyperFrames' workflow generates ElevenLabs VO and gets **word-level timestamps** back, then snaps "karaoke" active-word captions to them — the same timestamps you exported in step 3 drive caption sync automatically. This is why exporting timestamps from v3 isn't optional.
- **Music + SFX tracks:** add them as audio elements with timing data; layer the bed, the whooshes-on-cuts, the braam-on-title.
- **Audio-reactive visuals:** HyperFrames can pre-extract audio bands (bass/mid/treble) and sample them per-frame in the timeline loop — map bass to a scale-pulse on the logo, treble to glow on the title — so the *picture* reacts to the very bed you built, tightening the felt sync between sound and image.
- **Determinism:** because the render is frame-accurate, once your braam is on the right frame it stays there across re-renders — the opposite of the per-clip variability you fight in generative models.

This is precisely the chain the `yuv-fomo-teaser` workflow assembles: cloned-voice EN/HE VO + cinematic music bed + a designed SFX kit, mixed in HyperFrames, output 4-up (EN/HE × 16:9/9:16). The craft in this chapter is what makes that chain produce a trailer instead of a tech demo. (For the editing-side timing theory, see `10-editing-theory.md`; for the visual generation half, `15-ai-video-models-2026.md`.)

---

## Sources

- ElevenLabs — Eleven v3 (audio tags, GA, multi-speaker): https://elevenlabs.io/v3 · https://elevenlabs.io/blog/v3-audiotags · https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices
- ElevenLabs — Music v2 (commercial, structure, instrumental): https://elevenlabs.io/docs/eleven-creative/products/music · https://theaiinsider.tech/2026/05/29/elevenlabs-launches-music-v2-with-mid-track-genre-switching-and-commercial-clearance/
- ElevenLabs — Sound Effects & Studio: https://elevenlabs.io/sound-effects · https://elevenlabs.io/docs/eleven-creative/products/studio
- TTS landscape (Cartesia, OpenAI, PlayAI wind-down): https://sureprompts.com/blog/voice-generation-models-compared-2026 · https://www.cartesia.ai/sonic/ · https://gradium.ai/content/tts-latency-benchmark-2026
- Suno v5 stems & commercial rights: https://discover.oreateai.com/discover/suno-ai-music-v5-stems-and-persona-control-actually-work-now · https://dynamoi.com/learn/ai-music-distribution/suno-commercial-rights-explained
- AI-music litigation status (RIAA, UMG/Udio, Warner/Suno, Sony): https://www.chartlex.com/blog/business/music-industry-ai-lawsuits-tracker-2026 · https://musically.com/2025/10/30/umg-settles-udio-lawsuit-companies-plan-new-ai-music-service-together/ · https://www.aivortex.io/legal/ai-case-law/suno-udio-music-ai/
- Veo 3 / 3.1 native audio: https://deepmind.google/models/veo/ · https://www.veo3ai.io/blog/veo-3-native-audio-prompt-guide-2026 · https://ai.google.dev/gemini-api/docs/video
- HeyGen & Hedra (avatars, pricing, lip-sync): https://www.heygen.com/pricing · https://lipsync.com/compare/heygen-vs-hedra · https://www.buildfastwithai.com/ai-tools/hedra
- HyperFrames audio workflow: https://github.com/heygen-com/hyperframes · https://www.mindstudio.ai/blog/ai-video-generation-workflow-hyperframes-elevenlabs
