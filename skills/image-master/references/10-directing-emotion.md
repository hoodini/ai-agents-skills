# 10 — Directing Emotion: the Heart-Wrenching Frame

Technical realism gets an image PAST inspection. **Emotional direction is what makes it WIN.** The most common failure of a clean prompt: it describes blocking ("a cheetah runs", "a lion sits") and leaves expression to the model — which defaults to NEUTRAL. The result is technically fine and emotionally dead. Fix: direct the *decisive emotional moment*, the *gaze*, and one *signature micro-detail* in every frame.

## 0. Anchor every frame to a SPECIFIC, REAL pain — research it first
Generic sadness is forgettable; a specific, true, lived pain is unforgettable. Before designing a series about any real human experience, RESEARCH the actual pains of the people who lived it (testimonies, reporting) and anchor each image to ONE concrete pain. The image then carries a truth the viewer recognizes in their own body — the highest form of "distinct visual narrative." Translating the pain through an allegory (here: animals) makes it bearable AND universal, but the pain underneath must be real and specific — never invented.

Worked anchors — the Israeli home-front pains this series is built on (each → ONE image, all sourced in the project research):
- the parental dilemma of waking a just-asleep child for the siren, or gambling on letting them sleep;
- the elderly/disabled who cannot reach shelter in the 15–90s window ("Go, don't wait for me");
- 56% of homes have no safe room (mamad);
- the public shelter crammed like "a tin of sardines," no toilet, strangers at 3am;
- caught in the open, told to lie face-down and cover your head;
- hit despite doing everything right (a struck safe room);
- bone-deep exhaustion from nightly alarms; the parent who performs calm and never sleeps;
- the siren as a Pavlovian trauma trigger (≈60% report phantom sirens);
- pets paralyzed by terror they cannot decode.

## 1. Direct the decisive EMOTIONAL moment (not the action)
Never "X does Y." Always the peak instant of feeling: not "a cheetah runs" but "a cheetah at full desperate stretch twists her head back toward the incoming light, eyes wide." The verb carries the emotion. Freeze the moment a heart breaks, not a generic activity.

## 2. Animal affect cues — the believable vocabulary (real ethology, not cartoon)
- **Fear:** ears pinned flat back · eyes wide with the whites/sclera showing · pupils dilated · head lowered, body crouched · flared nostrils · rapid shallow breathing, flank heaving · trembling muscles · tail tucked · frozen mid-flinch.
- **Protection (parent):** body curled tight over the young · head lowered over them · muscles tensed · one paw drawing a cub in · eyes scanning, afraid-FOR-them, not aggressive.
- **Desperation / exhaustion:** panting open mouth · foam or saliva flecking the muzzle · heaving flanks · strained trembling limbs · stumbling.
- **Grief / shock:** frozen stillness · a wet glistening eye · a single tear cutting a track through dust or ash · the thousand-yard stare.
Avoid bared-teeth aggression unless intended — it reads as anger, not fear, and open mouths risk teeth artifacts.

## 3. The signature micro-detail — the thing that breaks the heart
Every frame needs ONE, named explicitly (the model will not invent it): a tear welling or tracking through dust · the airburst/fire mirrored in the wet eye · breath fogging in cold air · a cub's tiny paw gripping a parent's mane · foam at the mouth · dust caked on a tear-streaked face · trembling limbs · a single catchlight that is actually the war.

## 4. The eye is the story (and a craft flex)
Lead the viewer to ONE eye — large, sharp, wet, catchlit. Put the **reflection of the airburst/strobe inside the pupil**: simultaneously the most devastating emotional beat AND a showcase of fine-detail + reflection physics the judges reward. Reuse this "war-in-the-eye" device across the set for cohesion and a striking point of view. (The reflection must match the real light direction — see `02`.)

## 5. Emotion vs artifact — resolve the tension on purpose
Expressive faces raise facial-render risk; backs-turned is safe but emotion-poor. The resolution: keep the BODY/pose safe (turned, cropped, head-down for hands/limbs) while granting ONE readable, well-directed eye — face/head turned into frame, single catchlight, slight natural asymmetry (`01`). You can have both drama and safety; you just have to direct it. Don't trade away the eye for safety — trade away the hands.

## 6. The emotion gate (add to every generation)
Before generating any frame, answer in one line:
> **"What is the animal FEELING in this exact instant, which eye shows it, and what single detail makes me ache?"**
If the prompt doesn't answer all three, it will render neutral. Don't generate until it does.

## 7. Reality check
No prompt guarantees emotion — the model still has to deliver, and you will re-roll and pick the frame where the eye and the tear land. Generate a batch, then choose the one that aches. A clean-but-neutral frame is a reject, however technically perfect.

## 8. Legibility beats subtlety — make the key story element UNMISTAKABLE
A frame fails if a stranger can't tell what's happening in one second. If the core story element (here: the war) must be understood, render it BIG, clear and iconic — never "distant," "soft," or "subtle." Hard lessons from the first Reve batch:
- A "distant airburst" renders as a meaningless bright star / lens-flare. Instead write: *"the sky filled with the unmistakable Iron Dome interception — many curved interceptor-missile trails criss-crossing, orange airburst explosions, drifting smoke trails, over a city skyline."* Iconic and instantly readable.
- But make it read as an INTERCEPTION, not FIREWORKS: cascading sparks read as celebration. Specify *"rising interceptor streaks meeting incoming rockets in sharp mid-air airburst flashes, plus incoming rocket trails and smoke — a missile interception over a city, not fireworks, no cascading sparks."*
- An extreme close-up has NO room for context — the war vanishes and a red strobe just reads as "a lamp." Pull back to a MEDIUM shot so the subject's emotion AND the war sky are both in frame. Reserve extreme close-ups only when the war is dramatically, clearly reflected in the eye.
- Anchor the setting so it reads as the real place: an Israeli street, a concrete bomb shelter, a city skyline — never an ambiguous "cave/den."
- Wild animals (lion, tiger) read as "Israel at war" ONLY with the unmistakable war sky + a city behind them. Domestic animals (dog, cat) in a real street/shelter read fastest — lean the set toward maximum legibility.
- **Text colour:** don't default to flat white (reads generic). Specify it — masthead white, the recurring tagline in **alarm RED** (pops like a real magazine, ties to the Red-Alert siren).
Test before generating: would a stranger glancing for ONE second say "that animal is in a war"? If not, the war isn't big enough.
