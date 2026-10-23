"""V6 cards for tt.mp4 — TOP BANNER layout for 9:16 (above face) so the
speaker's face is never covered. 16:9 keeps left-half placement (cards
sit on the blurred BG, not over the speaker).

Content audited against transcript: NO 'עצור', NO '$$$', NO 'ביי שירותי תשלום',
NO 'ב-0 שקלים', NO '100% הבנה'. Only what was actually said.

Avatar font fix: Hebrew letters use KARANTINA not Anton.
"""
from __future__ import annotations
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys

sys.path.insert(0, r"C:\Users\User\Desktop\edit")
from apple_glass import (
    blank, apple_glass_card, make_glass_mask,
    draw_text_safe as t_text, RAD_BANNER, RAD_CARD, RAD_PIP, COLORS,
    KEY_STRIP_16X9,
)
from bidi import get_display


def rtl(s):
    return get_display(s)


EDIT = Path(r"C:\Users\User\Downloads\tt_edit")
FONTS = Path(r"C:\Users\User\Desktop\edit\fonts")
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


# Bottom strip for tt.mp4 9:16 — moved BELOW speaker (very bottom)
BOTTOM_STRIP_9X16 = {"x": 40, "y": 1750, "w": 1000, "h": 130, "radius": 36}


def _key_card_9x16(W, H, label_he, label_en):
    k = BOTTOM_STRIP_9X16
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


def _key_card_16x9(W, H, label_he, label_en):
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


# ====================== 9:16 — TOP-BANNER LAYOUT ======================
def cards_9x16(out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    W, H = 1080, 1920
    # Top banner area: x=40-1040 (1000 wide), y=80-450 (370 tall) — above face
    BX, BY, BW = 40, 80, 1000

    # ---- HOOK ----
    def hook_content(W, H, x, y, w, h):
        c = blank(W, H)
        d = ImageDraw.Draw(c)
        f_huge = ImageFont.truetype(KARANTINA, int((130) * 1.25))
        f_sub = ImageFont.truetype(ASSISTANT_B, 50)
        f_lab = ImageFont.truetype(ASSISTANT_B, 28)
        t_text(c, (x + w // 2, y + 50), rtl("לא צריך לשלם!"), f_lab, fill=(255, 214, 110, 255))
        round_fill(d, x + 60, y + 100, w - 120, 150, (255, 214, 110, 255), radius=44)
        t_text(c, (x + w // 2, y + 175), rtl("די לשלם"), f_huge,
               fill=(0, 0, 0, 255))
        round_fill(d, x + 60, y + 270, w - 120, 70, (0, 0, 0, 255), radius=24)
        t_text(c, (x + w // 2, y + 305), rtl("יש קלאוד דסקטופ"), f_sub,
               fill=(255, 214, 110, 255))
        return c

    H_HK = 370
    img = apple_glass_card(W, H, BX, BY, BW, H_HK, RAD_CARD,
                           tint=(0, 0, 0, 130), content_fn=hook_content)
    img.save(out_dir / "hook.png")
    make_glass_mask(W, H, BX, BY, BW, H_HK, RAD_CARD).save(out_dir / "hook_mask.png")

    # ---- WORKSHOP ----
    def workshop_content(W, H, x, y, w, h):
        c = blank(W, H)
        d = ImageDraw.Draw(c)
        f_lab = ImageFont.truetype(ASSISTANT_B, 26)
        f_title = ImageFont.truetype(KARANTINA, int((50) * 1.25))
        f_val = ImageFont.truetype(ANTON, 80)
        f_he = ImageFont.truetype(ASSISTANT_XB, 30)
        t_text(c, (x + w // 2, y + 35), rtl("אתמול בסדנה"), f_lab, fill=(255, 214, 110, 255))
        t_text(c, (x + w // 2, y + 100), rtl("רייכמן"), f_title,
               fill=(255, 255, 255, 255), stroke=(0, 0, 0, 200), stroke_w=2)
        # Stats: real values from transcript only
        stats = [
            ("3", rtl("שעות"),       (255, 214, 110)),
            ("0", rtl("ידע קודם"),    COLORS["blue"]),
        ]
        cell_w = (w - 60) // 2
        cy = y + 180
        cell_h = 170
        for i, (val, lab, color) in enumerate(stats):
            cx = x + 30 + i * cell_w
            round_fill(d, cx + 12, cy, cell_w - 24, cell_h, color + (60,), radius=22)
            d.rounded_rectangle([cx + 12, cy, cx + cell_w - 12, cy + cell_h],
                                radius=22, outline=color + (200,), width=3)
            t_text(c, (cx + cell_w // 2, cy + 70), val, f_val,
                   fill=color + (255,), stroke=(0, 0, 0, 220), stroke_w=3)
            t_text(c, (cx + cell_w // 2, cy + 140), lab, f_he, fill=(255, 255, 255, 255))
        return c

    H_WS = 380
    img = apple_glass_card(W, H, BX, BY, BW, H_WS, RAD_CARD,
                           tint=(255, 255, 255, 30), content_fn=workshop_content)
    img.save(out_dir / "workshop.png")
    make_glass_mask(W, H, BX, BY, BW, H_WS, RAD_CARD).save(out_dir / "workshop_mask.png")

    # ---- STUDENT (avatar uses KARANTINA, not Anton, for Hebrew letter) ----
    def student_content(W, H, x, y, w, h):
        c = blank(W, H)
        d = ImageDraw.Draw(c)
        f_lab = ImageFont.truetype(ASSISTANT_B, 26)
        f_name = ImageFont.truetype(KARANTINA, int((80) * 1.25))
        f_role = ImageFont.truetype(ASSISTANT_XB, 36)
        f_quote = ImageFont.truetype(ASSISTANT_XB, 32)
        f_letter = ImageFont.truetype(KARANTINA, int((64) * 1.25))  # Karantina supports Hebrew
        t_text(c, (x + w // 2, y + 35), rtl("בסוף הסדנה"), f_lab, fill=(255, 214, 110, 255))
        # Avatar (left side) + name+role (right side)
        avatar = brand_icon(W, H, x + 130, y + 200, 110, COLORS["pink"], rtl("א"), f_letter)
        c = Image.alpha_composite(c, avatar)
        d = ImageDraw.Draw(c)
        t_text(c, (x + w - 80, y + 130), rtl("אריאל"), f_name,
               fill=(255, 255, 255, 255), stroke=(0, 0, 0, 200), stroke_w=3, anchor="rm")
        t_text(c, (x + w - 80, y + 200), rtl("סטודנטית"), f_role,
               fill=(220, 220, 230, 255), anchor="rm")
        # quote
        round_fill(d, x + 60, y + 280, w - 120, 70, (255, 255, 255, 30), radius=24)
        d.rounded_rectangle([x + 60, y + 280, x + w - 60, y + 350],
                            radius=24, outline=(255, 255, 255, 100), width=2)
        t_text(c, (x + w // 2, y + 315), rtl("משתמשת בגרמרלי"), f_quote,
               fill=(255, 255, 255, 255))
        return c

    H_ST = 380
    img = apple_glass_card(W, H, BX, BY, BW, H_ST, RAD_CARD,
                           tint=(255, 255, 255, 30), content_fn=student_content)
    img.save(out_dir / "student.png")
    make_glass_mask(W, H, BX, BY, BW, H_ST, RAD_CARD).save(out_dir / "student_mask.png")

    # ---- BUILD_15MIN ----
    def build_content(W, H, x, y, w, h):
        c = blank(W, H)
        d = ImageDraw.Draw(c)
        f_huge = ImageFont.truetype(ANTON, 200)
        f_lab = ImageFont.truetype(ASSISTANT_B, 26)
        f_he = ImageFont.truetype(ASSISTANT_XB, 40)
        t_text(c, (x + w // 2, y + 35), rtl("רבע שעה"), f_lab, fill=(255, 214, 110, 255))
        t_text(c, (x + w // 2, y + 175), "15:00", f_huge,
               fill=(255, 214, 110, 255), stroke=(0, 0, 0, 220), stroke_w=8)
        round_fill(d, x + w // 2 - 100, y + 290, 200, 6, (255, 214, 110, 255), radius=3)
        t_text(c, (x + w // 2, y + 340), rtl("עבד"), f_he,
               fill=(255, 255, 255, 255))
        return c

    H_BL = 380
    img = apple_glass_card(W, H, BX, BY, BW, H_BL, RAD_CARD,
                           tint=(0, 0, 0, 140), content_fn=build_content)
    img.save(out_dir / "build_15min.png")
    make_glass_mask(W, H, BX, BY, BW, H_BL, RAD_CARD).save(out_dir / "build_15min_mask.png")

    # ---- RESULT ----
    def result_content(W, H, x, y, w, h):
        c = blank(W, H)
        d = ImageDraw.Draw(c)
        f_en = ImageFont.truetype(ANTON, 84)
        f_he = ImageFont.truetype(ASSISTANT_XB, 38)
        f_lab = ImageFont.truetype(ASSISTANT_B, 26)
        round_fill(d, x + 60, y + 35, w - 120, 8, COLORS["blue"] + (255,), radius=4)
        t_text(c, (x + w // 2, y + 75), rtl("התוצאה"), f_lab, fill=COLORS["blue"] + (255,))
        t_text(c, (x + w // 2, y + 165), "WINDOWS APP", f_en,
               fill=(255, 255, 255, 255), stroke=(0, 0, 0, 220), stroke_w=4)
        round_fill(d, x + w // 2 - 90, y + 230, 180, 6, COLORS["blue"] + (255,), radius=3)
        t_text(c, (x + w // 2, y + 285), rtl("מתקנת שגיאות באנגלית"), f_he,
               fill=(220, 230, 255, 255))
        return c

    H_RS = 360
    img = apple_glass_card(W, H, BX, BY, BW, H_RS, RAD_CARD,
                           tint=(255, 255, 255, 30), content_fn=result_content)
    img.save(out_dir / "result.png")
    make_glass_mask(W, H, BX, BY, BW, H_RS, RAD_CARD).save(out_dir / "result_mask.png")

    # ---- NO_PAY ----
    def nopay_content(W, H, x, y, w, h):
        c = blank(W, H)
        d = ImageDraw.Draw(c)
        f_big = ImageFont.truetype(ANTON, 120)
        f_he = ImageFont.truetype(ASSISTANT_XB, 40)
        f_lab = ImageFont.truetype(ASSISTANT_B, 26)
        round_fill(d, x + 60, y + 35, w - 120, 8, (255, 80, 80, 255), radius=4)
        t_text(c, (x + w // 2, y + 75), rtl("לא צריך לשלם"), f_lab, fill=(255, 80, 80, 255))
        t_text(c, (x + w // 2, y + 200), "GRAMMARLY", f_big,
               fill=(255, 255, 255, 255), stroke=(0, 0, 0, 220), stroke_w=4)
        round_fill(d, x + 130, y + 195, w - 260, 10, (255, 80, 80, 255), radius=5)
        t_text(c, (x + w // 2, y + 310), rtl("גם לא לצד ג'"), f_he, fill=(220, 220, 230, 255))
        return c

    H_NP = 380
    img = apple_glass_card(W, H, BX, BY, BW, H_NP, RAD_CARD,
                           tint=(60, 10, 10, 160), content_fn=nopay_content)
    img.save(out_dir / "no_pay.png")
    make_glass_mask(W, H, BX, BY, BW, H_NP, RAD_CARD).save(out_dir / "no_pay_mask.png")

    # ---- MAGIC stamp (NOT a glass card — full-frame title) ----
    img = blank(W, H)
    halo = blank(W, H)
    dh = ImageDraw.Draw(halo)
    dh.ellipse([BX - 20, 250, BX + BW + 20, 750], fill=(255, 90, 0, 200))
    halo = halo.filter(ImageFilter.GaussianBlur(radius=80))
    img = Image.alpha_composite(img, halo)
    f_huge = ImageFont.truetype(KARANTINA, int((130) * 1.25))
    t_text(img, (BX + BW // 2, 380), rtl("מצליחים"), f_huge,
           fill=(255, 214, 110, 255), stroke=(0, 0, 0, 255), stroke_w=8)
    t_text(img, (BX + BW // 2, 530), rtl("לעשות הכל"), f_huge,
           fill=(255, 255, 255, 255), stroke=(0, 0, 0, 255), stroke_w=8)
    img.save(out_dir / "magic.png")

    # ---- CTA ----
    def cta_content(W, H, x, y, w, h):
        c = blank(W, H)
        d = ImageDraw.Draw(c)
        f_en = ImageFont.truetype(ANTON, 100)
        f_he = ImageFont.truetype(ASSISTANT_XB, 60)
        round_fill(d, x + 80, y + 60, w - 160, 130, COLORS["pink"] + (255,), radius=65)
        t_text(c, (x + w // 2, y + 130), "AI MINDSET", f_en,
               fill=(255, 255, 255, 255), stroke=(0, 0, 0, 220), stroke_w=4)
        t_text(c, (x + w // 2, y + 260), rtl("יום טוב"), f_he,
               fill=(255, 214, 110, 255), stroke=(0, 0, 0, 200), stroke_w=4)
        return c

    H_CT = 340
    img = apple_glass_card(W, H, BX, BY, BW, H_CT, RAD_CARD,
                           tint=(0, 0, 0, 130), content_fn=cta_content)
    img.save(out_dir / "cta.png")
    make_glass_mask(W, H, BX, BY, BW, H_CT, RAD_CARD).save(out_dir / "cta_mask.png")

    # Bottom key-moment strips at very bottom
    for name, he, en in [
        ("km_hook",     "די לשלם",        ""),
        ("km_workshop", "סדנה ברייכמן",  ""),
        ("km_build",    "רבע שעה",        "15 MIN"),
        ("km_result",   "תוכנה במחשב",   "WINDOWS APP"),
        ("km_nopay",    "בלי לשלם",       ""),
        ("km_magic",    "מצליחים",         ""),
        ("km_cta",      "מיינדסט של AI", "AI MINDSET"),
    ]:
        img, mask = _key_card_9x16(W, H, he, en)
        img.save(out_dir / f"{name}.png")
        mask.save(out_dir / f"{name}_mask.png")


# ====================== 16:9 — LEFT-HALF (unchanged from v4) ======================
def cards_16x9(out_dir):
    """For 16:9, the speaker is letterboxed centered (607x1080) with blurred BG.
    Cards on left half (x=60-1140) sit on the blurred BG, NOT over the speaker."""
    out_dir.mkdir(parents=True, exist_ok=True)
    W, H = 1920, 1080
    LX, LY, LW = 60, 100, 1080

    # HOOK
    def hook_content(W, H, x, y, w, h):
        c = blank(W, H)
        d = ImageDraw.Draw(c)
        f_huge = ImageFont.truetype(KARANTINA, int((160) * 1.25))
        f_sub = ImageFont.truetype(ASSISTANT_B, 56)
        f_lab = ImageFont.truetype(ASSISTANT_B, 30)
        t_text(c, (x + w // 2, y + 60), rtl("לא צריך לשלם!"), f_lab, fill=(255, 214, 110, 255))
        round_fill(d, x + 60, y + 140, w - 120, 240, (255, 214, 110, 255), radius=60)
        t_text(c, (x + w // 2, y + 260), rtl("די לשלם"), f_huge,
               fill=(0, 0, 0, 255))
        round_fill(d, x + 60, y + 410, w - 120, 90, (0, 0, 0, 255), radius=30)
        t_text(c, (x + w // 2, y + 455), rtl("יש קלאוד דסקטופ"), f_sub,
               fill=(255, 214, 110, 255))
        return c

    H_HK = 600
    img = apple_glass_card(W, H, LX, LY, LW, H_HK, RAD_CARD,
                           tint=(0, 0, 0, 100), content_fn=hook_content)
    img.save(out_dir / "hook.png")
    make_glass_mask(W, H, LX, LY, LW, H_HK, RAD_CARD).save(out_dir / "hook_mask.png")

    def workshop_content(W, H, x, y, w, h):
        c = blank(W, H)
        d = ImageDraw.Draw(c)
        f_lab = ImageFont.truetype(ASSISTANT_B, 30)
        f_title = ImageFont.truetype(KARANTINA, int((56) * 1.25))
        f_val = ImageFont.truetype(ANTON, 110)
        f_he = ImageFont.truetype(ASSISTANT_XB, 38)
        t_text(c, (x + w // 2, y + 60), rtl("אתמול בסדנה"), f_lab, fill=(255, 214, 110, 255))
        t_text(c, (x + w // 2, y + 160), rtl("רייכמן"), f_title,
               fill=(255, 255, 255, 255), stroke=(0, 0, 0, 200), stroke_w=2)
        stats = [
            ("3", rtl("שעות"),       (255, 214, 110)),
            ("0", rtl("ידע קודם"),    COLORS["blue"]),
        ]
        cell_w = (w - 60) // 2
        cy = y + 280
        cell_h = 240
        for i, (val, lab, color) in enumerate(stats):
            cx = x + 30 + i * cell_w
            round_fill(d, cx + 12, cy, cell_w - 24, cell_h, color + (60,), radius=24)
            d.rounded_rectangle([cx + 12, cy, cx + cell_w - 12, cy + cell_h],
                                radius=24, outline=color + (200,), width=3)
            t_text(c, (cx + cell_w // 2, cy + 100), val, f_val,
                   fill=color + (255,), stroke=(0, 0, 0, 220), stroke_w=3)
            t_text(c, (cx + cell_w // 2, cy + 200), lab, f_he, fill=(255, 255, 255, 255))
        return c

    H_WS = 600
    img = apple_glass_card(W, H, LX, LY, LW, H_WS, RAD_CARD,
                           tint=(255, 255, 255, 30), content_fn=workshop_content)
    img.save(out_dir / "workshop.png")
    make_glass_mask(W, H, LX, LY, LW, H_WS, RAD_CARD).save(out_dir / "workshop_mask.png")

    def student_content(W, H, x, y, w, h):
        c = blank(W, H)
        d = ImageDraw.Draw(c)
        f_lab = ImageFont.truetype(ASSISTANT_B, 30)
        f_name = ImageFont.truetype(KARANTINA, int((100) * 1.25))
        f_role = ImageFont.truetype(ASSISTANT_XB, 46)
        f_quote = ImageFont.truetype(ASSISTANT_XB, 40)
        f_letter = ImageFont.truetype(KARANTINA, int((80) * 1.25))  # FIXED: Karantina for Hebrew
        t_text(c, (x + w // 2, y + 60), rtl("בסוף הסדנה"), f_lab, fill=(255, 214, 110, 255))
        avatar = brand_icon(W, H, x + w // 2, y + 220, 140, COLORS["pink"], rtl("א"), f_letter)
        c = Image.alpha_composite(c, avatar)
        d = ImageDraw.Draw(c)
        t_text(c, (x + w // 2, y + 340), rtl("אריאל"), f_name,
               fill=(255, 255, 255, 255), stroke=(0, 0, 0, 200), stroke_w=3)
        t_text(c, (x + w // 2, y + 430), rtl("סטודנטית"), f_role,
               fill=(220, 220, 230, 255))
        round_fill(d, x + 200, y + 510, w - 400, 100, (255, 255, 255, 30), radius=28)
        d.rounded_rectangle([x + 200, y + 510, x + w - 200, y + 610],
                            radius=28, outline=(255, 255, 255, 100), width=2)
        t_text(c, (x + w // 2, y + 560), rtl("משתמשת בגרמרלי"), f_quote,
               fill=(255, 255, 255, 255))
        return c

    H_ST = 660
    img = apple_glass_card(W, H, LX, LY, LW, H_ST, RAD_CARD,
                           tint=(255, 255, 255, 30), content_fn=student_content)
    img.save(out_dir / "student.png")
    make_glass_mask(W, H, LX, LY, LW, H_ST, RAD_CARD).save(out_dir / "student_mask.png")

    def build_content(W, H, x, y, w, h):
        c = blank(W, H)
        d = ImageDraw.Draw(c)
        f_huge = ImageFont.truetype(ANTON, 320)
        f_lab = ImageFont.truetype(ASSISTANT_B, 30)
        f_he = ImageFont.truetype(ASSISTANT_XB, 56)
        t_text(c, (x + w // 2, y + 60), rtl("רבע שעה"), f_lab, fill=(255, 214, 110, 255))
        t_text(c, (x + w // 2, y + 280), "15:00", f_huge,
               fill=(255, 214, 110, 255), stroke=(0, 0, 0, 220), stroke_w=10)
        round_fill(d, x + w // 2 - 130, y + 460, 260, 8, (255, 214, 110, 255), radius=4)
        t_text(c, (x + w // 2, y + 540), rtl("עבד"), f_he, fill=(255, 255, 255, 255))
        return c

    H_BL = 620
    img = apple_glass_card(W, H, LX, LY, LW, H_BL, RAD_CARD,
                           tint=(0, 0, 0, 140), content_fn=build_content)
    img.save(out_dir / "build_15min.png")
    make_glass_mask(W, H, LX, LY, LW, H_BL, RAD_CARD).save(out_dir / "build_15min_mask.png")

    def result_content(W, H, x, y, w, h):
        c = blank(W, H)
        d = ImageDraw.Draw(c)
        f_en = ImageFont.truetype(ANTON, 130)
        f_he = ImageFont.truetype(ASSISTANT_XB, 54)
        f_lab = ImageFont.truetype(ASSISTANT_B, 30)
        round_fill(d, x + 60, y + 70, w - 120, 12, COLORS["blue"] + (255,), radius=6)
        t_text(c, (x + w // 2, y + 130), rtl("התוצאה"), f_lab, fill=COLORS["blue"] + (255,))
        t_text(c, (x + w // 2, y + 270), "WINDOWS APP", f_en,
               fill=(255, 255, 255, 255), stroke=(0, 0, 0, 220), stroke_w=4)
        round_fill(d, x + w // 2 - 130, y + 360, 260, 6, COLORS["blue"] + (255,), radius=3)
        t_text(c, (x + w // 2, y + 440), rtl("מתקנת שגיאות באנגלית"), f_he,
               fill=(220, 230, 255, 255))
        return c

    H_RS = 540
    img = apple_glass_card(W, H, LX, LY, LW, H_RS, RAD_CARD,
                           tint=(255, 255, 255, 30), content_fn=result_content)
    img.save(out_dir / "result.png")
    make_glass_mask(W, H, LX, LY, LW, H_RS, RAD_CARD).save(out_dir / "result_mask.png")

    def nopay_content(W, H, x, y, w, h):
        c = blank(W, H)
        d = ImageDraw.Draw(c)
        f_big = ImageFont.truetype(ANTON, 130)
        f_he = ImageFont.truetype(ASSISTANT_XB, 56)
        f_lab = ImageFont.truetype(ASSISTANT_B, 30)
        round_fill(d, x + 60, y + 70, w - 120, 12, (255, 80, 80, 255), radius=6)
        t_text(c, (x + w // 2, y + 130), rtl("לא צריך לשלם"), f_lab, fill=(255, 80, 80, 255))
        t_text(c, (x + w // 2, y + 280), "GRAMMARLY", f_big,
               fill=(255, 255, 255, 255), stroke=(0, 0, 0, 220), stroke_w=5)
        round_fill(d, x + 130, y + 270, w - 260, 12, (255, 80, 80, 255), radius=6)
        t_text(c, (x + w // 2, y + 420), rtl("גם לא לצד ג'"), f_he, fill=(220, 220, 230, 255))
        return c

    H_NP = 540
    img = apple_glass_card(W, H, LX, LY, LW, H_NP, RAD_CARD,
                           tint=(60, 10, 10, 160), content_fn=nopay_content)
    img.save(out_dir / "no_pay.png")
    make_glass_mask(W, H, LX, LY, LW, H_NP, RAD_CARD).save(out_dir / "no_pay_mask.png")

    # MAGIC stamp
    img = blank(W, H)
    halo = blank(W, H)
    dh = ImageDraw.Draw(halo)
    cxw, cyw = 600, 540
    dh.ellipse([cxw - 700, cyw - 280, cxw + 700, cyw + 280], fill=(255, 90, 0, 200))
    halo = halo.filter(ImageFilter.GaussianBlur(radius=80))
    img = Image.alpha_composite(img, halo)
    f_huge = ImageFont.truetype(KARANTINA, int((200) * 1.25))
    t_text(img, (cxw, cyw - 110), rtl("מצליחים"), f_huge,
           fill=(255, 214, 110, 255), stroke=(0, 0, 0, 255), stroke_w=10)
    t_text(img, (cxw, cyw + 110), rtl("לעשות הכל"), f_huge,
           fill=(255, 255, 255, 255), stroke=(0, 0, 0, 255), stroke_w=10)
    img.save(out_dir / "magic.png")

    def cta_content(W, H, x, y, w, h):
        c = blank(W, H)
        d = ImageDraw.Draw(c)
        f_en = ImageFont.truetype(ANTON, 130)
        f_he = ImageFont.truetype(ASSISTANT_XB, 80)
        round_fill(d, x + 60, y + 70, w - 120, 200, COLORS["pink"] + (255,), radius=100)
        t_text(c, (x + w // 2, y + 170), "AI MINDSET", f_en,
               fill=(255, 255, 255, 255), stroke=(0, 0, 0, 220), stroke_w=5)
        t_text(c, (x + w // 2, y + 380), rtl("יום טוב"), f_he,
               fill=(255, 214, 110, 255), stroke=(0, 0, 0, 200), stroke_w=4)
        return c

    H_CT = 480
    img = apple_glass_card(W, H, LX, LY, LW, H_CT, RAD_CARD,
                           tint=(0, 0, 0, 130), content_fn=cta_content)
    img.save(out_dir / "cta.png")
    make_glass_mask(W, H, LX, LY, LW, H_CT, RAD_CARD).save(out_dir / "cta_mask.png")

    for name, he, en in [
        ("km_hook",     "די לשלם",        ""),
        ("km_workshop", "סדנה ברייכמן",  ""),
        ("km_build",    "רבע שעה",        "15 MIN"),
        ("km_result",   "תוכנה במחשב",   "WINDOWS APP"),
        ("km_nopay",    "בלי לשלם",       ""),
        ("km_magic",    "מצליחים",         ""),
        ("km_cta",      "מיינדסט של AI", "AI MINDSET"),
    ]:
        img, mask = _key_card_16x9(W, H, he, en)
        img.save(out_dir / f"{name}.png")
        mask.save(out_dir / f"{name}_mask.png")


def main():
    # Overwrite cards_v4_* (used by composite_v5) so we don't have to update composite paths
    cards_9x16(EDIT / "cards_v4_9x16")
    cards_16x9(EDIT / "cards_v4_16x9")
    for d in [EDIT / "cards_v4_9x16", EDIT / "cards_v4_16x9"]:
        n = len(list(d.glob("*.png")))
        print(f"  {d.name}: {n} files")


if __name__ == "__main__":
    main()
