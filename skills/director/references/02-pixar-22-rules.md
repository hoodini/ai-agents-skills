# Pixar's 22 Rules of Storytelling — Annotated

In 2011, **Emma Coats** — then a storyboard artist at Pixar — began tweeting story tips she'd absorbed from senior story people in the building, under the hashtag **#storybasics**. She posted them sporadically between roughly March and May 2011 (and a few into 2012). The internet collected them, numbered them, and slapped the title "Pixar's 22 Rules of Storytelling" on the set. Coats has been clear ever since about two things: (1) these are her paraphrases of advice she heard, **not an official Pixar doctrine carved on a wall**, and (2) she'd call them *guidelines*, not rules. Treat them that way. They're not laws of physics; they're the compressed, hard-won folk wisdom of a studio that, at its peak, had an almost unfair hit rate.

Why does a thread of tweets matter to an AI filmmaker? Because the 22 are a *debugging checklist for narrative*. Most AI-generated shorts fail not at the pixel level but at the story level — they look gorgeous and mean nothing. The 22 are exactly the questions that catch "looks great, says nothing" before you've burned 200 generations. This chapter reproduces each rule **verbatim** (wording verified against the original-tweet transcriptions; see Sources), then annotates: what it really means, the mistake it prevents, a concrete film example, and how it bites in short-form AI video.

A note on verbatim text: several second-hand listings online have quietly "improved" the grammar of the tweets (e.g. "Stack the odds against them" instead of Coats' actual "Stack the odds against"). The wording below follows the original tweet transcriptions. Where I quote, that's exactly what she wrote, abbreviations and all.

---

## The 22, Annotated

### Rule 1
> **You admire a character for trying more than for their successes.**

**What it means.** Audiences bond with *effort and intention*, not outcomes. A character who struggles, fails, and gets up again earns our investment; a character who simply wins is a trophy, not a person. The mistake it prevents: writing competence porn — flawless protagonists who never strain — which reads as smug and emotionally inert.

**Example.** *WALL·E* barely succeeds at anything for the first act; he just keeps *trying* to connect (collecting trinkets, reaching for EVE's hand). We're hooked before he's "won" anything.

**→ AI APPLICATION.** In a 8–10 second AI clip you can't show an arc of attempts, but you can show *the posture of trying* in one frame: a hand reaching and not quite grasping, a runner mid-stumble, eyes straining upward. Prompt the *micro-gesture of effort*, not the victory pose. In Veo 3.1 / Sora 2, write the verb as a struggle ("she strains to pull the door, knuckles white") rather than a state ("she opens the door").

### Rule 2
> **You gotta keep in mind what's interesting to you as an audience, not what's fun to do as a writer. They can be v. different.**

**What it means.** The thing you enjoy *making* is often not the thing anyone enjoys *watching*. Self-indulgent worldbuilding, a clever camera move, a pun you love — these serve the author, not the viewer. The mistake it prevents: building scenes that exist because they were satisfying to construct.

**Example.** Pixar's own brain trust famously cut huge swaths of *Toy Story 2* and *Ratatouille* — material the makers were attached to — because it didn't serve the audience's experience.

**→ AI APPLICATION.** This is the single most violated rule in AI film. It is *intoxicating* to generate beautiful drone shots and slow-motion particles because the tool makes them effortless. Ask of every shot: would a stranger scrolling care, or am I just enjoying that the model can do this? See `04-engagement-psychology-hooks.md` on retention — the first 3 seconds must serve the *viewer's* curiosity, not your delight in the render.

### Rule 3
> **Trying for theme is important, but you won't see what the story is actually about til you're at the end of it. Now rewrite.**

**What it means.** You start with a hunch at the theme, but the *real* theme only reveals itself once the whole thing exists. Then you go back and sharpen everything toward it. The mistake it prevents: locking your meaning prematurely and forcing the story to illustrate a thesis.

**Example.** *Up* began as a fantasy about a floating city; the theme of grief and letting go of a dead spouse emerged through iteration, and the famous "Married Life" montage was built once the team understood what the film was *actually* about.

**→ AI APPLICATION.** Generate a rough cut of clips before you commit to your edit's "meaning." Often the emotional through-line you discover in the assembly is better than your script. Budget for a *theme-pass* re-prompt: once you see what your footage is saying, re-generate 2–3 hero shots to point harder at it.

### Rule 4
> **Once upon a time there was ___. Every day, ___. One day ___. Because of that, ___. Because of that, ___. Until finally ___.**

**What it means.** This is the **Story Spine** (full treatment below). It's a minimal causal skeleton: a status quo, a routine, a disruption, a chain of consequences, a resolution. The mistake it prevents: episodic "and then... and then..." structure, where events happen in *sequence* but not in *causal* relation.

**Example.** *Finding Nemo* maps cleanly: Once upon a time a clownfish lived safely; every day he overprotected his son; one day Nemo was captured; *because of that* Marlin chased across the ocean; *because of that* he was changed by Dory and the journey; until finally he found Nemo and learned to let go.

**→ AI APPLICATION.** Use the spine as your shot-list spine. Each "because of that" is a *causal cut* — the strongest kind of edit, because the viewer's brain is already asking "and so?". For a 30-second AI short, force at least one genuine "because of that": the second shot must be a *consequence* of the first, not just the next pretty thing.

### Rule 5
> **Simplify. Focus. Combine characters. Hop over detours. You'll feel like you're losing valuable stuff but it sets you free.**

**What it means.** Compression is creation. Merge two thin characters into one thick one; cut the subplot; skip the connective tissue the audience can infer. The mistake it prevents: bloat — the death of pacing by a thousand "necessary" beats.

**Example.** In *Toy Story*, many early-draft toys were combined or cut so Woody and Buzz could carry the emotional weight without dilution.

**→ AI APPLICATION.** AI shorts live or die on density. You have ~30–60 seconds. Combine: a single character who is both the comic relief and the heart. Hop over detours: don't render the walk *to* the door — cut to the door. Every second of "transition" you generate is a second you didn't spend on a beat that matters.

### Rule 6
> **What is your character good at, comfortable with? Throw the polar opposite at them. Challenge them. How do they deal?**

**What it means.** Drama is the gap between a character's competence and the situation. Find their comfort zone, then violate it. The mistake it prevents: situations that don't *cost* the character anything because they're already equipped for them.

**Example.** *Finding Nemo* gives an anxious, control-obsessed father the most uncontrollable possible environment: the open ocean. Maximum pressure on the exact weakness.

**→ AI APPLICATION.** Establish the comfort zone *visually* in shot 1, then break it in shot 2. A pristine surgeon → blood on the gloves. A pin-drop-quiet librarian → a screaming alarm. The visual contrast *is* the conflict; the model renders the collision and the viewer infers the stakes.

### Rule 7
> **Come up with your ending before you figure out your middle. Seriously. Endings are hard, get yours working up front.**

**What it means.** Know your destination, then build the road to it. The mistake it prevents: the meandering middle that exists because you didn't know where you were going — the most common cause of "it fell apart in act two."

**Example.** Pixar story leads (notably Andrew Stanton) talk about working backward from the ending so every earlier beat *plants* what the finale *pays off*.

**→ AI APPLICATION.** Decide your final shot first — the image you want to leave burned in. Then every preceding shot is engineered as setup or contrast for it. In practice: write the last prompt, generate it, then reverse-engineer the opening so they rhyme (a visual or color callback). See `10-editing-theory.md` on bookending.

### Rule 8
> **Finish your story, let go even if it's not perfect. In an ideal world you have both, but move on. Do better next time.**

**What it means.** A finished imperfect thing beats a perfect unfinished thing. Shipping teaches you what polishing never will. The mistake it prevents: infinite-refinement paralysis.

**Example.** Every Pixar film shipped with compromises the directors would still list for you — they finished anyway, then carried the lessons forward.

**→ AI APPLICATION.** Acute danger in AI film: the slot-machine of re-generation. You *can* roll the dice 80 times for a marginally better take. Set a hard cap (e.g. "best of 6, then move on"). The compounding returns are in *finishing and posting* and learning from the response, not in the 7th re-roll.

### Rule 9
> **When you're stuck, make a list of what WOULDN'T happen next. Lots of times the material to get you unstuck will show up.**

**What it means.** Enumerate the impossible/forbidden options; the act of bounding the space often reveals the right move (or shows you the "wouldn't" is secretly the most interesting "would"). The mistake it prevents: staring at a blank middle.

**Example.** A classic writers'-room technique — list the clichés you refuse, and the un-clichéd path becomes visible by elimination.

**→ AI APPLICATION.** Stuck on a transition between two AI clips? List what *shouldn't* connect them (a hard match cut, a sound bridge, an impossible camera move through a wall), and one of those "shouldn't"s is usually your most striking edit. This pairs with Rule 12.

### Rule 10
> **Pull apart the stories you like. What you like in them is a part of you; you've got to recognize it before you can use it.**

**What it means.** Reverse-engineer the films that move you to learn *why*, so the technique becomes a tool you can wield deliberately instead of a vibe you can't reproduce. The mistake it prevents: cargo-culting surface style without understanding mechanism.

**Example.** Pixar's directors are encyclopedic students of film history — Brad Bird's action grammar is consciously built on studying classic blocking and staging.

**→ AI APPLICATION.** Shot-list your favorite 30 seconds of a film: lens, duration per shot, color, what the cut does. That decomposition *is* your prompt template. The whole `directors/` bible is essentially this rule industrialized — see `17-ai-storyboard-prompting-and-keyframes.md`.

### Rule 11
> **Putting it on paper lets you start fixing it. If it stays in your head, a perfect idea, you'll never share it with anyone.**

**What it means.** Externalize early; the idea in your head is frictionless and therefore fake-perfect. On the page it has problems you can actually solve. The mistake it prevents: protecting an idea by never testing it.

**→ AI APPLICATION.** Generate a *cheap, fast* version immediately — a rough storyboard with an image model (Nano Banana / Midjourney) before you spend on video. The mediocre first pass exposes the structural problem that the imagined version concealed. Cheap externalization first, expensive video second.

### Rule 12
> **Discount the 1st thing that comes to mind. And the 2nd, 3rd, 4th, 5th – get the obvious out of the way. Surprise yourself.**

**What it means.** Your first ideas are everyone's first ideas — they're the training-data average. Originality lives past the obvious. The mistake it prevents: clichéd, predictable beats and imagery.

**Example.** Pixar's pitch process forces many alternatives per beat precisely to push past the default.

**→ AI APPLICATION.** This rule is *doubly* binding for AI, because a generative model is *literally* a machine for producing the statistically most-likely image. "Cinematic shot of a lonely robot" gives you the average of every such image ever made. Push to the 5th idea in the *concept*, and use specificity in the prompt to escape the mean: a named lens, an unexpected color, a specific imperfection. See the LLM-grilling section at the end — this is rule #1 to hard-enforce.

### Rule 13
> **Give your characters opinions. Passive/malleable might seem likable to you as you write, but it's poison to the audience.**

**What it means.** Characters who *want* and *judge* and *push back* generate drama; agreeable ditherers generate nothing. The mistake it prevents: the passive protagonist things happen *to*.

**Example.** Mr. Incredible's stubborn opinion (heroes should be allowed to be heroes) drives the entire plot of *The Incredibles*.

**→ AI APPLICATION.** Even in a wordless clip, *opinion* is readable as attitude: a defiant chin, a dismissive turn, a refusal. Prompt the *stance*, not just the appearance: "she folds her arms and looks away, unimpressed" carries more story than "a woman stands in a room."

### Rule 14
> **Why must you tell THIS story? What's the belief burning within you that your story feeds off of? That's the heart of it.**

**What it means.** The films that land carry a genuine conviction from their maker — a belief the story *metabolizes*. The mistake it prevents: hollow, competent, soulless content that nobody needed to make.

**Example.** *Inside Out* exists because Pete Docter genuinely needed to understand his own daughter's emotional change — that personal stake is felt in every frame.

**→ AI APPLICATION.** AI lowers the cost of making *anything* to near zero, which means the deciding variable is no longer skill — it's *conviction*. The shorts that break through are the ones with a real point of view. Before generating, answer in one sentence: what do *I* believe that this clip argues? If you can't, you're making wallpaper. The end-section LLM should refuse to proceed until this is answered.

### Rule 15
> **If you were your character, in this situation, how would you feel? Honesty lends credibility to unbelievable situations.**

**What it means.** Emotional truth buys you fantastical license. A talking rat is believable if his *feelings* are honest. The mistake it prevents: spectacle without grounding — the CGI-soup problem where nothing matters because nothing feels real.

**Example.** *Ratatouille*: the premise is absurd, but Remy's longing and shame are exact, so we buy it completely.

**→ AI APPLICATION.** AI loves to give you the impossible (a whale flying over a city). It will read as empty unless something in the frame is *emotionally* honest — a child's genuine awe, a real reaction. Ground every surreal AI image with one true human emotional beat. See `05-neuroscience-honest.md`.

### Rule 16
> **What are the stakes? Give us reason to root for the character. What happens if they don't succeed? Stack the odds against.**

**What it means.** Stakes = the cost of failure. We need to know what's at risk and to want the character to avoid it. The mistake it prevents: tension-free scenes where nothing is actually on the line.

**Example.** *Toy Story 3*'s incinerator sequence works because the stakes are total — death — and the odds are absolute, so the hand-clasp resignation is devastating.

**→ AI APPLICATION.** In short form, stakes must be *legible in seconds*. Visual shorthand: a countdown, a cliff edge, a single tear, a closing door. Establish "what's at risk" in the first 1–2 shots or the viewer has no reason to watch shot 3. Stakes are the engine of the arousal arc the `cinematic-ai-video` skill operationalizes — this chapter is the *why* beneath that.

### Rule 17
> **No work is ever wasted. If it's not working, let go and move on – it'll come back around to be useful later.**

**What it means.** Cut material isn't lost; it's compost. The idea that didn't fit here feeds something later. The mistake it prevents: refusing to cut because you're protecting sunk cost.

**Example.** Pixar's cut scenes and abandoned films repeatedly seeded later projects (ideas from one film's discarded act resurfacing in another's premise).

**→ AI APPLICATION.** Keep a "b-roll graveyard" of every generation you cut. Those orphan clips become transitions, texture, or the seed of the next short. Nothing you generate is wasted if you archive it with good tags. This also lowers the emotional cost of obeying Rule 5 (cutting).

### Rule 18
> **You have to know yourself: the difference between doing your best & fussing. Story is testing, not refining.**

**What it means.** Learn to distinguish *real* improvement from anxious fiddling. Story development is about *testing* whether the structure works, not polishing surfaces. The mistake it prevents: mistaking motion for progress.

**→ AI APPLICATION.** The direct antidote to AI's re-generation slot-machine (cf. Rule 8). "Testing" = does this *shot do its job in the edit*? "Fussing" = re-rolling for a prettier version of a shot that already works. Test the cut, don't fuss the frame.

### Rule 19
> **Coincidences to get characters into trouble are great; coincidences to get them out of it are cheating.**

**What it means.** Random bad luck *starting* trouble is fair and lifelike; random good luck *solving* it (deus ex machina) robs the character of agency and the audience of catharsis. The mistake it prevents: unearned, deflating resolutions.

**Example.** It's fine that Marlin loses Nemo to a passing diver (coincidence in); it would be cheating if a random current simply swept Nemo home. The resolution must come from the characters' *earned* change.

**→ AI APPLICATION.** In micro-narratives the temptation is to resolve with spectacle ("and then everything magically fixes"). Resolve with *consequence* instead — the payoff should visibly stem from something established earlier (Rule 7). A callback resolution feels earned; a random one feels like the model just stopped.

### Rule 20
> **Exercise: take the building blocks of a movie you dislike. How d'you rearrange them into what you DO like?**

**What it means.** A deliberate craft drill: failure is more instructive than success because the mechanism is exposed. Diagnose *why* something doesn't work, then fix it. The mistake it prevents: only studying what you love, and never learning to spot/repair structural faults.

**→ AI APPLICATION.** Take a *bad* viral AI video (there are millions) and re-cut/re-prompt it into something that works. This sharpens your eye for the specific failure modes of generative film — uncanny faces held too long, motion with no motivation, edits with no causal logic — far faster than admiring polished work.

### Rule 21
> **You gotta identify with your situation/characters, can't just write 'cool'. What would make YOU act that way?**

**What it means.** "Cool" is a description, not a motivation. You must be able to inhabit the character's logic from the inside. The mistake it prevents: empty style — characters doing impressive things for no internal reason.

**Example.** A villain who is merely "badass" is forgettable; one whose cruelty has a comprehensible internal logic (you can *feel* why) is terrifying and memorable.

**→ AI APPLICATION.** The deepest trap in AI film, because the tools make "cool" *trivially* generatable. A slow-mo character walking from an explosion is the platonic "cool" shot — and means nothing. Before you prompt the cool image, answer: what does this person *want* such that this action follows? Encode that want as the verb of the scene (next section).

### Rule 22
> **What's the essence of your story? Most economical telling of it? If you know that, you can build out from there.**

**What it means.** Distill to the irreducible core — one sentence, one image. Once you have the essence, every elaboration is a deliberate choice rather than clutter. The mistake it prevents: not knowing what your story *is*, so it sprawls.

**Example.** *Up* = "an old man flies his house to honor his dead wife's dream." Everything else hangs off that line.

**→ AI APPLICATION.** Write your short's logline in one sentence before generating a single frame. If the essence is one image, sometimes the most economical telling *is* one perfect 8-second shot — not 40 cuts. Economy is a feature in short form, not a limitation.

---

## Beyond the 22: Pixar's Deeper Story Practices

The 22 tweets are the famous part. The *load-bearing* craft at Pixar lives in a handful of practices the tweets only gesture at.

### The Story Spine (the real version)

Rule 4 is a compressed quote of the **Story Spine**, which Pixar did *not* invent. It was created by playwright/improviser **Kenn Adams** around 1991 for improvised theatre and teaching kids; his collaborator **Kat Koppett** later named it "the Story Spine," and improv teacher **Rebecca Stockley** carried it into Pixar in the late 1990s. The full canonical form:

> **Once upon a time...** *(the status quo — who, where, the world as it stably is)*
> **Every day...** *(the routine — what reliably happens, establishing normal)*
> **Until one day...** *(the inciting incident — the disruption that breaks routine)*
> **Because of that...** *(consequence)*
> **Because of that...** *(consequence — repeat as the rising action needs)*
> **Until finally...** *(the climax — the decisive consequence)*
> **And ever since then...** *(the new normal — resolution / changed status quo)*

Note Coats' tweet compresses "Until one day" to "One day" and omits the closing "And ever since then." The full version is better because it makes the **before/after symmetry** explicit: the "new normal" must *differ* from the "every day," and that difference *is* the character's arc. The engine of the whole structure is the **"because of that"** links — they enforce *causality*, which is the difference between a story and a list. (See `01-story-structure.md` for how the spine maps onto three acts.)

### The Color Script

A **color script** is a sequence of small, low-detail pastel/digital paintings — one per beat or sequence — that plot the film's *emotional temperature* as a journey in color and light, *before* any final art is made. Pixar pioneered using them systematically; *Finding Nemo*'s color script is the canonical example, charting warm safety → cold danger → warm reunion across the whole film. The point isn't pretty thumbnails; it's that **emotion has a color arc**, and you design it deliberately rather than discovering it accidentally shot-by-shot.

**→ AI APPLICATION.** Make a color script for your short *first*, using an image model to generate one tiny key frame per beat with the intended palette and lighting. This becomes your **continuity bible**: feed those frames back as style/color references (image-to-video conditioning, or as reference images in Veo/Sora/Midjourney) so your separately-generated clips share an emotional through-line instead of looking like 12 unrelated renders. This is the highest-leverage fix for the "incoherent AI montage" problem. See `08-lenses-lighting-color.md`.

### The Brain Trust and Iterative Dailies

Pixar's **Brain Trust** is a standing group of directors/story people who watch each other's films-in-progress and give blunt, ego-free notes. Two rules make it work, per Ed Catmull's *Creativity, Inc.*: the Brain Trust has **no authority** (the director isn't obligated to take any note), and feedback attacks the *film*, not the person. Combined with **dailies** — the culture of showing unfinished work *every day* to peers — this institutionalizes Rules 8, 11, and 18: externalize early, finish-then-improve, test rather than fuss.

**→ AI APPLICATION.** Solo AI filmmakers have no Brain Trust — so *build a synthetic one*. Use an LLM (or several with different persona prompts: "harsh editor," "confused first-time viewer," "platform algorithm") to critique your rough cut against the 22 rules before you finalize. Crucially, replicate the *no-authority* rule: the LLM diagnoses problems, *you* decide. And replicate *dailies*: show your work-in-progress to real humans early and often — the cost of being wrong privately is paid in wasted generations.

### "The Verb of the Scene"

A Pixar/theatre discipline: every scene (and every shot) has one **active verb** describing what the character is *doing to* the other party — *to seduce, to intimidate, to plead, to escape, to forgive*. Not an adjective ("she's sad"), not a topic ("the breakup scene") — a transitive verb. If you can't name the verb, the scene has no spine and the actors (or the camera) have nothing to play.

**→ AI APPLICATION.** This is the most direct craft-to-prompt translation in this entire chapter. **Generative video models are verb-engines** — they animate *actions*. A prompt built on a state ("a sad woman in a kitchen") produces a static, dead clip; a prompt built on a verb ("a woman *scrubbing* the same clean spot on the counter, *refusing* to look at the empty chair") produces motion *with motivation* — exactly what reads as alive. Before writing any video prompt, name the verb. Then make the verb the grammatical core of the prompt. This single habit fixes more "lifeless AI clip" problems than any model upgrade.

---

## AI APPLICATION: Which Rules an LLM Story-Assistant Must Hard-Enforce

If you wire an LLM as the front-end "story grilling" layer of an AI-film skill, do **not** make it gently surface all 22. Most are craft advice the user can take or leave. A small subset are *gates* — the LLM should refuse to proceed to generation until they're satisfied, because violating them guarantees a hollow film no amount of render quality can save. Enforce these four hard, in roughly this order:

| Gate | Rule | What the LLM must extract from the user, and the failure it blocks |
|---|---|---|
| **Conviction** | **#14 — Why must YOU tell THIS story?** | One sentence stating the belief/point of view driving the piece. Blocks soulless wallpaper. If the user can't answer, the LLM should push (not generate): "What do you actually believe that this argues?" |
| **Audience over author** | **#2 — interesting to the audience, not fun for the writer** | For each planned shot, "why would a stranger scrolling care?" Blocks the self-indulgent-render trap that is AI film's defining failure mode. |
| **Structure** | **#4 — the Story Spine** | At minimum one real *"because of that"* causal link. Blocks the "and then... and then..." pretty-montage with no spine. The LLM should make the user fill the spine template before shot-listing. |
| **Originality** | **#12 — discard the obvious (1st through 5th)** | Reject the user's first concept and first imagery as the training-data average and demand the 5th idea. Doubly critical because the *generator itself* outputs the statistical mean — see Rule 12 above. |

Two secondary checks worth adding as *warnings* (not hard gates): **#21** (can the user state the character's *want*, not just "cool"?) and **#19** (does the resolution come from earned consequence, not a coincidence/spectacle?). Both catch the most common ways short AI films feel empty even when they look expensive.

Design note, in keeping with the Brain Trust's **no-authority** principle: the LLM *diagnoses and grills*, it does not overrule. It should be able to say "this fails Rule 14 and here's why," then let the human decide to proceed anyway. An enforcer with veto power becomes a creativity tax; an enforcer that asks the right four questions becomes the synthetic Brain Trust every solo AI filmmaker lacks.

---

## Sources

- Aerogramme Studio, "Pixar's 22 Rules of Storytelling" — https://www.aerogrammestudio.com/2013/03/07/pixars-22-rules-of-storytelling/
- Aerogramme Studio, "The Story Spine: Pixar's 4th Rule of Storytelling" — https://www.aerogrammestudio.com/2013/03/22/the-story-spine-pixars-4th-rule-of-storytelling/
- Open Culture, "Pixar's 22 Rules of Storytelling" — https://www.openculture.com/2013/03/pixars_22_rules_of_good_storytelling.html
- David Knopp, "Emma Coats's 22 'Rules' for #StoryBasics" (original-tweet transcription) — https://www.davidknoppblog.com/emma-coatss-22-rules/
- Kindlepreneur, "Story Spine: 7 Steps to Pixar's Storytelling Structure" (Kenn Adams / Kat Koppett / Rebecca Stockley provenance) — https://kindlepreneur.com/story-spine/
- Ed Catmull, *Creativity, Inc.* (Brain Trust, dailies, no-authority feedback culture)
