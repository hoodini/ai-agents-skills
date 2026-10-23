"""V2 karaoke — bigger video-title style, positioned in the LEFT HALF
(below the cards, above the bottom key-moment strip). Per-word pop with
strong scale entrance + slight Y-translation. Hebrew = Karantina Bold (yuv-design-system §2).
English brand tokens = Anton.
"""
from __future__ import annotations
import json, re
from pathlib import Path

EDIT = Path(r"C:\Users\User\Desktop\edit")
TRANSCRIPT = EDIT / "transcripts" / "0423.json"
EDL = EDIT / "edl.json"

# 9:16: Caption row at bottom-left of left-half (left half = x 0-540).
#   Alignment=2 (bottom-center). MarginL=0, MarginR=540 forces center within 0..540.
#   MarginV from bottom: 380 places at y=1540 (above key-moment strip @ y=1730).
# 16:9: Caption row at bottom-left half. MarginR=860 forces center within 0..1060.
#   MarginV=170 places at y=910 (above key strip @ y=920).
ASS_HEADERS = {
    "9x16": """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: HE,Karantina,135,&H00FFFFFF,&H00FFFFFF,&H00111111,&H00000000,1,0,0,0,100,100,0,0,1,9,4,2,0,0,40,1
Style: EN,Anton,124,&H0000E5FF,&H0000E5FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,11,4,2,0,0,40,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""",
    "16x9": """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: HE,Karantina,112,&H00FFFFFF,&H00FFFFFF,&H00111111,&H00000000,1,0,0,0,100,100,0,0,1,7,3,2,0,440,80,1
Style: EN,Anton,104,&H0000E5FF,&H0000E5FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,9,3,2,0,440,80,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""",
}

ENGLISH_RE = re.compile(r"^[A-Za-z][A-Za-z0-9\-]*$")
ACCENT_HE = {"מטורף", "טירוף", "אוטומטית", "גדול", "גרפיקות", "ננו", "בננה", "חדש"}


def fmt_time(t):
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t - h * 3600 - m * 60
    cs = int(round((s - int(s)) * 100))
    sec = int(s)
    if cs == 100:
        cs = 0
        sec += 1
    return f"{h:01d}:{m:02d}:{sec:02d}.{cs:02d}"


def escape(text):
    text = text.strip()
    while text and text[-1] in ",.;:":
        text = text[:-1]
    return text.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")


def main():
    transcript = json.loads(TRANSCRIPT.read_text(encoding="utf-8"))
    edl = json.loads(EDL.read_text(encoding="utf-8"))
    words = [w for w in transcript["words"] if w.get("type") == "word"]

    events = []
    seg_offset = 0.0
    for r in edl["ranges"]:
        rs, re_ = float(r["start"]), float(r["end"])
        dur = re_ - rs
        in_range = [w for w in words if w["start"] >= rs and w["end"] <= re_ + 0.05]
        for i, w in enumerate(in_range):
            local_start = max(0.0, w["start"] - rs)
            if i + 1 < len(in_range):
                local_end = max(local_start + 0.08, in_range[i + 1]["start"] - rs)
            else:
                local_end = min(dur, w["end"] - rs + 0.30)
            out_start = local_start + seg_offset
            out_end = local_end + seg_offset
            raw = w["text"].strip()
            if not raw:
                continue
            clean = escape(raw)
            if not clean:
                continue
            is_eng = bool(ENGLISH_RE.match(clean))
            is_accent = clean in ACCENT_HE
            # Stronger video-title pop: scale 1.45 -> 1.0 with cubic settle, slight slide-up
            # \fad(60,80) for in/out fade, \move for upward slide
            pop = (r"{\fscx150\fscy150\t(0,140,\fscx100\fscy100)"
                   r"\fad(60,80)")
            if is_eng:
                style = "EN"
                text = pop + r"}" + clean.upper()
            elif is_accent:
                style = "HE"
                text = pop + r"\c&H0000E5FF&\t(0,80,\frz-3)\t(80,160,\frz3)\t(160,220,\frz0)}" + clean
            else:
                style = "HE"
                text = pop + r"}" + clean
            events.append(
                f"Dialogue: 0,{fmt_time(out_start)},{fmt_time(out_end)},{style},,0,0,0,,{text}"
            )
        seg_offset += dur

    body = "\n".join(events) + "\n"
    for aspect, header in ASS_HEADERS.items():
        out_path = EDIT / ("karaoke.ass" if aspect == "9x16" else f"karaoke_{aspect}.ass")
        out_path.write_text(header + body, encoding="utf-8")
        print(f"  wrote {out_path.name}: {len(events)} events ({aspect})")


if __name__ == "__main__":
    main()
