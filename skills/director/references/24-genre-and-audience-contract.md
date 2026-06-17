# Genre & The Audience Contract

Genre is not a shelf in a bookstore. It is a **promise you make to a viewer's nervous system before they have seen a single frame** — and the most reliable way to fail at storytelling is to break that promise without knowing you made it. The single deepest reframe in this chapter, drawn from Shawn Coyne's *Story Grid* and consistent with Blake Snyder's *Save the Cat!*, is this:

> **Choosing a genre is choosing a set of expectations the audience will hold you to.** Those expectations take two concrete forms — *conventions* (the standing ingredients the genre requires) and *obligatory scenes/moments* (the specific events the audience came to see). Deliver them well and the viewer feels satisfied. Withhold them and the viewer feels cheated, even if they can't articulate why.

This is why "story problems" are so often invisible to a technically skilled, AI-native maker (the most common failure mode for the reader of this bible, per [03-character-and-scene-craft.md](03-character-and-scene-craft.md)). The footage is gorgeous, the cuts are clean, the dramatic question is even present (see [01-story-structure.md](01-story-structure.md)) — but the piece *declared* itself a thriller in shot 2 and then never put the hero at the mercy of the villain. The contract was opened and never paid. Coyne's line is exact: *"You must know what your reader is expecting before you can possibly satisfy her."*

## Genre as expectation management, not categorization

The word "genre" does two jobs and they are constantly confused. Coyne splits them, and the split is load-bearing.

- **Content genre (external):** *what the conflict is about and what's at stake.* Story Grid names twelve and pairs each with a **core value at stake** and a **core emotion** it must generate. The nine externally-driven ones are **Action, War, Horror, Crime, Thriller, Western/Eastern, Love, Performance, Society**; plus three internally-driven ones — **Status, Worldview, Morality**. Examples of the core question each answers: *Horror* — how do we stay safe and sane when victimized by a manifestation of our deepest fears? *Thriller* — how do we deal with ever-present, often incomprehensible evil in everyday life? *Crime* — how do we expose and punish those who break society's code? Each genre lives on a **value spectrum** (Love runs hate ↔ love, with intimacy as a midpoint; Action runs death ↔ life; Crime runs injustice ↔ justice). The genre is, precisely, *which value the story moves along.*

- **Story-type genre (structural):** *what shape the plot takes and what problem the hero is solving.* This is Snyder's contribution: he argues every film, regardless of its content genre, is really one of **ten** recurring story types. A horror film and a courtroom drama can be the same story-type ("Monster in the House") wearing different content skins.

You pick **one of each**. A film is a *content genre* (the subject and stakes) realized through a *story-type* (the structural engine). *Jaws* is content-genre Horror/Action delivered as the story-type "Monster in the House." *The Silence of the Lambs* is content-genre Crime/Thriller delivered as "Whydunit." Naming both, deliberately, is the move that separates a film with a story from a montage with a vibe.

> **→ SHORT-FORM:** In a 15–90s teaser you almost never have time to *develop* a content genre — but you have every second to *invoke* one. The viewer's brain pre-fills the missing story from a few genre signals: a low drone + a slow push-in down a hallway and they are *already* in horror, supplying their own dread. You are not telling a horror story; you are *renting the audience's horror schema* and letting it do the narrative work for free. Pick the skin in the first 3 seconds.

> **→ AI APPLICATION:** An LLM story-assistant should treat genre as a *typed contract* it extracts from the brief before writing a beat: `{content_genre, story_type, core_value, core_emotion, obligatory_scenes[], conventions[]}`. Generation then becomes a checklist-validated process — every draft is linted against "are the obligatory scenes present?" exactly the way a compiler checks that a declared interface is implemented.

## Conventions vs. obligatory scenes — the two halves of the promise

Coyne's most useful distinction, and the one most often blurred:

| | **Conventions** | **Obligatory scenes (moments)** |
|---|---|---|
| What they are | Standing *ingredients* the genre requires to be present | Specific *events* the audience is waiting to witness |
| Function | Set up expectation; "furnish the world" | Pay off expectation; deliver the catharsis |
| Thriller example | A master villain who makes it personal and overmatches the hero (a large power divide favoring the antagonist); a MacGuffin (the villain's object of desire); investigative red herrings; a clock | **The "Hero at the Mercy of the Villain" scene** |
| Love story example | The lovers are "made for each other"; a societal/internal force keeping them apart; a confidant | **The lovers meet; the first kiss / declaration; the dark moment of near-loss; the proof of love** |
| Whydunit example | A detective; a master criminal; clues and red herrings | The reveal of *who* and *why*; the speech explaining the crime |

The key mechanism: **conventions create the potential energy that obligatory scenes discharge.** If a thriller never establishes a villain who genuinely overmatches the hero (a convention), then the "hero at the mercy" scene (the obligatory moment) has nothing to release — the hero was never really in danger, so the escape is unearned. Coyne: the Hero at the Mercy of the Villain is *"the core event of the Thriller, when the protagonist unleashes his or her gift"* — the moment the hero is seemingly incapable of overpowering the villain and yet outsmarts or overpowers them anyway.

This is also where the chapter connects to the value-shift discipline from [03-character-and-scene-craft.md](03-character-and-scene-craft.md): an obligatory scene is just the *largest, genre-defining value turn* in the film. The first kiss is the scene where Love flips from apart(−) to together(+); the dark moment is where it flips back to near-loss(−) so the ending can earn its reunion. Genre tells you *which* turns are non-negotiable.

> **→ SHORT-FORM:** A teaser's job is to *promise* the obligatory scene without spending it — the trailer-maker's craft. A horror trailer cuts to black one frame before the kill; a heist trailer shows the vault and the crew and the "we have a problem" beat but withholds the reveal. You stage the convention (the team, the impossible target) so the viewer's brain *demands* the obligatory payoff — and then you make the click/watch the only way to get it. That demand is the curiosity gap of [04-engagement-psychology-hooks.md](04-engagement-psychology-hooks.md), genre-loaded.

> **→ AI APPLICATION:** Store, per content genre, a small library of `obligatory_scenes` and `conventions` (Story Grid publishes these; they're stable). When the assistant beats out a script, it (1) asserts each obligatory scene maps to at least one beat, (2) flags conventions that are merely named but never dramatized. This is the single highest-yield "story lint" an AI pipeline can run, because missing-obligatory-scene is the failure the maker can't see.

## Snyder's 10 story-type genres (verified)

From *Save the Cat! Goes to the Movies*. Each is a structural engine, not a subject. One line each:

1. **Monster in the House** — a "monster" (literal or metaphorical) is trapped in an enclosed space with victims, usually unleashed by someone's "sin." *Jaws, Alien, Fatal Attraction.*
2. **Golden Fleece** — a hero (often with a team) takes a *road/quest* after a prize, and the real growth happens on the journey, not at the goal. *Star Wars, Ocean's Eleven, road movies, heists.*
3. **Out of the Bottle** — a wish or magic with *rules* changes the hero's life; the lesson is that they win in the end *without* the magic. *Bruce Almighty, Liar Liar, Freaky Friday.*
4. **Dude with a Problem** — an *ordinary* person is thrust into *extraordinary* danger they didn't ask for and must survive. *Die Hard, Titanic, Schindler's List.*
5. **Rites of Passage** — life forces a painful transition (grief, addiction, adolescence, midlife) and the hero must accept it; the "monster" is the change itself. *10, Ordinary People, coming-of-age.*
6. **Buddy Love** — two people who complete (and irritate) each other; covers romance *and* platonic partnerships and pet movies. The genre of incompleteness made whole. *When Harry Met Sally, Rain Man, Brokeback Mountain.*
7. **Whydunit** — the draw is not *who* but *why*; the detective uncovers a dark truth — often about human nature — and is changed by it. *Chinatown, Zodiac, Citizen Kane.*
8. **Fool Triumphant** — an underestimated "fool" outclasses a powerful establishment that dismisses them; often features a disguise or an "insider" foil. *Forrest Gump, Being There, Amadeus* (told from the foil's view).
9. **Institutionalized** — a story about a *group/institution* (family, mob, hospital, company) and the cost of belonging vs. individuality; ends with the hero joining, burning it down, or going "out." *One Flew Over the Cuckoo's Nest, American Beauty, The Godfather.*
10. **Superhero** — the *inverse* of Dude with a Problem: an extraordinary being trapped in an ordinary world that can't comprehend them; the conflict is the gap between their power and others' smallness. *Gladiator, A Beautiful Mind, the literal cape movies.*

The payoff of Snyder's claim: if your story "feels broken," diagnose which of the ten it *is*, then check whether you're honoring that engine. A "Dude with a Problem" that gives the hero too much agency stops being suspenseful (they're no longer in over their head); a "Superhero" whose hero has no real opposition from the small-minded world has no engine at all.

> **→ SHORT-FORM:** Story-types are *castable in seconds* because they're so archetypal. A 30s product ad that frames the customer as a **Dude with a Problem** (ordinary person, sudden chaos, our product is the unexpected ally) reads instantly as a story. A 30s brand film that frames the founder as a **Superhero** (singular vision, a world too small to get it) reads as myth. You're not writing the full type — you're triggering its silhouette.

> **→ AI APPLICATION:** Make the ten a closed enum the assistant must choose from during concept ping-pong (Phase 1 of [19-the-grilling-workflow.md](19-the-grilling-workflow.md)). Forcing the model to commit to one type prevents the "beautiful disconnected footage" failure: each type ships with its own beat expectations, so the choice immediately constrains the beat sheet.

## Fulfill, then subvert — the order is everything

Conventions exist to be *honored*; their power is precisely what makes *violating* them feel meaningful. But there is an iron rule, and it is the rule most often broken by clever makers who want to seem original:

> **You can only subvert a convention the audience believes you are about to fulfill.** Subversion that arrives before the expectation is set isn't subversion — it's just absence. Coyne's framing is that the thrill comes when a story zigs where the reader expects it to zag — but only after the expectation to zag has been set. That requires first making the reader *think it's going to zag.*

- *Psycho* kills its protagonist at the midpoint — a genuine shock — *but only after* 40 minutes of treating Marion as the unmistakable lead (the convention is fully installed before it's detonated).
- *Cabin in the Woods* deconstructs Monster-in-the-House horror — *but* it spends its first act letting you settle into the cliché it's about to expose.
- A "happily ever after" subverted into tragedy (*La La Land*) lands *because* Buddy Love trained you to expect the reunion.

The maker's discipline: **acknowledge the convention on screen, then break it.** A subversion the audience didn't see coming because it was never set up just reads as a story that forgot to deliver. This is the difference between "surprising yet inevitable" (Aristotle's ideal; see also Pixar's Rule on coincidence in [02-pixar-22-rules.md](02-pixar-22-rules.md)) and merely random.

## Tone vs. genre — they are different dials

**Genre** is the contract (what must happen). **Tone** is the *attitude* toward that contract (how it feels to watch). They're independent knobs, and confusing them produces tonal whiplash — the piece that can't decide if it's serious.

- *Get Out* is content-genre Horror with a satirical, socially-critical tone.
- *Shaun of the Dead* is Monster-in-the-House structure (zombies) with comedic tone — a "zom-rom-com."
- *Fargo* is Crime with a folksy, deadpan tone that makes the violence more disturbing, not less.

The rule: **pick the genre first (it sets the obligatory scenes), then pick the tone (it sets the texture of every choice within them).** A horror film played for laughs still owes you the "monster unleashed" scene — it just delivers it with a wink. Establish tone *early and consistently*; the first 15 seconds teach the audience how to feel about everything after, and an unstable tone reads as the maker not knowing what they made.

> **→ SHORT-FORM:** Tone is the fastest brand differentiator in an ad. Two products in the same genre skin (say, a Golden Fleece "journey" ad) feel like different *companies* purely through tone — Apple's reverent minimalism vs. a challenger brand's irreverent snark. Lock tone in the first beat and never wobble; a 30s spot has no runtime to recover from tonal confusion.

## Mixing genres — primary contract plus seasoning

Almost every film blends content genres (Coyne: the Thriller itself is a blend of Action, Crime, and Horror). But blending is not democracy. There is always a **primary content genre that owns the obligatory scenes**, and secondary genres that *flavor* it.

- *Alien* — primary Horror (it owes you the monster-stalks-survivors scenes); secondary Sci-Fi (setting/texture) and Action (the third act).
- *The Princess Bride* — primary Buddy Love / Golden Fleece; seasoned with Comedy, Adventure, and meta-framing.

The failure mode is **co-equal genres fighting for the obligatory slot:** a film trying to be fully a love story *and* fully a thriller will starve both — neither the "dark moment of near-loss" nor the "hero at the mercy" gets the room it needs, and the audience feels two half-paid contracts. Decide which genre's promise the *ending* fulfills. That's your primary. Everything else seasons.

> **→ AI APPLICATION:** Represent genre blends as a weighted list with one flagged primary: `genres: [{Love, primary:true}, {Thriller, secondary}]`. The assistant enforces obligatory scenes only for the primary, and treats secondaries as conventions/texture — preventing the model from trying to satisfy two full contracts and bloating the runtime.

## Genre → the Kill Shot (mapping the contract to the commercial goal)

The "Kill Shot" is this bible's term for the one outcome a piece exists to produce. Genre is the most efficient lever for it, because each genre comes pre-wired with an emotional payload. Match the contract to the conversion you need:

| Commercial goal (Kill Shot) | Best-fit genre lens | Why it converts |
|---|---|---|
| **Sales / "buy this and change"** | **Golden Fleece** + transformation (often *Out of the Bottle*) | The viewer projects onto the hero's journey to a better state; the product is the road or the magic. The promise *is* transformation. |
| **Brand / aspiration** | **Superhero** + Spectacle | Frames the brand as a singular, world-shifting force; viewer adopts the myth. Apple, Nike. |
| **Trust / category education** | **Whydunit** | Positions you as the one who reveals the hidden truth ("the real reason your X is failing"); authority through revelation. |
| **Founder / origin story** | **Dude with a Problem** | Relatable ordinary-person-in-over-their-head start makes the win feel earned and earns parasocial loyalty. |
| **Community / movement** | **Institutionalized** (the joining kind) | Belonging is the payoff; viewer wants *in* the group. |
| **Fear-driven / urgent fix** | **Monster in the House** / **Thriller** | The problem is the monster; your product is the gift the hero unleashes at the mercy moment. Use sparingly and honestly (see [05-neuroscience-honest.md](05-neuroscience-honest.md) on not manufacturing false dread). |

The reasoning: a Kill Shot is an emotional state you need the viewer to arrive in (desire, trust, belonging, urgency). Genre is the *fastest reliable generator* of a target emotion because the audience's schema pre-loads it. Choosing the wrong genre for the goal — e.g. a fear-based Monster-in-the-House frame when you actually need aspirational trust — fights your own conversion.

> **→ SHORT-FORM:** This is how a 30s ad "feels like a story" without becoming a bloated micro-film (the #1 trap when porting feature theory to short content). You do **not** run a full arc. You **borrow one genre's grammar and deliver the single beat that triggers its core emotion** — the transformation reveal (Golden Fleece), the heist reveal (Crime), the monster-unleashed turn (Horror). One genre, one obligatory beat, one emotion. The viewer's schema supplies the rest of the "story" for free. Trying to cram a three-act structure into 30 seconds is what produces the talky, lifeless micro-film; renting a genre schema is what avoids it.

> **→ AI APPLICATION:** The brief-to-contract step is the assistant's first real decision: read the commercial goal, select the genre lens that maps to it from the table above, and *only then* generate beats. The genre choice becomes the spec the rest of the pipeline (storyboard prompts in [17-ai-storyboard-prompting-and-keyframes.md](17-ai-storyboard-prompting-and-keyframes.md), shot grammar in [06-shots-framing-composition.md](06-shots-framing-composition.md)) inherits — a horror-skin teaser and a superhero-skin teaser will request different lenses, lighting, and pacing automatically.

## The working checklist

Before generating a frame, the maker (or the LLM) should be able to fill this in:

1. **Content genre (primary):** ________ → **core value at stake:** ____ → **core emotion to produce:** ____
2. **Story-type (one of Snyder's 10):** ________
3. **Conventions I will install:** ________ (the world/character ingredients)
4. **Obligatory scenes I owe the audience:** ________ (the events they came for)
5. **Tone:** ________ (and it stays constant)
6. **Any convention I'm subverting** — and *where I set it up first.*
7. **Kill Shot:** ________ → does the chosen genre's core emotion match it?

If any line is blank, that's where the "story problem" lives. Genre isn't decoration you add after the footage — it's the contract that tells you which footage you were obligated to shoot in the first place.

## Sources

- Shawn Coyne, *Story Grid* — "Genre Conventions: Must-Have Elements of Story": https://storygrid.com/genres-have-conventions-and-obligatory-scenes/
- Story Grid — "Content Genre: Objects of Desire and Values in Story" (the 12 content genres and core values/emotions): https://storygrid.com/content-genre/
- Story Grid — "Internal Genres: Worldview, Morality, and Status in Story": https://storygrid.com/internal-genres/
- Story Grid — "Thriller Genre: The Blending of Action, Crime, and Horror Stories" (Hero at the Mercy of the Villain): https://storygrid.com/thriller-genre/
- Story Grid — "Editor Roundtable: Conventions & Obligatory Scenes": https://storygrid.com/editor-roundtable-conventions-obligatory-scenes/
- Story Grid — "Love and An Immersive Story Grid Experience" (love-story obligatory scenes): https://storygrid.com/2228-2/
- Blake Snyder, *Save the Cat!* — "Blake Snyder's Glossary of Genre Terms": https://savethecat.com/tips-and-tactics/blake-snyders-glossary-of-genre-terms-2
- Save the Cat!® — "10 Story Genres and Beat Sheets" (forum reference): https://savethecat.com/forum/10-genres-and-beat-sheets
- Erik Bork — "Using the Save the Cat Genres" (the ten story-types explained): https://www.flyingwrestler.com/2010/11/using-save-the-cats-genres/
- The Write Practice — "Story Grid Genre: What You Need to Know": https://thewritepractice.com/story-grid-genre/
- Alice Sudlow — "The 12 Core Genres That Power Every Great Story": https://alicesudlow.com/content-genres/
