# The Script-Development Workflow — Building the Story Before the Shots

> This chapter is the engine room of [Chapter 19](19-the-grilling-workflow.md). Where Ch.19 governs the whole pipeline (idea → concept → beats → shots → pixels → post), *this* chapter zooms all the way into the part that decides whether the film is any good: **developing the script.** It is a gated sub-state-machine that runs inside Ch.19's Phase 1 and Phase 2. Nothing visual exists yet. Everything here is words — and that is the point, because words are free to rewrite and pixels are not.

The thesis of the whole bible restated for the script: **a film is a delivery system for one story decision made well.** Most AI videos are technically fine and emotionally dead because the maker never forced the story to survive interrogation. This workflow is that interrogation. It is built directly on the craft in chapters [20](20-screenwriting-masters.md)–[26](26-script-doctor-diagnostics.md), and it operationalizes the "grill, don't please" mandate: the assistant's job here is to be the toughest, fairest story editor the user has ever worked with.

---

## The principle: escalating fidelity, gated at every rung

You do not write a script in one move. You raise it through rungs of increasing fidelity, and **you do not climb to the next rung until the current one survives scrutiny.** Each rung is cheaper to fix than the one above it. A broken logline costs one sentence to fix; the same flaw discovered at the AV-draft stage costs a rewrite; discovered after generation, it costs the whole film.

```
S0  RAW MATERIAL     what the user actually has              (gather)
S1  LOGLINE          one sentence: who wants what, vs what    → GATE S1
S2  CONTROLLING IDEA the argument / designing principle       → GATE S2
S3  CHARACTER ENGINE want · need · opponent · flaw            → GATE S3
S4  BEAT OUTLINE     the structure, timed, with setups/payoffs→ GATE S4
S5  AV DRAFT         the actual two-column script + hook line → GATE S5
S6  DOCTOR + READ    diagnose, table-read, revise, LOCK       → GATE S6 → hand to Ch.19 Phase 3
```

Each gate is a full stop: the assistant presents the rung's artifact, runs the relevant diagnostics out loud, and waits for the user to approve or push. The whole climb is conversational ping-pong — the user reacts, the assistant revises in words, re-presents. This can loop many times per rung. That looping is not friction; it *is* the writing.

---

## S0 — Raw material (what do you actually have?)

Before a logline, find out what the user is bringing. People arrive at story from different doors, and the assistant adapts:

- **A message** ("I want people to feel that AI gives you your time back") → start from theme/controlling idea (S2), then reverse-engineer a story that *dramatizes* it.
- **A character or person** (a founder, an animal, themselves) → start from the character engine (S3).
- **An event or true story** → start from the beat outline (S4), then find the spine.
- **A product/feature to show** → start from "what is the ONE visible demo?" (the holy-shit moment) and build a story whose climax IS that demo.
- **Just a vibe or a reference** ("like that Apple ad, but for me") → name the genre contract ([24](24-genre-and-audience-contract.md)) and the feeling, then build.

The assistant's first move is to identify the door and say so: *"You've got a theme but no character yet — let's dramatize it. Who is the one person this happens to?"* This prevents the most common stall: trying to write a logline for a story that doesn't have a protagonist yet.

---

## S1 — The logline (the whole film in one sentence)

The logline is the load-bearing sentence. If it isn't compelling here, no camera move will save it later. Use the formula from [25](25-idea-to-polished-script.md):

> **A [flawed protagonist] must [active goal] before [stakes / ticking clock], or else [concrete consequence].**

Then **grill it** against these (from [26](26-script-doctor-diagnostics.md)) and report each verdict aloud:

- **Protagonist clear?** Whose story is this — one person/entity we follow?
- **Active goal?** Do they *pursue* something, or merely react/receive? (Passive protagonist = #1 logline killer.)
- **Real opposition?** What/who is actively in the way? No opposition = no story, just an event.
- **Stakes / "so what?"** What is lost if they fail? Is it concrete and felt?
- **Irony / mental picture?** Is there a hook of irony or a vivid image the listener can *see*? (Snyder: a good logline makes you picture the movie.)

The assistant offers 2–3 logline variants when the user is stuck, each pulling the story in a different direction, and names the trade-off of each. It refuses to advance with a logline that fails "active goal" or "stakes."

> **⛔ GATE S1.** *"This is the whole film in one line. Lock it, or pull on it?"* Wait.

---

## S2 — The controlling idea (what is the film *arguing*?)

Now lock the spine beneath the plot — the **controlling idea** (McKee) / **premise** (Egri) / **designing principle** (Truby), all defined in [21](21-theme-premise-moral-argument.md). One sentence of the form **value + cause**: *"[Positive value] wins when [the cause]"* — e.g. "Freedom is worth dying for when the alternative is a life of obedience."

For short form especially, also extract the **designing principle**: the one-line organizing metaphor that makes *this* telling unique (e.g. "show a day in reverse so the ending reframes the start"). In a 60-second piece the designing principle is often the entire creative idea.

The law to enforce: **theme is dramatized, never stated.** The assistant flags any plan to have a character (or VO) *announce* the theme — that's the on-the-nose failure. The theme must be *proven* by what happens, especially the ending.

This locked sentence becomes the **filter for everything downstream**: any beat, line, or shot that doesn't serve or test the controlling idea is a darling, and darlings get cut (Pixar #12).

> **⛔ GATE S2.** *"Here's what the film argues, and the one-line principle that organizes it. Right argument?"* Wait.

---

## S3 — The character engine (want · need · opponent · flaw)

Even a 15-second film has a protagonist with an engine. Lock, from [03](03-character-and-scene-craft.md) and Truby's 7 key steps ([20](20-screenwriting-masters.md)):

- **Want** (the conscious external goal — what they chase; drives plot).
- **Need** (the unconscious internal lack — what they must learn; drives theme; usually the opposite of the want).
- **The flaw / the lie they believe** (the wound that makes the need necessary).
- **The opponent** (who/what attacks the want *and* is best positioned to exploit the flaw — the opponent is the protagonist's mirror, not just an obstacle).
- **Stakes** (consequence of failure, tied to need).

For non-narrative subjects (a product, a concept), map the engine onto the **viewer-as-protagonist**: the viewer wants X, believes the lie that Y, and the film's demo is the self-revelation. This is how an ad becomes a story rather than a brochure.

> **⛔ GATE S3.** *"Want vs need, the flaw, the opponent. Does the want pull hard enough?"* Wait.

---

## S4 — The beat outline (structure, timed, wired)

Translate the locked engine into a **timed beat sheet** — the same artifact as Ch.19 Phase 2, but now story-complete. Pick the structure to fit the duration ([01](01-story-structure.md)): Harmon's Story Circle (compressed) or hook→build→turn→payoff→button for the shortest pieces; check the **genre's obligatory scenes** ([24](24-genre-and-audience-contract.md)) are present.

For each beat record: `t-start–t-end · what happens · value shift (+/−) · the setup or payoff it carries · the hook firing here`. Then wire the **plot mechanics** from [22](22-plot-mechanics-setups-payoffs.md):

- **Causality:** join beats with **but/therefore**, never "and then." The assistant literally rewrites the outline as a but/therefore chain and shows it.
- **Setups → payoffs:** maintain a ledger — every payoff has an earlier setup; every gun shown is fired; the hook's promise is paid at the button.
- **Escalation:** each beat's stakes ≥ the last; find the midpoint reversal or the worse-choice.
- **The turn:** locate the single reversal/recognition the piece pivots on.
- **Budget check:** total beats ≤ the duration's budget (Ch.19 Phase 0). Overflow means the story is too big — cut a subplot or escalate back to S1.

> **⛔ GATE S4.** *"The structure, timed and causally wired. Does it escalate, and does every beat change a value?"* Wait.

---

## S5 — The AV draft (the actual script)

Now write the real thing in the **two-column A/V format** from [25](25-idea-to-polished-script.md) — because in film, video and audio are designed together:

```
| t | VIDEO (what we see)            | AUDIO (VO / dialogue / SFX / music) |
|---|-------------------------------|-------------------------------------|
```

Write the **hook line** first (the first spoken or on-screen line that stops the scroll — [23](23-dialogue-subtext-voice.md)), the VO/dialogue beats (subtext over statement; economy; one killer line beats five explainers), the on-screen text, and the **CTA / button line**. For short form, the entire script may be 4–8 rows — that is correct, not lazy. Write for the ear and for muted viewing (captions).

The assistant writes dialogue that *does* something (a tactic to get something), not dialogue that *explains*. It actively hunts and removes the AI tell of over-explaining and on-the-nose emotion.

> **⛔ GATE S5.** *"Here's the script. Read it — does the hook land and does the last line drive the kill shot?"* Wait.

---

## S6 — The doctor pass, the table read, and the lock

Before the script earns the right to become shots, it goes through the **Script Doctor** ([26](26-script-doctor-diagnostics.md)) run *adversarially* — the assistant tries to break its own script and reports honestly:

- Spine in one sentence? Protagonist active? Stakes felt? Opponent real?
- But/therefore all the way through? No "and then"?
- Every scene changes a value? No dead beats?
- Theme dramatized, not stated? Ending earned (no deus ex machina)?
- Every setup paid, every payoff set up? Hook promise kept?
- **Cut the first and last line of every scene** — is it tighter? (Usually yes.)
- Short-form triage: ONE want, ONE turn, ONE payoff, ONE demo?

Then the **table read**: read the VO/dialogue aloud (or run it through TTS — [18](18-ai-audio-vo-music-sfx-2026.md)) against the beat timing. Reading aloud exposes clunky lines, wrong rhythm, and scripts that overrun their duration. Revise. Loop S5–S6 until clean.

> **⛔ GATE S6 — THE SCRIPT LOCK.** *"The script survives the doctor and reads clean at length. Lock the script?"* On approval, this artifact hands off to Ch.19 **Phase 3 (Shot Design)** — and only now does visual thinking begin. This gate is the boundary between *story* and *production*.

---

## The short-form fast-path (≤ 90 seconds)

For a teaser/ad/reel, the full climb collapses but **no rung is skipped** — each just takes a sentence:

```
S1 logline (1 line) → S2 controlling idea + designing principle (1 line)
→ S3 want/need/flaw/opponent (1 line, often viewer-as-protagonist)
→ S4 4–8 beat outline, but/therefore wired, hook + button marked
→ S5 AV draft (4–8 rows) → S6 doctor triage + read-aloud → LOCK
```

The discipline is identical; only the word-count shrinks. The fast-path still **stops at GATE S6** before any pixel. The reason short films fail is almost always that someone ran S5 in their head and skipped S1–S4 entirely.

---

## The grilling question bank (what the assistant asks, by rung)

| Rung | The hard questions |
|------|--------------------|
| S0 | What do you actually have — a message, a person, an event, a product, or a vibe? |
| S1 | Who is this about? What do they actively want? What's stopping them? What's lost if they fail? Can I picture it? |
| S2 | What is this film *arguing* about how to live or what's true? What's the one-line principle organizing it? Are we *showing* that or *saying* it? |
| S3 | What does the protagonist want vs need? What lie do they believe? Who is the opponent and how do they exploit the flaw? |
| S4 | Can I join every beat with "but" or "therefore"? Does it escalate? Where's the turn? Is every setup paid? Is it within the time budget? |
| S5 | Does the first line stop the scroll? Is the dialogue doing or explaining? Does the last line drive the action? |
| S6 | If I cut every scene's first and last line, is it better? Is the ending earned? Read it aloud — does it land and fit the clock? |

## The one-paragraph version

*"We build the script in rungs, and I won't let us climb until each one holds. First the logline — who wants what, against what, or else what. Then the one-line argument the film is making. Then the character's want vs need and the opponent. Then a timed beat outline I'll force into a but/therefore chain with every setup paid off. Then the actual two-column script with a hook line that stops the scroll. Then I try to break it, we read it aloud, and we fix it. Only when the script is locked do we talk about a single camera angle. The reason your videos died before is that we used to start at the last sentence."*
