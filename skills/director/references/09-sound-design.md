# Sound Design — The Half of Film You Cannot See

Walter Murch — the man who edited and mixed *Apocalypse Now*, *The Conversation*, and *The Godfather Part II*, and who coined the job title "sound designer" — has a deceptively simple way of putting it: the eye looks; the ear listens. Vision evolved to answer *where* and *what*; hearing evolved to answer *when* and *is something coming for me*. The auditory system is the body's threat-detection radar — it runs in the dark, behind your head, while you sleep. That is why sound bypasses the deliberate, skeptical front of the brain and goes straight to the limbic, emotional core. You can choose to close your eyes during a horror film. You cannot close your ears, and the filmmakers know it.

So when editors and mixers repeat "sound is 50% of the experience," they are not being poetic about their own craft. There is a real perceptual asymmetry: **bad picture with good sound reads as a stylistic choice; good picture with bad sound reads as broken.** Test it on yourself — a slightly soft, grainy image with crisp, full audio feels like a vibe (think early *Blair Witch*). A pristine 4K image with hollow, tinny, room-echo audio feels like an amateur YouTube upload you click away from in two seconds. The audience's tolerance for visual imperfection is enormous and their tolerance for audio imperfection is near zero, because sub-par audio triggers the ancient "this signal is wrong / unsafe" alarm.

This chapter is the foundation beneath every other "make it feel cinematic" trick. For AI filmmaking specifically, it is the single biggest free win available right now — because most AI video is mute or carries thin, generic native audio, and a properly built sound stack is what separates a tech demo from a film.

> **The honest-science caveat up front.** You will read claims online that "sound is processed faster than vision" or "audio is 80% of emotion." The defensible facts are narrower: auditory reaction times *are* shorter than visual ones (roughly 140–160 ms vs 180–200 ms for simple stimuli — the cochlea transduces faster than the retina), and audio drives a large, measurable share of perceived production value and emotional response. But there is no rigorous study that produces a clean "50%" or "80%." Treat those numbers as craft heuristics that point at a true phenomenon, not as measured constants. The *phenomenon* — that sound disproportionately governs immersion and emotion — is real and robust.

## Diegetic vs non-diegetic: whose ears are these?

The first and most important distinction in all of sound is *where the sound lives*.

- **Diegetic sound** exists inside the story world. The characters could, in principle, hear it: dialogue, footsteps, a car engine, a radio playing in the scene, gunfire. The *diegesis* is the fictional world of the film; diegetic sound belongs to it.
- **Non-diegetic sound** exists only for the audience. The characters cannot hear it: the orchestral score, a voice-over narrator, the ominous low drone under a tense shot. It is the film *commenting* on its own world.

Why does this matter beyond vocabulary? Because the line between them is an emotional control surface. Moving a sound across it changes meaning. The most powerful version is the **trans-diegetic** sound (also called a "sound bridge of source" or the diegetic/non-diegetic gag): a sound that starts on one side and crosses to the other, usually for wit or shock.

The classic gag: in *Blazing Saddles*, Bart rides across the prairie to swelling orchestral music — then literally rides *past the Count Basie Orchestra* playing in the desert. The score we assumed was non-diegetic turns out to be diegetic. Mel Brooks weaponizes the convention. The serious version: in *The Truman Show*, the "score" is being played live by a composer at a piano in the control room — it is non-diegetic to Truman but diegetic to the show's producers, which is the whole theme of the film made audible. A subtler everyday use: a song begins as score over a montage, then we cut to a character turning down the car radio playing that same song — the music "lands" in the world and pulls us from reflection into scene.

> **→ AI APPLICATION.** Native-audio video models (Veo 3, see below) generate *diegetic* sound joined to the picture — footsteps, dialogue, room tone — because they're trained on real footage where sound is bonded to image. They are bad at *non-diegetic* score, because score has no on-screen source to learn from. So treat the layers differently in your pipeline: let the video model (or your foley/SFX pass) own diegetic sound, and add score and VO as separate non-diegetic tracks in the edit. When you *want* the trans-diegetic gag, you must build it by hand — generate the music as a clean stem, place it over the cut, then EQ-filter it to "telephone/tinny" the instant the camera reveals the radio playing it (a high-pass + low-pass band-limit, see the mix section). The model will not invent that move for you.

## The layers of a mix: what's actually in the soundtrack

A finished film soundtrack is not one recording. It is dozens to hundreds of separate tracks, grouped into five **stems** (a stem is a submix of one category, kept separate so it can be balanced independently and re-versioned — e.g. an "M&E" stem, music-and-effects with dialogue removed, is what lets a film be dubbed into other languages). The five families:

| Layer | What it is | Why it exists |
|---|---|---|
| **Dialogue** | Spoken lines — production sound from set, plus ADR | Carries plot and character; the spine the whole mix protects |
| **Foley** | Human-performed everyday sounds: footsteps, cloth rustle, prop handling, door knobs | Re-creates the small sounds the boom mic missed or that need to feel *right* |
| **Hard SFX** | Designed/"sync" effects: gunshots, explosions, car bys, sci-fi weapons, the "braam" | Spectacle, impact, the unreal made physical |
| **Ambience / room tone / atmos** | The continuous bed of a space: wind, traffic hum, refrigerator buzz, crowd murmur | Sells the *location* and prevents "dead air" that feels broken |
| **Music / score** | Non-diegetic emotional underscore, plus source music | Tells the audience how to feel and binds scenes into emotional arcs |

### Foley: why the most realistic sounds are fake

**Foley** (named for Jack Foley, a Universal sound man from the 1930s) is the art of re-performing everyday sounds in sync to picture, in a studio, by an artist watching the scene on a loop. Footsteps, clothing movement ("cloth pass"), keys, a sword being drawn, a punch.

Here is the counterintuitive truth that beginners resist: **you almost always re-record these even when the original was captured on set.** Three reasons. First, the boom mic on set is positioned to capture *dialogue*, so the incidental sounds it picks up are off-axis, distant, and inconsistent. Second, control — the director may want footsteps *heavier* on the villain to telegraph menace, which reality won't provide. Third, the M&E requirement: for international dubbing you must be able to delete the entire dialogue stem and still have a complete soundtrack, which means every non-dialogue sound has to live somewhere *other* than the dialogue track.

And foley is theatrical, not literal. The famous examples are folklore precisely because they work: snapping celery for breaking bones, a leather glove flapped for bird wings, coconut halves for hooves, cornstarch in a leather pouch squeezed for crunching snow. The ear does not want the *physically accurate* sound; it wants the *emotionally legible* one. A real punch is a dull, disappointing thud; the cinema punch is a layered crack-and-whump that says "that hurt." This is the single most important mental shift in sound design: **you are not reproducing reality, you are composing a more-legible-than-real impression of it.**

> **→ AI APPLICATION.** This is where text-to-SFX tools shine, because you're describing an *impression*, not transcribing reality. ElevenLabs' sound-effects model (`eleven_text_to_sound_v2`, available from the $5/mo Starter tier, generations of 0.5–30 s, with a loopable flag) takes natural-language and audio-terminology prompts: "single heavy male footstep on wet concrete, close mic, slight reverb tail" or "wet visceral bone-crunch impact, layered, cinematic, no music." Generate 3–4 variations per cue and pick. For a foley pass on an AI clip: list each on-screen action (every footfall, every cloth movement, every prop touch), generate a cue for each, and place them in sync — exactly as a human foley artist works through a scene. Layer two or three generated cues for a single impact (a "crack" + a "body whump" + a low "sub thud") to get the more-legible-than-real punch. Do **not** rely on a native-audio video model for hero foley; its footsteps are generic and not art-directable.

### Ambience and room tone: the silence that isn't silent

**Room tone** is the sound of a "silent" room — the specific hum, hiss, and air of a space. Every location has one and it is never true silence. **Ambience** (or **atmos**, after Dolby Atmos but used loosely) is the broader environmental bed: the city outside the window, the forest at dusk, the office air-handling.

Why it's non-negotiable: a hard cut to *digital* silence (an absolute zero waveform) is perceived as a dropout, a glitch, a broken file — the brain's "signal lost" alarm again. Editors lay a continuous room-tone bed *under* dialogue so that the gaps *between* lines don't fall into that uncanny void. The bed also smooths edits: when you cut between two takes recorded minutes apart, their background hiss differs, and a unifying ambience track hides the seam. Ambience is also your cheapest tool for *scale and place* — the same shot of a person at a desk becomes "lonely night office" or "frantic newsroom" purely by the bed you choose.

> **→ AI APPLICATION.** Generate a long ambience bed (ElevenLabs SFX supports up to 30 s; loop it or generate several and crossfade) for each location in your film and run it *continuously* under every shot in that location — including under dialogue and under the silences. This one move does more for "is this real footage?" than any visual tweak. Native-audio models give you *per-clip* ambience that resets at every cut and changes character shot-to-shot — audibly wrong. Strip or duck the model's ambience and lay your own continuous bed across the whole scene.

## Score: the most direct line to the heart

Music is the only film element that the audience knows is artificial and yet surrenders to completely. It is non-diegetic by default, and it tells them what to feel before they consciously know they feel it.

### Tempo, key, instrumentation — the levers

There is real, if rough, mapping between musical parameters and felt emotion, and it's mostly learned-cultural plus some cross-cultural cores:

| Lever | Tends toward | Tends toward |
|---|---|---|
| **Tempo** | Fast → urgency, excitement, anxiety | Slow → grief, calm, grandeur |
| **Mode/key** | Major → resolved, bright, safe | Minor → sad, tense, unresolved (this is largely Western-cultural, not universal) |
| **Instrumentation** | Strings → emotion/warmth; brass → heroism/threat; low synth/cello → dread | Solo piano/woodwind → intimacy, fragility |
| **Dissonance** | Consonant → comfort | Dissonant/atonal → unease, horror (*Jaws*' two-note motif, *There Will Be Blood*' string clusters) |
| **Register** | Low → power, dread, mass | High → tension, fragility, the uncanny |

Be honest about the limits: the major=happy / minor=sad mapping is strongly Western-learned, not a hardwired human constant — many musical traditions don't share it. Don't over-claim neuroscience. What *is* robust is that **expectation and its violation** drive musical emotion: a score sets up a pattern and the payoff (or denial) of that pattern is where the feeling lives.

### Leitmotif: Wagner to Williams

A **leitmotif** ("leading motif") is a short musical idea bound to a character, place, or concept, which recurs and *transforms* as that thing changes. Wagner built the *Ring* cycle on it in the 1800s; Richard Strauss and the late-Romantics carried it; and John Williams made it the lingua franca of modern Hollywood. The Imperial March *is* Darth Vader; the five-note phrase is Force/destiny; the *Jaws* motif is the shark even when the shark is off-screen — which is the point, the music makes the unseen threat present. The power is in the *transformation*: Vader's theme played tenderly on a solo instrument at his redemption inverts the meaning without changing the notes. A motif you state once is a label; a motif you develop is storytelling.

### Scoring to picture, and the temp-track trap

**Scoring to picture** means the composer writes against the locked edit, hitting specific frames — a sting on a reveal, a swell at the kiss, a downbeat on the cut. The **temp track** (temporary music, usually borrowed from other films) is laid in during editing so everyone can feel the intended emotion before the real score exists. Its danger is **"temp love"**: directors fall for the temp and ask the composer to clone it, producing derivative scores and occasional lawsuits. The honest version of the lesson: temp tracks are great for finding the *function* you need (a "rising hope" cue, a "dread" cue) and dangerous when they dictate the *specific notes*.

> **→ AI APPLICATION.** AI music in 2026 is genuinely usable for score, with a sharp limitation: it cannot reliably hit a frame. **Suno** (v5.5 as of March 2026 — voice cloning, custom model fine-tuning, Suno Studio DAW, stem separation, 44.1 kHz, songs up to ~8 min) is the all-round pick; **Udio** (v1.5 lineage, 48 kHz stereo, and crucially **inpainting** — select a ~2 s segment and regenerate just that region) is the audiophile/granular pick. Workflow: prompt by *function and instrumentation*, not by referencing copyrighted tracks ("slow-building minor-key cello and low synth dread bed, sparse, no drums, cinematic, 80 bpm"), generate several, then **edit the music to the picture** rather than expecting the model to score to it — cut the music's natural swell to land on your edit, or use Udio's inpainting to extend/alter a region so a hit falls on the right frame. Use Suno's stem separation to get a music-only stem you can duck under dialogue. For leitmotif: generate one strong theme, then re-prompt for slow/sparse/major and dark/dissonant *variations of the same melody* — you author the transformation, the model renders the textures. Treat anything online as a **temp track**: find the function, don't worship the notes. See `18-ai-audio-vo-music-sfx-2026.md` for current model/pricing detail.

## The power of silence and the dropout

Silence is the loudest tool in the kit, *because* it violates the expected continuous bed. The mechanism is contrast: after a dense, loud passage, cutting the soundtrack to near-nothing makes the audience lean in — the ear, deprived of input, strains. Spielberg drops nearly all sound at the D-Day landing's worst moment in *Saving Private Ryan* (the muffled, ringing POV after the blast) to put us inside concussion and shock. *No Country for Old Men* famously has **no score at all** — the tension lives in footsteps, wind, and the absence of music telling you it's okay. *A Quiet Place* makes silence the literal premise.

The craft nuance: pure *digital* silence reads as a glitch (the dropout problem above). So "silence" in film is usually a *near*-silence — a held tone, a high ringing, a single sustained note, or a very quiet room tone — not an absolute zero. The dramatic dropout works because it's surrounded by sound; silence has no power in a film that's quiet throughout.

> **→ AI APPLICATION.** This is a pure *editorial* move, and you own it entirely — no model decides it. In your edit, identify the peak moment and cut every stem (or all but one sustained sub-bass tone) for 1–3 seconds, then slam back in. For social/teaser cuts, a beat of silence right before the hook reveal is one of the strongest retention tools you have. Never use absolute silence; lay a whisper of room tone or a held low tone underneath so it reads as *chosen*, not *broken*.

## The sound bridge: how audio smooths the cut

A **sound bridge** is when audio from one shot overlaps the picture of another — the sound either *leads* (we hear the next scene before we see it) or *lags* (the previous scene's sound continues over the new image). It is one of the most important editing tools and it lives at the seam between this chapter and `10-editing-theory.md` and `11-transitions.md`.

- **Audio leads (J-cut)**: we hear the next scene's dialogue/ambience while still seeing the current shot, then the picture catches up. Pulls us forward, creates anticipation, makes the cut feel inevitable rather than abrupt. Named for the rough "J" shape the audio and video clips make on a timeline.
- **Audio lags (L-cut)**: the picture cuts but the previous scene's sound hangs over the new shot. Used constantly in dialogue editing so we cut to the *listener's* reaction while the *speaker* is still talking — this is how editors keep conversations feeling alive instead of ping-ponging head to head.

Why it works perceptually: a straight cut where both picture and sound change *at the same frame* is a hard, noticeable seam (a "butt cut"). Staggering the sound and picture transitions means the brain only registers one change at a time, so the edit slides by under awareness. Almost every "invisible" edit in a polished film is a J- or L-cut.

> **→ AI APPLICATION.** Since you assemble AI clips in a normal NLE (non-linear editor) timeline, J- and L-cuts cost nothing and instantly upgrade choppy AI sequences. Default to staggering your audio: let a clip's ambience or a line of VO start a few frames before its picture, or extend the outgoing clip's sound a beat past the cut. For dialogue scenes built from separate AI shots, L-cut to reaction shots while the line continues. This single habit hides the "stitched-together clips" feeling more than any visual transition. See `11-transitions.md`.

## Dialogue, ADR, and the three-way balance

**Dialogue** is the protected element — the mix is built so that, whatever else happens, the words stay intelligible. **ADR** (Automated Dialogue Replacement, also "looping") is re-recording dialogue in a studio in sync to picture, when the production sound is unusable (wind, plane overhead, a mic bump) or when a line is changed in post. The actor watches the loop and re-performs; a good ADR line is invisible, a bad one floats slightly "outside" the scene because it lacks the room's acoustics — which is why an ADR mixer adds matching reverb and "worldizes" the line (re-recording it played through a speaker in a real space) to seat it back into the room tone.

The eternal mix problem is the **dialogue / music / SFX balance**. The three families fight for the same frequency space and the same attention. The discipline: dialogue wins. Techniques include **ducking** (automatically lowering music/SFX when dialogue is present — sidechain compression keyed off the dialogue stem), **EQ carving** (cutting the music in the 1–4 kHz band where speech intelligibility lives so the voice has a clear lane), and simple level automation. Christopher Nolan is the famous controversialist here — *Tenet* and *Interstellar* drew complaints that dialogue was buried under sound and score; whether that's bold immersion or a mistake is a real, unsettled debate, but it proves the stakes: the moment the audience strains to understand words, you've lost them.

> **→ AI APPLICATION.** Generate dialogue/VO as a clean isolated stem (TTS gives you this for free — it's dry, no music). In the edit, sidechain-duck your music and ambience to that stem so the voice always sits on top, and high-pass your music slightly (roll off above ~2–3 kHz competition) under spoken sections. If you use a native-audio video model's spoken dialogue, be warned it is its weakest output (the search-confirmed limitation of Veo-class models) — prefer generating dialogue with a dedicated TTS and replacing the model's mouth-audio, or lean on ADR-style replacement.

## Voice-over: tool or crutch

**Voice-over (VO)** is narration laid over picture. It is non-diegetic (a narrator outside the scene) or sometimes a character's internal monologue. The hard truth: VO is powerful when it does something the image *cannot*, and a crutch when it merely describes what we can already see.

VO **works** when it adds an ironic or retrospective layer the picture lacks: the wry, doomed narration of *Sunset Boulevard* (spoken by a dead man), the hindsight of *Goodfellas* and *The Shawshank Redemption*, the unreliable interiority of *Fight Club*. It **fails** as a patch for a story that didn't dramatize its information — the studio-imposed explanatory narration on the original *Blade Runner* theatrical cut is the textbook crutch, and Ridley Scott removed it from the Director's Cut precisely because it told us what the images were already saying. Robert McKee's screenwriting maxim, voiced verbatim by the screenwriter character in *Adaptation*: never use voice-over to "stuff exposition" into the audience's ears.

The **documentary narration voice** is its own register: calm, authoritative, slightly slower than conversation, with deliberate phrasing and trust-conveying downward inflections at sentence ends. And the cardinal rule of all VO writing: **write for the ear, not the eye.** Spoken language is shorter sentences, simpler clauses, concrete nouns, contractions, and *rhythm* — you must be able to say it in one breath. Read every VO line aloud; if you stumble, rewrite it.

> **→ AI APPLICATION.** ElevenLabs is the default. **Eleven v3** (as of 2026, their most expressive model, 70+ languages) supports inline **audio tags** — `[whispers]`, `[laughs]`, `[sighs]`, `[sarcastic]`, and even SFX cues — to direct delivery, plus multi-speaker control; `eleven_multilingual_v2` is the stable workhorse and `eleven_flash_v2_5` the low-latency option. Yuval has a **cloned voice** in his account (Professional Voice Cloning, the high-fidelity tier), so brand VO should use that voice id rather than a stock voice — it's the difference between "an AI read this" and "this is *his* film." Craft notes that transfer directly: write short, breath-sized lines (the model paces better and you avoid run-on prosody); add commas and ellipses to *force* pauses; use the v3 tags sparingly for emotional beats; generate 2–3 takes and pick the one with the right rhythm. For documentary register, prompt/select a slower, lower, authoritative voice and don't over-tag — restraint reads as authority. See `18-ai-audio-vo-music-sfx-2026.md`.

## The 75-second teaser audio build

Short-form teasers run on a specific, repeatable audio architecture. The visuals carry attention; the *audio* carries the arousal arc. The recurring tools:

- **Riser** — a sound (synth sweep, rising noise, accelerating ticks) that pitches/builds *upward* to create anticipation. It is a promise that something is coming. Always resolves into an impact.
- **Impact / "braam"** — the deep, brass-and-sub-bass *hit* on a hard cut or title reveal. The "braam" (the *Inception* horn, popularized by Hans Zimmer / Zack Hemsey's "Mind Heist") became the trailer cliché precisely because it works: a massive low-frequency event reads as *consequence*. Pair every major riser with a braam landing.
- **Whoosh** — a fast pass-by sound under a transition (a swipe, a smash cut, a text slam) that gives motion a body and hides the cut. The audio equivalent of a wipe.
- **Needle-drop** — dropping a recognizable, perfectly-timed piece of music, usually with the *beat hitting the first hard cut*. Edit the visuals to the music's transients, not the other way around.

The shape: tension builds (risers, sparse hits, maybe a beat of near-silence) → the drop (needle-drop or braam on the hook) → escalating montage cut to the beat (whooshes on every transition) → final braam + hard cut to logo/CTA. The audio *is* the structure.

> **→ AI APPLICATION.** Generate each element as a separate cue: risers, braams, and whooshes from ElevenLabs SFX ("deep cinematic brass braam impact with sub-bass, single hit"; "fast tonal whoosh transition, short"); the bed/needle-drop from Suno or Udio. Build the timeline beat-first: lay the music, mark its transients, then cut every visual to land on a beat and put a whoosh on every transition and a braam on the title. This is the spine of Yuval's default FOMO-teaser style — the `yuv-fomo-teaser` skill already encodes the cut pattern; this chapter is the *why* and the source-of-cues beneath it.

## Loudness and the mix for phones

Most of your audience watches on a phone speaker, in public, **muted**. This dictates real mix decisions:

1. **Mix for small speakers.** Phone and laptop speakers can't reproduce deep sub-bass; a braam that shakes a theater is *inaudible* on a phone. Don't put critical information only in the lows. Check your mix on actual phone speakers, not studio monitors. The *midrange* (where voice lives) is what survives.
2. **Loudness normalization is enforced.** Platforms normalize to a target integrated loudness — roughly **-14 LUFS** for many streaming/social contexts (LUFS = Loudness Units Full Scale, the perceptual loudness standard; "integrated" = averaged over the whole clip). Master too hot and the platform turns you *down*, killing your dynamics; master too quiet and you're buried. Aim near the platform target and preserve some dynamic range for your silences and impacts to land. *(Verify exact per-platform targets — they drift; as of model training -14 LUFS is the common reference.)*
3. **Captions are not optional.** Because so many watch muted, on-screen captions carry the dialogue and VO for the silent majority — and they boost completion and accessibility even for sound-on viewers. Burn them in, time them to the audio, keep them readable on a small screen.

> **→ AI APPLICATION.** Loudness-normalize your final master to the platform target (a one-line ffmpeg `loudnorm` pass, or your NLE's loudness meter) and audition on a real phone before publishing. Auto-generate accurate captions from your VO/dialogue stem (the same TTS script *is* your caption text — perfect, no transcription error) and burn them in styled for mobile. For Yuval's bilingual EN/HE deliverables, generate both caption tracks from both VO scripts. The single highest-ROI mobile habit: design the opening so the **first 3 seconds make sense muted, with captions** — the sound is the reward for unmuting, not the price of entry.

## Spec'ing sound alongside the shot list

The professional discipline that ties this all together: **write a sound design list in parallel with your shot list.** For every shot/scene, specify the five layers explicitly so nothing defaults to "whatever the video model gave me." A workable per-shot row:

| Field | Example |
|---|---|
| Shot | 04 — alley, hero turns to face threat |
| Dialogue/VO | VO (cloned voice): "He never heard them coming." |
| Foley | 2 footsteps wet concrete; coat rustle on turn |
| Hard SFX | low metallic drone-in on reveal; single sub-impact on cut |
| Ambience | continuous "night city distant" bed (scene-wide) |
| Music | minor cello dread bed, swell to braam on cut to 05 |
| Notes | L-cut: ambience leads from shot 03; silence beat before braam |

Treating sound as a designed track from the script stage — not a post-hoc layer you sprinkle on a finished video — is the difference between AI footage and an AI *film*. The shot list (planned in `13-production-pipeline.md`) is one half; the sound list is its mandatory twin. For the full current toolchain — model ids, prices, prompt syntax, and the audio render pipeline — see **`18-ai-audio-vo-music-sfx-2026.md`**.

---

### Sources

- ElevenLabs — Text to Speech & Eleven v3: https://elevenlabs.io/docs/overview/capabilities/text-to-speech and https://elevenlabs.io/v3
- ElevenLabs — Sound Effects API (`eleven_text_to_sound_v2`): https://elevenlabs.io/docs/overview/capabilities/sound-effects and https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert
- ElevenLabs cheat sheet (2026 models): https://www.webfuse.com/elevenlabs-cheat-sheet
- Suno v5.5 (March 2026 features): https://suno.com/blog/v5-5
- Suno vs Udio 2026 comparison: https://neuronad.com/suno-vs-udio/ and https://www.tldl.io/blog/suno-vs-udio-comparison
- Google Veo 3 / 3.1 native audio: https://deepmind.google/models/veo/ and https://www.mindstudio.ai/blog/what-is-google-veo-3-video-audio
- Veo audio generation technical explainer: https://www.veo3ai.io/blog/veo-3-audio-generation-how-it-works-2026
