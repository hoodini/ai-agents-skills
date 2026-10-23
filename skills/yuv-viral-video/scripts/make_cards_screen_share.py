"""V6 cards for 0423 — Apple-glass cards on LEFT HALF (right half has speaker).
Content audited against the actual transcript: NO fake values, NO 'לינק בביו',
NO 'בלי ידיים'. Only what Yuval actually said in the video.

Card real estate per aspect:
  9:16 (1080x1920): left content area x=40-540, y=80-1500
                    bottom key-moment x=40-1040, y=1730-1880 (full width)
  16:9 (1920x1080): left content area x=40-1100, y=80-820
                    bottom key-moment x=40-1880, y=920-1050 (full width)
"""
from __future__ import annotations
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys

sys.path.insert(0, r"C:\Users\User\Desktop\edit")
from apple_glass import (
    blank, apple_glass_card, make_glass_mask,
    draw_text_safe as t_text, RAD_BANNER, RAD_CARD, RAD_PIP, COLORS,
    LEFT_CONTENT_9X16, LEFT_CONTENT_16X9,
    KEY_STRIP_9X16, KEY_STRIP_16X9,
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


def fill(d, x, y, w, h, color):
    d.rectangle([x, y, x + w, y + h], fill=color)


def round_fill(d, x, y, w, h, color, radius=20):
    d.rounded_rectangle([x, y, x + w, y + h], radius=radius, fill=color)


def brand_icon(W, H, cx, cy, size, color, letter, font):
    img = blank(W, H)
    glow = blank(W, H)
    gd = ImageDraw.Draw(glow)
    gd.ellipse([cx - size, cy - size, cx + size, cy + size], fill=color + (140,))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=size // 4))
    img = Image.alpha_composite(img, glow)
    d2 = ImageDraw.Draw(img)
    d2.ellipse([cx - size // 2, cy - size // 2, cx + size // 2, cy + size // 2],
               fill=color + (255,), outline=(255, 255, 255, 220), width=3)
    t_text(img, (cx, cy + 2), letter, font, fill=(255, 255, 255, 255),
           stroke=(0, 0, 0, 200), stroke_w=3)
    return img


def _key_moment_card_9x16(W, H, label_he, label_en):
    """Bottom-strip key-moment card for 9:16 (full width)."""
    k = KEY_STRIP_9X16
    def content(W, H, x, y, w, h):
        c = blank(W, H)
        f_en = ImageFont.truetype(ANTON, 60)
        f_he = ImageFont.truetype(ASSISTANT_XB, 50)
        # English on right, Hebrew on left (visual balance)
        if label_en:
            t_text(c, (x + 200, y + h // 2), label_en, f_en,
                   fill=(255, 214, 110, 255), stroke=(0, 0, 0, 220), stroke_w=3, anchor="lm")
        if label_he:
            t_text(c, (x + w - 60, y + h // 2), rtl(label_he), f_he,
                   fill=(255, 255, 255, 255), stroke=(0, 0, 0, 200), stroke_w=2, anchor="rm")
        # left accent stripe
        d = ImageDraw.Draw(c)
        round_fill(d, x + 30, y + 30, 14, h - 60, (255, 214, 110, 255), radius=7)
        return c
    img = apple_glass_card(W, H, k["x"], k["y"], k["w"], k["h"], k["radius"],
                           tint=(0, 0, 0, 130), content_fn=content)
    mask = make_glass_mask(W, H, k["x"], k["y"], k["w"], k["h"], k["radius"])
    return img, mask


def _key_moment_card_16x9(W, H, label_he, label_en):
    k = KEY_STRIP_16X9
    def content(W, H, x, y, w, h):
        c = blank(W, H)
        f_en = ImageFont.truetype(ANTON, 56)
        f_he = ImageFont.truetype(ASSISTANT_XB, 46)
        if label_en:
            t_text(c, (x + 200, y + h // 2), label_en, f_en,
                   fill=(255, 214, 110, 255), stroke=(0, 0, 0, 220), stroke_w=3, anchor="lm")
        if label_he:
            t_text(c, (x + w - 60, y + h // 2), rtl(label_he), f_he,
                   fill=(255, 255, 255, 255), stroke=(0, 0, 0, 200), stroke_w=2, anchor="rm")
        d = ImageDraw.Draw(c)
        round_fill(d, x + 30, y + 25, 14, h - 50, (255, 214, 110, 255), radius=7)
        return c
    img = apple_glass_card(W, H, k["x"], k["y"], k["w"], k["h"], k["radius"],
                           tint=(0, 0, 0, 130), content_fn=content)
    mask = make_glass_mask(W, H, k["x"], k["y"], k["w"], k["h"], k["radius"])
    return img, mask


def cards_9x16(out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    W, H = 1080, 1920

    # Left half card area: x=40-540, y=80-1500
    LX, LY, LW = 40, 220, 480

    # ---------- REVEAL: META ADS reveal — content actually said ----------
    def reveal_content(W, H, x, y, w, h):
        c = blank(W, H)
        f_lab = ImageFont.truetype(ASSISTANT_B, 30)
        f_title = ImageFont.truetype(ANTON, 96)
        f_he = ImageFont.truetype(ASSISTANT_XB, 44)
        # tagline
        t_text(c, (x + w // 2, y + 80), rtl("סקיל חדש"), f_lab,
               fill=(255, 214, 110, 255))
        # main brand
        t_text(c, (x + w // 2, y + 220), "META", f_title,
               fill=(255, 255, 255, 255), stroke=(0, 0, 0, 220), stroke_w=4)
        t_text(c, (x + w // 2, y + 320), "ADS", f_title,
               fill=(255, 255, 255, 255), stroke=(0, 0, 0, 220), stroke_w=4)
        # accent
        d = ImageDraw.Draw(c)
        round_fill(d, x + w // 2 - 80, y + 410, 160, 8, (255, 214, 110, 255), radius=4)
        # quote
        t_text(c, (x + w // 2, y + 490), rtl("בניתי עם קלוד"), f_he,
               fill=(220, 220, 230, 255))
        return c

    H_R = 600
    img = apple_glass_card(W, H, LX, LY, LW, H_R, RAD_CARD,
                           tint=(255, 255, 255, 32), content_fn=reveal_content)
    img.save(out_dir / "reveal.png")
    make_glass_mask(W, H, LX, LY, LW, H_R, RAD_CARD).save(out_dir / "reveal_mask.png")

    # ---------- PLATFORMS: 3 brand chips stacked vertically ----------
    def platforms_content(W, H, x, y, w, h):
        c = blank(W, H)
        f_lab = ImageFont.truetype(ASSISTANT_B, 30)
        f_en = ImageFont.truetype(ANTON, 50)
        f_he = ImageFont.truetype(ASSISTANT_XB, 36)
        f_letter = ImageFont.truetype(ANTON, 50)
        t_text(c, (x + w // 2, y + 80), rtl("לנהל את הכל"), f_lab,
               fill=(255, 214, 110, 255))
        chips = [
            ("FACEBOOK",  rtl("פייסבוק"),   COLORS["facebook"],  "f"),
            ("INSTAGRAM", rtl("אינסטגרם"),  COLORS["instagram"], "IG"),
            ("WHATSAPP",  rtl("וואטסאפ"),   COLORS["whatsapp"],  "WA"),
        ]
        ch = 130
        gap = 24
        cx_l = x + 30
        chip_w = w - 60
        y0 = y + 160
        for i, (en, he, color, letter) in enumerate(chips):
            cy = y0 + i * (ch + gap)
            d = ImageDraw.Draw(c)
            round_fill(d, cx_l, cy, chip_w, ch, (255, 255, 255, 30), radius=24)
            d.rounded_rectangle([cx_l, cy, cx_l + chip_w, cy + ch],
                                radius=24, outline=(255, 255, 255, 80), width=2)
            icon = brand_icon(W, H, cx_l + 80, cy + ch // 2, 90, color, letter, f_letter)
            c = Image.alpha_composite(c, icon)
            t_text(c, (cx_l + 165, cy + ch // 2 - 8), en, f_en,
                   fill=(255, 255, 255, 255), stroke=(0, 0, 0, 200), stroke_w=2, anchor="lm")
            t_text(c, (cx_l + chip_w - 30, cy + ch // 2 - 8), he, f_he,
                   fill=(220, 220, 230, 255), anchor="rm")
        return c

    H_P = 700
    img = apple_glass_card(W, H, LX, LY, LW, H_P, RAD_CARD,
                           tint=(255, 255, 255, 32), content_fn=platforms_content)
    img.save(out_dir / "platforms.png")
    make_glass_mask(W, H, LX, LY, LW, H_P, RAD_CARD).save(out_dir / "platforms_mask.png")

    # ---------- AUTO: actually-said quote ----------
    def auto_content(W, H, x, y, w, h):
        c = blank(W, H)
        f_lab = ImageFont.truetype(ASSISTANT_B, 30)
        f_en = ImageFont.truetype(ANTON, 90)
        f_he = ImageFont.truetype(ASSISTANT_XB, 40)
        t_text(c, (x + w // 2, y + 80), rtl("משימות מתוזמנות"), f_lab,
               fill=(255, 214, 110, 255))
        t_text(c, (x + w // 2, y + 220), "AUTO", f_en,
               fill=(255, 214, 110, 255), stroke=(0, 0, 0, 220), stroke_w=4)
        t_text(c, (x + w // 2, y + 320), "IMPROVE", f_en,
               fill=(255, 214, 110, 255), stroke=(0, 0, 0, 220), stroke_w=4)
        d = ImageDraw.Draw(c)
        round_fill(d, x + w // 2 - 100, y + 410, 200, 8, (255, 214, 110, 255), radius=4)
        t_text(c, (x + w // 2, y + 490), rtl("תוך כדי ריצה"), f_he,
               fill=(255, 255, 255, 255))
        return c

    H_A = 600
    img = apple_glass_card(W, H, LX, LY, LW, H_A, RAD_CARD,
                           tint=(0, 0, 0, 130), content_fn=auto_content)
    img.save(out_dir / "auto.png")
    make_glass_mask(W, H, LX, LY, LW, H_A, RAD_CARD).save(out_dir / "auto_mask.png")

    # ---------- WOW stamp (no glass — direct overlay) ----------
    img = blank(W, H)
    halo = blank(W, H)
    dh = ImageDraw.Draw(halo)
    dh.ellipse([LX - 20, 800, LX + LW + 20, 1200], fill=(255, 90, 0, 200))
    halo = halo.filter(ImageFilter.GaussianBlur(radius=80))
    img = Image.alpha_composite(img, halo)
    f_huge = ImageFont.truetype(KARANTINA, int((220) * 1.25))
    t_text(img, (LX + LW // 2, 1000), rtl("מטורף"), f_huge,
           fill=(255, 214, 110, 255), stroke=(0, 0, 0, 255), stroke_w=10)
    img.save(out_dir / "wow.png")

    # ---------- CTA: actual quote ----------
    def cta_content(W, H, x, y, w, h):
        c = blank(W, H)
        f_lab = ImageFont.truetype(ASSISTANT_B, 30)
        f_he_big = ImageFont.truetype(KARANTINA, int((80) * 1.25))
        f_en = ImageFont.truetype(ANTON, 84)
        d = ImageDraw.Draw(c)
        # pink pill header
        round_fill(d, x + 30, y + 60, w - 60, 130, COLORS["pink"] + (255,), radius=65)
        t_text(c, (x + w // 2, y + 125), rtl("טירוף"), f_he_big,
               fill=(255, 255, 255, 255), stroke=(0, 0, 0, 220), stroke_w=4)
        # body
        t_text(c, (x + w // 2, y + 280), "META ADS", f_en,
               fill=(255, 214, 110, 255), stroke=(0, 0, 0, 220), stroke_w=4)
        round_fill(d, x + w // 2 - 80, y + 350, 160, 6, (255, 214, 110, 255), radius=3)
        f_sub = ImageFont.truetype(ASSISTANT_XB, 36)
        t_text(c, (x + w // 2, y + 430), rtl("מה שעושים במשרדי פרסום"), f_sub,
               fill=(220, 220, 230, 255))
        return c

    H_C = 540
    img = apple_glass_card(W, H, LX, LY, LW, H_C, RAD_CARD,
                           tint=(0, 0, 0, 130), content_fn=cta_content)
    img.save(out_dir / "cta.png")
    make_glass_mask(W, H, LX, LY, LW, H_C, RAD_CARD).save(out_dir / "cta_mask.png")

    # ---------- KEY-MOMENT BOTTOM STRIPS ----------
    for name, he, en in [
        ("km_hook",      "דבר גדול",            "BIG THING"),
        ("km_reveal",    "סקיל חדש",            "META ADS"),
        ("km_metrics",   "מטריקות מלאות",       "ALL METRICS"),
        ("km_auto",      "אוטומטית",            "AUTOMATIC"),
        ("km_nano",      "ננו בננה",            "NANO BANANA"),
        ("km_wow",       "מטורף",               ""),
        ("km_cta",       "טירוף",               ""),
    ]:
        img, mask = _key_moment_card_9x16(W, H, he, en)
        img.save(out_dir / f"{name}.png")
        mask.save(out_dir / f"{name}_mask.png")


def cards_16x9(out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    W, H = 1920, 1080
    # Left half: x=40-1100, y=80-820 (1060 wide × 740 tall)
    LX, LY, LW = 60, 100, 1080

    # ---------- REVEAL ----------
    def reveal_content(W, H, x, y, w, h):
        c = blank(W, H)
        f_lab = ImageFont.truetype(ASSISTANT_B, 30)
        f_title = ImageFont.truetype(ANTON, 130)
        f_he = ImageFont.truetype(ASSISTANT_XB, 50)
        t_text(c, (x + w // 2, y + 70), rtl("סקיל חדש"), f_lab, fill=(255, 214, 110, 255))
        t_text(c, (x + w // 2, y + 230), "META ADS", f_title,
               fill=(255, 255, 255, 255), stroke=(0, 0, 0, 220), stroke_w=5)
        d = ImageDraw.Draw(c)
        round_fill(d, x + w // 2 - 100, y + 310, 200, 8, (255, 214, 110, 255), radius=4)
        t_text(c, (x + w // 2, y + 390), rtl("בניתי עם קלוד"), f_he,
               fill=(220, 220, 230, 255))
        return c

    H_R = 500
    img = apple_glass_card(W, H, LX, LY, LW, H_R, RAD_CARD,
                           tint=(255, 255, 255, 32), content_fn=reveal_content)
    img.save(out_dir / "reveal.png")
    make_glass_mask(W, H, LX, LY, LW, H_R, RAD_CARD).save(out_dir / "reveal_mask.png")

    # ---------- PLATFORMS ----------
    def platforms_content(W, H, x, y, w, h):
        c = blank(W, H)
        f_lab = ImageFont.truetype(ASSISTANT_B, 32)
        f_en = ImageFont.truetype(ANTON, 60)
        f_he = ImageFont.truetype(ASSISTANT_XB, 40)
        f_letter = ImageFont.truetype(ANTON, 56)
        t_text(c, (x + w // 2, y + 60), rtl("לנהל את הכל"), f_lab, fill=(255, 214, 110, 255))
        chips = [
            ("FACEBOOK",  rtl("פייסבוק"),   COLORS["facebook"],  "f"),
            ("INSTAGRAM", rtl("אינסטגרם"),  COLORS["instagram"], "IG"),
            ("WHATSAPP",  rtl("וואטסאפ"),   COLORS["whatsapp"],  "WA"),
        ]
        ch = 130
        gap = 20
        cx_l = x + 40
        chip_w = w - 80
        y0 = y + 130
        for i, (en, he, color, letter) in enumerate(chips):
            cy = y0 + i * (ch + gap)
            d = ImageDraw.Draw(c)
            round_fill(d, cx_l, cy, chip_w, ch, (255, 255, 255, 30), radius=24)
            d.rounded_rectangle([cx_l, cy, cx_l + chip_w, cy + ch],
                                radius=24, outline=(255, 255, 255, 80), width=2)
            icon = brand_icon(W, H, cx_l + 90, cy + ch // 2, 96, color, letter, f_letter)
            c = Image.alpha_composite(c, icon)
            t_text(c, (cx_l + 200, cy + ch // 2 - 6), en, f_en,
                   fill=(255, 255, 255, 255), stroke=(0, 0, 0, 200), stroke_w=2, anchor="lm")
            t_text(c, (cx_l + chip_w - 50, cy + ch // 2 - 6), he, f_he,
                   fill=(220, 220, 230, 255), anchor="rm")
        return c

    H_P = 660
    img = apple_glass_card(W, H, LX, LY, LW, H_P, RAD_CARD,
                           tint=(255, 255, 255, 32), content_fn=platforms_content)
    img.save(out_dir / "platforms.png")
    make_glass_mask(W, H, LX, LY, LW, H_P, RAD_CARD).save(out_dir / "platforms_mask.png")

    # ---------- AUTO ----------
    def auto_content(W, H, x, y, w, h):
        c = blank(W, H)
        f_lab = ImageFont.truetype(ASSISTANT_B, 30)
        f_en = ImageFont.truetype(ANTON, 130)
        f_he = ImageFont.truetype(ASSISTANT_XB, 50)
        t_text(c, (x + w // 2, y + 60), rtl("משימות מתוזמנות"), f_lab, fill=(255, 214, 110, 255))
        t_text(c, (x + w // 2, y + 230), "AUTO-IMPROVE", f_en,
               fill=(255, 214, 110, 255), stroke=(0, 0, 0, 220), stroke_w=5)
        d = ImageDraw.Draw(c)
        round_fill(d, x + w // 2 - 120, y + 320, 240, 8, (255, 214, 110, 255), radius=4)
        t_text(c, (x + w // 2, y + 400), rtl("תוך כדי ריצה"), f_he, fill=(255, 255, 255, 255))
        return c

    H_A = 510
    img = apple_glass_card(W, H, LX, LY, LW, H_A, RAD_CARD,
                           tint=(0, 0, 0, 130), content_fn=auto_content)
    img.save(out_dir / "auto.png")
    make_glass_mask(W, H, LX, LY, LW, H_A, RAD_CARD).save(out_dir / "auto_mask.png")

    # ---------- WOW ----------
    img = blank(W, H)
    halo = blank(W, H)
    dh = ImageDraw.Draw(halo)
    cxw, cyw = 600, 540
    dh.ellipse([cxw - 700, cyw - 280, cxw + 700, cyw + 280], fill=(255, 90, 0, 200))
    halo = halo.filter(ImageFilter.GaussianBlur(radius=80))
    img = Image.alpha_composite(img, halo)
    f_huge = ImageFont.truetype(KARANTINA, int((240) * 1.25))
    t_text(img, (cxw, cyw), rtl("מטורף"), f_huge,
           fill=(255, 214, 110, 255), stroke=(0, 0, 0, 255), stroke_w=10)
    img.save(out_dir / "wow.png")

    # ---------- CTA ----------
    def cta_content(W, H, x, y, w, h):
        c = blank(W, H)
        d = ImageDraw.Draw(c)
        f_he_big = ImageFont.truetype(KARANTINA, int((100) * 1.25))
        f_en = ImageFont.truetype(ANTON, 100)
        f_sub = ImageFont.truetype(ASSISTANT_XB, 40)
        round_fill(d, x + 60, y + 60, w - 120, 150, COLORS["pink"] + (255,), radius=75)
        t_text(c, (x + w // 2, y + 140), rtl("טירוף"), f_he_big,
               fill=(255, 255, 255, 255), stroke=(0, 0, 0, 220), stroke_w=4)
        t_text(c, (x + w // 2, y + 290), "META ADS", f_en,
               fill=(255, 214, 110, 255), stroke=(0, 0, 0, 220), stroke_w=4)
        round_fill(d, x + w // 2 - 100, y + 370, 200, 6, (255, 214, 110, 255), radius=3)
        t_text(c, (x + w // 2, y + 450), rtl("מה שעושים במשרדי פרסום"), f_sub,
               fill=(220, 220, 230, 255))
        return c

    H_C = 540
    img = apple_glass_card(W, H, LX, LY, LW, H_C, RAD_CARD,
                           tint=(0, 0, 0, 130), content_fn=cta_content)
    img.save(out_dir / "cta.png")
    make_glass_mask(W, H, LX, LY, LW, H_C, RAD_CARD).save(out_dir / "cta_mask.png")

    # KEY-MOMENT BOTTOM STRIPS
    for name, he, en in [
        ("km_hook",      "דבר גדול",            "BIG THING"),
        ("km_reveal",    "סקיל חדש",            "META ADS"),
        ("km_metrics",   "מטריקות מלאות",       "ALL METRICS"),
        ("km_auto",      "אוטומטית",            "AUTOMATIC"),
        ("km_nano",      "ננו בננה",            "NANO BANANA"),
        ("km_wow",       "מטורף",               ""),
        ("km_cta",       "טירוף",               ""),
    ]:
        img, mask = _key_moment_card_16x9(W, H, he, en)
        img.save(out_dir / f"{name}.png")
        mask.save(out_dir / f"{name}_mask.png")


def main():
    cards_9x16(EDIT / "cards_v6_9x16")
    cards_16x9(EDIT / "cards_v6_16x9")
    for d in [EDIT / "cards_v6_9x16", EDIT / "cards_v6_16x9"]:
        n = len(list(d.glob("*.png")))
        print(f"  {d.name}: {n} files")


if __name__ == "__main__":
    main()
