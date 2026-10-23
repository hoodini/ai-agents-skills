"""V3 animations sized for the LEFT HALF of the new layout.
Bar chart: 4 categories (only-real-words from transcript), tall vertical layout.
Flow diagram: 4 nodes vertical for 9:16, horizontal for 16:9.
"""
from __future__ import annotations
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys

sys.path.insert(0, r"C:\Users\User\Desktop\edit")
from apple_glass import (
    blank, apple_glass_card, draw_text_safe as t_text, COLORS, RAD_CARD,
)
from bidi import get_display


def rtl(s):
    return get_display(s)


EDIT = Path(r"C:\Users\User\Desktop\edit")
FONTS = EDIT / "fonts"
ANTON = str(FONTS / "Anton-Regular.ttf")
KARANTINA = str(FONTS / "Karantina-Bold.ttf")      # Hebrew display (yuv-design-system §2)
ASSISTANT_XB = str(FONTS / "Assistant-ExtraBold.ttf")  # Hebrew card text
ASSISTANT_B = str(FONTS / "Assistant-Bold.ttf")    # Hebrew labels


def ease_out_cubic(t):
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def ease_out_back(t, k=1.6):
    t = max(0.0, min(1.0, t))
    c3 = k + 1
    return 1 + c3 * (t - 1) ** 3 + k * (t - 1) ** 2


# ---- METRICS bar chart ----
# 4 categories said in video: המרות / הוצאות / תקציבים / קליקים
BARS = [
    ("המרות",   COLORS["yellow"]),
    ("הוצאות",  (255, 90, 30)),
    ("תקציבים", COLORS["whatsapp"]),
    ("קליקים",  COLORS["pink"]),
]


def render_bars_frame(W, H, area, fi, total_frames, title_text, vertical_layout=True):
    img = blank(W, H)
    x, y, w, h = area
    img = Image.alpha_composite(img, apple_glass_card(W, H, x, y, w, h, RAD_CARD,
                                                      tint=(255, 255, 255, 30)))
    f_title = ImageFont.truetype(KARANTINA, int((max(40, h // 16) * 1.25)))
    f_label = ImageFont.truetype(ASSISTANT_B, max(30, h // 22))
    title_h = h // 9
    t_text(img, (x + w // 2, y + title_h // 2 + 30), title_text, f_title,
           fill=(255, 214, 110, 255), stroke=(0, 0, 0, 200), stroke_w=2)

    if vertical_layout:
        # 4 horizontal bars (good for narrow vertical card)
        n = len(BARS)
        bar_h = (h - title_h - 80 - (n - 1) * 22) // n
        bar_w_max = w - 80
        bx = x + 40
        y0 = y + title_h + 50
        for i, (he_raw, color) in enumerate(BARS):
            offset = i * 4
            local = (fi - offset) / 16.0
            p = ease_out_back(local) if local > 0 else 0.0
            target_ratio = [0.92, 0.72, 0.52, 0.95][i]
            w_now = max(0, int(bar_w_max * target_ratio * p))
            by = y0 + i * (bar_h + 22)
            # Glow
            if w_now > 10:
                glow = blank(W, H)
                gd = ImageDraw.Draw(glow)
                gd.rounded_rectangle([bx - 8, by - 4, bx + w_now + 8, by + bar_h + 4],
                                     radius=18, fill=color + (140,))
                glow = glow.filter(ImageFilter.GaussianBlur(radius=14))
                img = Image.alpha_composite(img, glow)
            # Bar with horizontal gradient
            if w_now > 4:
                bar_layer = blank(W, H)
                bd = ImageDraw.Draw(bar_layer)
                for sx in range(w_now):
                    t = sx / max(1, w_now)
                    r = int(color[0] * (0.55 + 0.45 * t))
                    g = int(color[1] * (0.55 + 0.45 * t))
                    b = int(color[2] * (0.55 + 0.45 * t))
                    bd.line([(bx + sx, by), (bx + sx, by + bar_h)],
                            fill=(r, g, b, 255))
                mask = Image.new("L", (W, H), 0)
                md = ImageDraw.Draw(mask)
                md.rounded_rectangle([bx, by, bx + w_now, by + bar_h],
                                     radius=14, fill=255)
                bar_layer.putalpha(mask)
                img = Image.alpha_composite(img, bar_layer)
            # Label inside the bar (right-aligned, RTL Hebrew)
            t_text(img, (bx + bar_w_max - 20, by + bar_h // 2),
                   rtl(he_raw), f_label,
                   fill=(255, 255, 255, 255), stroke=(0, 0, 0, 220), stroke_w=2,
                   anchor="rm")
    else:
        # Horizontal vertical bars (4 columns) for wide card
        n = len(BARS)
        gap = int(w * 0.05)
        bar_w = (w - 80 - gap * (n - 1)) // n
        bars_top = y + title_h + 30
        bars_h = h - title_h - 130
        baseline_y = bars_top + bars_h
        d = ImageDraw.Draw(img)
        d.line([(x + 40, baseline_y + 2), (x + w - 40, baseline_y + 2)],
               fill=(180, 180, 200, 80), width=2)
        for i, (he_raw, color) in enumerate(BARS):
            bx = x + 40 + i * (bar_w + gap)
            offset = i * 4
            local = (fi - offset) / 16.0
            p = ease_out_back(local) if local > 0 else 0.0
            target_ratio = [0.92, 0.72, 0.52, 0.95][i]
            h_now = max(0, int(bars_h * target_ratio * p))
            top_y = baseline_y - h_now
            if h_now > 10:
                glow = blank(W, H)
                gd = ImageDraw.Draw(glow)
                gd.rounded_rectangle([bx - 12, top_y - 6, bx + bar_w + 12, baseline_y + 12],
                                     radius=20, fill=color + (140,))
                glow = glow.filter(ImageFilter.GaussianBlur(radius=18))
                img = Image.alpha_composite(img, glow)
            if h_now > 4:
                bar_layer = blank(W, H)
                bd = ImageDraw.Draw(bar_layer)
                for sy in range(h_now):
                    t = sy / max(1, h_now)
                    r = int(color[0] * (0.55 + 0.45 * (1 - t)))
                    g = int(color[1] * (0.55 + 0.45 * (1 - t)))
                    b = int(color[2] * (0.55 + 0.45 * (1 - t)))
                    bd.line([(bx, top_y + sy), (bx + bar_w, top_y + sy)],
                            fill=(r, g, b, 255))
                mask = Image.new("L", (W, H), 0)
                md = ImageDraw.Draw(mask)
                md.rounded_rectangle([bx, top_y, bx + bar_w, baseline_y],
                                     radius=18, fill=255)
                bar_layer.putalpha(mask)
                img = Image.alpha_composite(img, bar_layer)
            t_text(img, (bx + bar_w // 2, baseline_y + 50), rtl(he_raw), f_label,
                   fill=(255, 255, 255, 255), stroke=(0, 0, 0, 200), stroke_w=2)
    return img


# ---- FLOW diagram ----
# Nodes: words actually said in video: Meta Ads, Claude, automatic, results
FLOW_NODES = [
    ("META ADS",    "מערכת",      COLORS["facebook"],  "f"),
    ("CLAUDE",      "סוכן",        COLORS["claude"],    "C"),
    ("AUTOMATIC",   "אוטומטית",    COLORS["yellow"],    "↑"),
    ("CAMPAIGNS",   "קמפיינים",    COLORS["green"],     "✓"),
]


def render_flow_v_frame(W, H, x, y, w, h, fi, total_frames):
    img = blank(W, H)
    img = Image.alpha_composite(img, apple_glass_card(W, H, x, y, w, h, RAD_CARD,
                                                      tint=(255, 255, 255, 30)))
    f_title = ImageFont.truetype(KARANTINA, int((max(36, h // 22) * 1.25)))
    t_text(img, (x + w // 2, y + 50), rtl("איך זה עובד"), f_title,
           fill=(255, 214, 110, 255), stroke=(0, 0, 0, 200), stroke_w=2)

    n = len(FLOW_NODES)
    node_size = 96
    node_y_top = y + 140
    avail_h = h - 200
    gap = (avail_h - n * node_size) // (n - 1)
    cx = x + 90  # left side, leaves room for text right of node
    f_letter = ImageFont.truetype(ANTON, 50)
    f_en = ImageFont.truetype(ANTON, 44)
    f_he = ImageFont.truetype(ASSISTANT_XB, 28)

    for i, (en, he_raw, color, letter) in enumerate(FLOW_NODES):
        ny = node_y_top + i * (node_size + gap)
        offset = i * 5
        local = (fi - offset) / 9.0
        p = ease_out_back(local) if local > 0 else 0.0
        if p <= 0:
            continue
        scale = max(0.0, p)
        rs = int(node_size * scale)
        glow = blank(W, H)
        gd = ImageDraw.Draw(glow)
        gd.ellipse([cx - rs, ny + node_size // 2 - rs,
                    cx + rs, ny + node_size // 2 + rs],
                   fill=color + (170,))
        glow = glow.filter(ImageFilter.GaussianBlur(radius=18))
        img = Image.alpha_composite(img, glow)
        d2 = ImageDraw.Draw(img)
        d2.ellipse([cx - rs // 2, ny + node_size // 2 - rs // 2,
                    cx + rs // 2, ny + node_size // 2 + rs // 2],
                   fill=color + (255,), outline=(255, 255, 255, 220), width=3)
        if p > 0.7:
            t_text(img, (cx, ny + node_size // 2 + 2), letter, f_letter,
                   fill=(255, 255, 255, 255), stroke=(0, 0, 0, 200), stroke_w=2)
            t_text(img, (cx + node_size, ny + node_size // 2 - 14), en, f_en,
                   fill=(255, 255, 255, 255), stroke=(0, 0, 0, 200), stroke_w=2, anchor="lm")
            t_text(img, (cx + node_size, ny + node_size // 2 + 30), rtl(he_raw), f_he,
                   fill=(220, 220, 230, 255), anchor="lm")
        if i > 0:
            prev_ny = node_y_top + (i - 1) * (node_size + gap)
            prev_bottom = prev_ny + node_size
            cur_top = ny
            arrow_offset = (i - 1) * 5 + 6
            arrow_local = (fi - arrow_offset) / 6.0
            ap = ease_out_cubic(arrow_local) if arrow_local > 0 else 0.0
            if ap > 0:
                head_y = prev_bottom + int((cur_top - prev_bottom) * ap)
                d = ImageDraw.Draw(img)
                phase = (fi * 4) % 22
                dash_y = prev_bottom - phase
                while dash_y < head_y:
                    seg_top = max(prev_bottom, dash_y)
                    seg_bot = min(head_y, dash_y + 14)
                    if seg_bot > seg_top:
                        d.line([(cx, seg_top), (cx, seg_bot)],
                               fill=(255, 214, 110, 240), width=6)
                    dash_y += 22
                if ap > 0.85:
                    d.polygon(
                        [(cx, head_y + 14),
                         (cx - 14, head_y - 8),
                         (cx + 14, head_y - 8)],
                        fill=(255, 214, 110, 240),
                    )
    return img


def render_flow_h_frame(W, H, x, y, w, h, fi, total_frames):
    img = blank(W, H)
    img = Image.alpha_composite(img, apple_glass_card(W, H, x, y, w, h, RAD_CARD,
                                                      tint=(255, 255, 255, 30)))
    f_title = ImageFont.truetype(KARANTINA, int((44) * 1.25))
    t_text(img, (x + w // 2, y + 50), rtl("איך זה עובד"), f_title,
           fill=(255, 214, 110, 255), stroke=(0, 0, 0, 200), stroke_w=2)
    n = len(FLOW_NODES)
    node_size = 110
    avail_w = w - 160
    gap = (avail_w - n * node_size) // (n - 1)
    node_x_left = x + 80
    cy = y + 230
    f_letter = ImageFont.truetype(ANTON, 56)
    f_en = ImageFont.truetype(ANTON, 40)
    f_he = ImageFont.truetype(ASSISTANT_XB, 30)
    for i, (en, he_raw, color, letter) in enumerate(FLOW_NODES):
        nx = node_x_left + i * (node_size + gap)
        offset = i * 5
        local = (fi - offset) / 9.0
        p = ease_out_back(local) if local > 0 else 0.0
        if p <= 0:
            continue
        scale = max(0.0, p)
        rs = int(node_size * scale)
        glow = blank(W, H)
        gd = ImageDraw.Draw(glow)
        gd.ellipse([nx + node_size // 2 - rs, cy - rs,
                    nx + node_size // 2 + rs, cy + rs],
                   fill=color + (170,))
        glow = glow.filter(ImageFilter.GaussianBlur(radius=20))
        img = Image.alpha_composite(img, glow)
        d2 = ImageDraw.Draw(img)
        d2.ellipse([nx + node_size // 2 - rs // 2, cy - rs // 2,
                    nx + node_size // 2 + rs // 2, cy + rs // 2],
                   fill=color + (255,), outline=(255, 255, 255, 220), width=3)
        if p > 0.7:
            t_text(img, (nx + node_size // 2, cy + 2), letter, f_letter,
                   fill=(255, 255, 255, 255), stroke=(0, 0, 0, 200), stroke_w=2)
            t_text(img, (nx + node_size // 2, cy + node_size // 2 + 30), en, f_en,
                   fill=(255, 255, 255, 255), stroke=(0, 0, 0, 200), stroke_w=2)
            t_text(img, (nx + node_size // 2, cy + node_size // 2 + 75), rtl(he_raw), f_he,
                   fill=(220, 220, 230, 255))
        if i > 0:
            prev_nx = node_x_left + (i - 1) * (node_size + gap)
            prev_right = prev_nx + node_size
            cur_left = nx
            arrow_offset = (i - 1) * 5 + 6
            arrow_local = (fi - arrow_offset) / 6.0
            ap = ease_out_cubic(arrow_local) if arrow_local > 0 else 0.0
            if ap > 0:
                head_x = prev_right + int((cur_left - prev_right) * ap)
                d = ImageDraw.Draw(img)
                phase = (fi * 4) % 22
                dash_x = prev_right - phase
                while dash_x < head_x:
                    seg_l = max(prev_right, dash_x)
                    seg_r = min(head_x, dash_x + 14)
                    if seg_r > seg_l:
                        d.line([(seg_l, cy), (seg_r, cy)],
                               fill=(255, 214, 110, 240), width=6)
                    dash_x += 22
                if ap > 0.85:
                    d.polygon(
                        [(head_x + 14, cy),
                         (head_x - 8, cy - 12),
                         (head_x - 8, cy + 12)],
                        fill=(255, 214, 110, 240),
                    )
    return img


def save_seq(frames, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    for i, f in enumerate(frames, start=1):
        f.save(out_dir / f"{i:04d}.png")


def main():
    # 9:16 — bars in left card area (480x880-ish), flow vertical
    out9 = EDIT / "cards_v6_9x16"
    out9.mkdir(parents=True, exist_ok=True)
    bar_seq = [render_bars_frame(1080, 1920, area=(40, 220, 480, 900),
                                  fi=fi, total_frames=36,
                                  title_text=rtl("מטריקות מלאות"),
                                  vertical_layout=True) for fi in range(36)]
    save_seq(bar_seq, out9 / "anim_metrics")

    flow_v_seq = [render_flow_v_frame(1080, 1920, 40, 220, 480, 1100, fi, 36)
                   for fi in range(36)]
    save_seq(flow_v_seq, out9 / "anim_flow")

    # 16:9 — bars in left half (1080x720), flow horizontal
    out16 = EDIT / "cards_v6_16x9"
    out16.mkdir(parents=True, exist_ok=True)
    bar_seq_h = [render_bars_frame(1920, 1080, area=(60, 100, 1080, 800),
                                    fi=fi, total_frames=36,
                                    title_text=rtl("מטריקות מלאות"),
                                    vertical_layout=False) for fi in range(36)]
    save_seq(bar_seq_h, out16 / "anim_metrics")

    flow_h_seq = [render_flow_h_frame(1920, 1080, 60, 100, 1080, 660, fi, 36)
                   for fi in range(36)]
    save_seq(flow_h_seq, out16 / "anim_flow")

    for d in [out9 / "anim_metrics", out9 / "anim_flow",
              out16 / "anim_metrics", out16 / "anim_flow"]:
        n = len(list(d.glob("*.png")))
        print(f"  {d.relative_to(EDIT)}: {n} frames")


if __name__ == "__main__":
    main()
