#!/usr/bin/env python3
"""Render the make.fun 25 November 2026 world-news image.

Magazine-cover style, 1024x1024 PNG, deterministic: no network, no
randomness, no timestamps. Python 3 + Pillow only.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"

# Palette: dark navy + warm amber accent.
NAVY = (11, 29, 51)
NAVY2 = (16, 42, 68)
PANEL = (23, 58, 90)
CARD = (19, 47, 74)
CARD_LINE = (38, 78, 112)
AMBER = (255, 176, 32)
ORANGE = (255, 110, 30)
WHITE = (245, 247, 250)
LIGHT = (203, 216, 230)
MUTED = (148, 168, 190)
SEA = (13, 68, 92)
SEA2 = (10, 52, 74)
SKY = (46, 84, 122)
SKY2 = (30, 62, 96)
SMOKE = (120, 130, 140)
FLAME_Y = (255, 214, 64)
FLAME_O = (255, 140, 40)


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


F_SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
F_BOLD = lambda s: font("DejaVuSans-Bold.ttf", s)
F_REG = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, width):
    """Greedy word wrap measured with the real font."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def draw_tanker_scene(d, x0, y0, x1, y1):
    """Vector tanker at sea in the Strait, flames and smoke. Pillow shapes only."""
    # Sky bands.
    d.rectangle([x0, y0, x1, y0 + 100], fill=SKY2)
    d.rectangle([x0, y0 + 100, x1, y0 + 128], fill=SKY)
    # Low sun.
    d.ellipse([x1 - 140, y0 + 36, x1 - 76, y0 + 100], fill=(255, 190, 90))
    # Sea bands.
    d.rectangle([x0, y0 + 128, x1, y1], fill=SEA)
    d.rectangle([x0, y0 + 128, x1, y0 + 142], fill=SEA2)
    # Distant tanker silhouette (second ship, smaller, far right).
    d.rectangle([x0 + 660, y0 + 108, x0 + 800, y0 + 128], fill=(18, 44, 66))
    d.rectangle([x0 + 712, y0 + 92, x0 + 726, y0 + 108], fill=(18, 44, 66))
    # Main tanker hull.
    hx0, hy0, hx1, hy1 = x0 + 48, y0 + 146, x0 + 560, y0 + 196
    d.polygon([(hx0, hy0), (hx1, hy0), (hx1 - 34, hy1), (hx0 + 44, hy1)],
              fill=(142, 32, 24))
    d.rectangle([hx0, hy0, hx1, hy0 + 12], fill=(90, 22, 18))
    # Deck containers.
    d.rectangle([hx0 + 30, hy0 - 30, hx0 + 120, hy0], fill=(214, 140, 40))
    d.rectangle([hx0 + 130, hy0 - 30, hx0 + 220, hy0], fill=(60, 120, 130))
    d.rectangle([hx0 + 230, hy0 - 30, hx0 + 320, hy0], fill=(214, 140, 40))
    # Bridge tower: dark with amber windows.
    d.rectangle([hx0 + 400, hy0 - 56, hx0 + 462, hy0], fill=(24, 48, 72))
    d.rectangle([hx0 + 408, hy0 - 48, hx0 + 454, hy0 - 34], fill=AMBER)
    # Funnel.
    d.rectangle([hx0 + 332, hy0 - 46, hx0 + 376, hy0], fill=(20, 40, 60))
    # Flames over the deck (two bursts, rising from the containers).
    for fx, fh in ((hx0 + 75, 78), (hx0 + 275, 62)):
        d.polygon([(fx - 30, hy0 - 28), (fx - 11, hy0 - 28 - fh),
                   (fx + 4, hy0 - 28 - fh // 2), (fx + 16, hy0 - 28 - fh),
                   (fx + 34, hy0 - 28)], fill=FLAME_O)
        d.polygon([(fx - 16, hy0 - 28), (fx - 5, hy0 - 28 - fh // 2),
                   (fx + 5, hy0 - 28 - fh // 2), (fx + 18, hy0 - 28)],
                  fill=FLAME_Y)
    # Smoke puffs rising.
    for sx, sy, r in ((hx0 + 90, y0 + 22, 26), (hx0 + 126, y0 + 4, 20),
                      (hx0 + 62, y0 + 42, 19), (hx0 + 268, y0 + 30, 22),
                      (hx0 + 296, y0 + 10, 17)):
        d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=SMOKE)
    # Wave scallops below the hull only.
    for wx in range(x0 - 20, x1, 64):
        d.arc([wx, hy1 + 4, wx + 64, hy1 + 34], start=200, end=340,
              fill=(90, 150, 180), width=3)


def card(d, x, y, w, h, kicker, headline, body):
    d.rectangle([x, y, x + w, y + h], fill=CARD)
    d.rectangle([x, y, x + 6, y + h], fill=AMBER)
    d.rectangle([x, y, x + w, y + h], outline=CARD_LINE, width=2)
    tx = x + 22
    d.text((tx, y + 12), kicker, font=F_BOLD(17), fill=AMBER)
    f_h = F_BOLD(23)
    lines = wrap(d, headline, f_h, w - 44)
    yy = text_block(d, tx, y + 36, lines, f_h, WHITE, 27)
    f_b = F_REG(17)
    blines = wrap(d, body, f_b, w - 44)
    text_block(d, tx, yy + 6, blines, f_b, LIGHT, 21)


def main():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # ---- Masthead band (0-108) ----
    d.rectangle([0, 0, W, 108], fill=NAVY2)
    d.rectangle([0, 108, W, 112], fill=AMBER)
    d.text((32, 14), "WORLD NEWS", font=F_SERIF_B(54), fill=WHITE)
    d.text((32, 74), "WEDNESDAY  \u00b7  25 NOVEMBER 2026", font=F_BOLD(19), fill=AMBER)
    d.text((W - 32, 22), "ONE DAY", font=F_BOLD(22), fill=MUTED, anchor="ra")
    d.text((W - 32, 50), "ONE IMAGE", font=F_BOLD(22), fill=MUTED, anchor="ra")
    d.text((W - 32, 80), "THE WHOLE WORLD", font=F_BOLD(18), fill=AMBER, anchor="ra")

    # ---- Lead panel: illustrated tanker + headline (122-470) ----
    px0, py0, px1, py1 = 32, 122, W - 32, 470
    d.rectangle([px0, py0, px1, py1], fill=PANEL)
    d.rectangle([px0, py0, px1, py1], outline=CARD_LINE, width=2)
    draw_tanker_scene(d, px0 + 2, py0 + 2, px1 - 2, py0 + 208)
    hy = py0 + 220
    d.text((px0 + 24, hy), "LEAD  \u00b7  STRAIT OF HORMUZ", font=F_BOLD(18), fill=AMBER)
    f_lead = F_BOLD(34)
    lead = "TANKERS ABLAZE AFTER MINE STRIKES"
    lines = wrap(d, lead, f_lead, px1 - px0 - 48)
    yy = text_block(d, px0 + 24, hy + 26, lines, f_lead, WHITE, 40)
    f_sub = F_REG(20)
    sub = ("Two oil tankers struck naval mines, exploded and caught fire. "
           "Iran's Revolutionary Guard said they were on an unauthorised route.")
    slines = wrap(d, sub, f_sub, px1 - px0 - 48)
    text_block(d, px0 + 24, yy + 4, slines, f_sub, LIGHT, 25)

    # ---- 2x2 story grid (484-776) ----
    gy, gh, gap = 484, 140, 12
    cw = (W - 64 - gap) // 2
    card(d, 32, gy, cw, gh, "RED SEA  \u00b7  RIYADH",
         "Houthis hit Saudi refinery; Riyadh tower struck again",
         "Ras Tanura refinery hit; tallest tower struck a 2nd time in a week, 11 hurt.")
    card(d, 32 + cw + gap, gy, cw, gh, "GAZA",
         "Israel kills Hamas security chief in Gaza strike",
         "Mohammad Abuelouf killed with his wife and two children.")
    card(d, 32, gy + gh + gap, cw, gh, "UKRAINE",
         "Odesa strike kills 2; Russian dead put at 490,334",
         "Kyiv block hit, 2 hurt; Putin says Ukraine keeps hitting refineries.")
    card(d, 32 + cw + gap, gy + gh + gap, cw, gh, "SUDAN",
         "RSF drone strikes kill 19 civilians",
         "19 killed, 20 wounded in two cities.")

    # ---- Bottom "also today" strip (790-978) ----
    ay = 790
    d.rectangle([32, ay, W - 32, 978], fill=NAVY2)
    d.rectangle([32, ay, W - 32, 978], outline=CARD_LINE, width=2)
    d.text((56, ay + 10), "ALSO TODAY", font=F_BOLD(19), fill=AMBER)
    items = [
        "COP31 ends with no deal; Pope Leo XIV concerned. Solomon Islands & Australia sign no-foreign-base treaty.",
        "Huawei guilty in a US court of trade-secret theft and bank fraud.",
        "China carries Pakistan's first astronaut into orbit.",
        "CIA system breached \u00b7 Giuliani gets Medal of Freedom \u00b7 Colombia hostages freed \u00b7 Denmark bans headscarves for prosecutors.",
    ]
    f_a = F_REG(18)
    yy = ay + 38
    for it in items:
        d.text((56, yy), "\u2022", font=F_BOLD(18), fill=AMBER)
        ls = wrap(d, it, f_a, W - 64 - 56 - 24)
        yy = text_block(d, 80, yy, ls, f_a, LIGHT, 22)
        yy += 3

    # ---- Footer ----
    d.text((W // 2, H - 30), "25 NOVEMBER 2026  \u00b7  SUMMING UP THE DAY'S WORLD NEWS IN ONE IMAGE",
           font=F_BOLD(15), fill=MUTED, anchor="ma")

    img.save(OUT, format="PNG", optimize=True)


if __name__ == "__main__":
    main()
