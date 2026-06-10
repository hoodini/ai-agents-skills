# NN-explainer builder: fills template_b.tpl given the measured Manim duration.
# Usage: py gen_b.py <manim_duration_seconds>
import sys
sys.stdout.reconfigure(encoding="utf-8")

DM = float(sys.argv[1])
M0 = 13.0                 # manim clip start
S5 = round(M0 + DM, 2)    # results
S6 = round(S5 + 8.0, 2)   # punch
S7 = round(S6 + 6.0, 2)   # outro
D  = round(S7 + 6.0, 2)   # total

# Hebrew captions over the Manim body, windows as fractions of the clip
# windows matched to the measured chapters: neuron 0-13.27s, network 13.27-23.7s, training 23.7-34.5s
MCAPS = [
    (0.015, 0.180, 'נוירון מלאכותי: מקבל מספרים, שוקל אותם — <em>ומחליט אם לירות</em>'),
    (0.200, 0.360, 'המשקלים הם <em>הידע</em>: כל קו = חשיבות אחרת'),
    (0.395, 0.660, 'מחברים אלפי נוירונים בשכבות — <em>וזו רשת</em>'),
    (0.700, 0.985, 'אימון: כל טעות מכווננת את המשקלים — <em>והשגיאה צונחת</em>'),
]
mc_html, mc_js = [], []
for i,(f0,f1,txt) in enumerate(MCAPS):
    t0 = round(M0 + f0*DM, 2); t1 = round(M0 + f1*DM, 2); dur = round(t1-t0, 2)
    mc_html.append(f'<div id="mc{i}" class="mcap clip" data-start="{t0}" data-duration="{dur}" data-track-index="{20+i}">{txt}</div>')
    mc_js.append(f'tl.from("#mc{i}",{{yPercent:30,opacity:0,duration:0.3,ease:"power2.out",overwrite:"auto"}},{t0});'
                 f'tl.to("#mc{i}",{{opacity:0,duration:0.28,ease:"power1.in",overwrite:"auto"}},{round(t1-0.3,2)});')

html = (open("template_b.tpl", encoding="utf-8").read()
        .replace("@@DM@@", str(round(DM,2)))
        .replace("@@S5@@", str(S5)).replace("@@S6@@", str(S6)).replace("@@S7@@", str(S7))
        .replace("@@D@@", str(D))
        .replace("@@MCAPS_HTML@@", "\n      ".join(mc_html))
        .replace("@@MCAPS_JS@@", "\n      ".join(mc_js)))
open("index.html", "w", encoding="utf-8").write(html)
print(f"wrote index.html — manim {DM}s, total {D}s (S5 {S5} / S6 {S6} / S7 {S7})")
