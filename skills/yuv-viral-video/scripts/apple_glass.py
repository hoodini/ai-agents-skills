"""Shared Apple-style glass card primitives + dark-mode background + speaker
PIP card helpers.

apple_glass_card(W, H, x, y, w, h, radius, content_fn) -> RGBA Image
make_glass_mask(W, H, x, y, w, h, radius) -> "L" (grayscale) Image
make_pip_mask_local(pip_w, pip_h, radius) -> "L" mask sized to PIP itself
make_dark_bg(W, H, speaker_box=None) -> RGBA Image
    Solid dark modern gradient + optional soft shadow rendered at speaker_box position.
draw_text_safe(img, xy, text, font, ...)
"""
from __future__ import annotations
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont


def blank(w, h):
    return Image.new("RGBA", (w, h), (0, 0, 0, 0))


def apple_glass_card(W, H, x, y, w, h, radius=52, content_fn=None,
                     tint=(255, 255, 255, 38), border_alpha=110,
                     shadow_alpha=170, highlight_alpha=80):
    """Render an Apple-style glass card on a transparent WxH canvas."""
    img = blank(W, H)

    # 1. Drop shadow
    sl = blank(W, H)
    sd = ImageDraw.Draw(sl)
    sd.rounded_rectangle([x + 4, y + 14, x + w + 4, y + h + 14],
                         radius=radius, fill=(0, 0, 0, shadow_alpha))
    sl = sl.filter(ImageFilter.GaussianBlur(radius=24))
    img = Image.alpha_composite(img, sl)

    # 2. Body — translucent white tint
    body = blank(W, H)
    bd = ImageDraw.Draw(body)
    bd.rounded_rectangle([x, y, x + w, y + h], radius=radius, fill=tint)
    img = Image.alpha_composite(img, body)

    # 3. Top inner highlight
    hl = blank(W, H)
    hd = ImageDraw.Draw(hl)
    grad_h = int(h * 0.45)
    for i in range(grad_h):
        t = i / grad_h
        a = int(highlight_alpha * (1 - t) ** 1.6)
        if a <= 0:
            continue
        hd.line([(x + 2, y + i + 1), (x + w - 2, y + i + 1)],
                fill=(255, 255, 255, a))
    # clip the highlight to the card's rounded shape (a linear inset left chamfered corners)
    clip = Image.new("L", (W, H), 0)
    ImageDraw.Draw(clip).rounded_rectangle([x + 1, y + 1, x + w - 1, y + h - 1],
                                           radius=max(0, radius - 1), fill=255)
    hl.putalpha(ImageChops.multiply(hl.getchannel("A"), clip))
    img = Image.alpha_composite(img, hl)

    # 4. Inner border
    bb = blank(W, H)
    brd = ImageDraw.Draw(bb)
    brd.rounded_rectangle([x, y, x + w, y + h], radius=radius,
                          outline=(255, 255, 255, border_alpha), width=2)
    img = Image.alpha_composite(img, bb)

    if content_fn is not None:
        content = content_fn(W, H, x, y, w, h)
        img = Image.alpha_composite(img, content)

    return img


def make_glass_mask(W, H, x, y, w, h, radius=52):
    mask = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(mask)
    d.rounded_rectangle([x, y, x + w, y + h], radius=radius, fill=255)
    return mask


def make_pip_mask_local(pip_w, pip_h, radius=44):
    mask = Image.new("L", (pip_w, pip_h), 0)
    d = ImageDraw.Draw(mask)
    d.rounded_rectangle([0, 0, pip_w, pip_h], radius=radius, fill=255)
    return mask


def make_dark_bg(W, H, speaker_box=None):
    """Solid dark gradient background + soft drop shadow at speaker_box.
    speaker_box = (x, y, w, h, radius) or None.
    """
    bg = Image.new("RGB", (W, H), (14, 13, 42))
    # Smooth top-left to bottom-right gradient
    grad = Image.new("RGB", (W, H), (14, 13, 42))
    pixels = grad.load()
    for y in range(H):
        for x in range(W):
            t = (x / W + y / H) / 2
            # Phoenix Ink night sky: #15133C (top-left) -> #0A0922 (bottom-right)
            r = int(10 + 11 * (1 - t))
            g = int(9 + 10 * (1 - t))
            b = int(34 + 26 * (1 - t))
            pixels[x, y] = (r, g, b)
    bg = grad.convert("RGBA")

    # Subtle vignette (darker near edges)
    vig_mask = Image.new("L", (W, H), 0)
    vd = ImageDraw.Draw(vig_mask)
    vd.ellipse([-W // 3, -H // 3, W + W // 3, H + H // 3], fill=255)
    vig_mask = vig_mask.filter(ImageFilter.GaussianBlur(radius=120))
    # Invert so edges are dark, center is transparent
    inverted = vig_mask.point(lambda v: max(0, 90 - int(v * 0.35)))
    edge = Image.new("RGBA", (W, H), (5, 4, 20, 255))
    edge.putalpha(inverted)
    bg = Image.alpha_composite(bg, edge)

    # Soft drop shadow under the speaker box
    if speaker_box is not None:
        sx, sy, sw, sh, sr = speaker_box
        sh_img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        sd = ImageDraw.Draw(sh_img)
        sd.rounded_rectangle([sx + 6, sy + 22, sx + sw + 6, sy + sh + 22],
                             radius=sr, fill=(0, 0, 0, 200))
        sh_img = sh_img.filter(ImageFilter.GaussianBlur(radius=36))
        bg = Image.alpha_composite(bg, sh_img)

    return bg


def draw_text_safe(img, xy, text, font, fill=(255, 255, 255, 255),
                   stroke=None, stroke_w=0, anchor="mm"):
    d = ImageDraw.Draw(img)
    kw = dict(anchor=anchor, fill=fill)
    if stroke and stroke_w:
        kw["stroke_fill"] = stroke
        kw["stroke_width"] = stroke_w
    d.text(xy, text, font=font, **kw)


# Standard radii
RAD_BANNER = 36
RAD_CARD   = 52
RAD_PIP    = 56  # bigger for speaker frame

# Brand color reference. YUV.AI colours come from yuv-design-system (Phoenix Ink):
# pink #FF2EA0, gold #FFD66E ("yellow" is kept as an alias), violet #8B6CFF, night #0E0D2A.
# Third-party brand colours (facebook, whatsapp, claude...) stay as their owners define them.
COLORS = {
    "gold":      (255, 214, 110),
    "facebook":  (24, 119, 242),
    "instagram": (228, 64, 95),
    "whatsapp":  (37, 211, 102),
    "claude":    (215, 121, 70),
    "anthropic": (215, 121, 70),
    "yellow":    (255, 214, 110),
    "pink":      (255, 46, 160),
    "green":     (37, 211, 102),
    "red":       (255, 80, 80),
    "blue":      (90, 170, 255),
    "purple":    (139, 108, 255),
    "bg_dark":   (14, 13, 42),
    "bone":      (255, 255, 255),
}


# Speaker box specs (right-half placement)
SPEAKER_9X16 = {"x": 560, "y": 460, "w": 480, "h": 880, "radius": 56}
SPEAKER_16X9 = {"x": 1300, "y": 90,  "w": 540, "h": 900, "radius": 56}

# Bottom key-moment strip specs
KEY_STRIP_9X16 = {"x": 40,  "y": 1170, "w": 1000, "h": 110, "radius": 36}
KEY_STRIP_16X9 = {"x": 40,  "y": 920,  "w": 1840, "h": 130, "radius": 36}

# Left-half content area (for cards and animations)
LEFT_CONTENT_9X16 = {"x": 40, "y": 80,  "w": 480, "h": 1620}
LEFT_CONTENT_16X9 = {"x": 40, "y": 80,  "w": 1100, "h": 820}
