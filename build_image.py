#!/usr/bin/env python3
"""Draw the 22 November 2026 world-news front page (1024x1024 PNG).

Own design: cream broadsheet, navy masthead, one wide lead story on
top and four stories in a two-by-two grid below. Every picture is
drawn here with plain PIL shapes; no photos, no copied artwork.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (246, 241, 227)
INK = (20, 33, 61)
RED = (178, 34, 34)
TEAL = (14, 116, 144)
GOLD = (180, 130, 29)
MUTED = (90, 88, 78)
SEA = (38, 90, 130)
SKY = (214, 232, 240)
GRASS = (46, 125, 50)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning a list of lines that fit `width`."""
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


def para(draw, x, y, text, fnt, width, fill, leading):
    lines = wrap(draw, text, fnt, width)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def kicker(draw, x, y, text):
    draw.text((x, y), text, font=font(SANS_B, 15), fill=RED)


def headline(draw, x, y, text, size, width, leading=None):
    fnt = font(SERIF, size)
    return para(draw, x, y, text, fnt, width, INK, leading or size + 5)


# ---------------------------------------------------------------- pictures
def pic_submarine(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    d.ellipse([x + 8, y + h - 26, x + w - 8, y + h + 14], fill=SEA)
    for i in range(5):  # harbour skyline
        bx = x + 12 + i * 52
        d.rectangle([bx, y + 14 + (i % 3) * 8, bx + 34, y + 62], fill=(120, 140, 160))
    d.ellipse([x + 60, y + 62, x + w - 60, y + 118], fill=(30, 48, 70))  # hull
    d.rectangle([x + 150, y + 42, x + 210, y + 66], fill=(30, 48, 70))  # tower
    d.rectangle([x + 176, y + 28, x + 182, y + 44], fill=(30, 48, 70))
    d.rectangle([x + 30, y + 66, x + 52, y + 84], fill=(30, 48, 70))  # tail fin
    d.polygon([(x + w - 52, y + 88), (x + w - 30, y + 80), (x + w - 30, y + 104)],
              fill=(30, 48, 70))
    for cx in (95, 150, 205, 260):  # portholes
        d.ellipse([x + cx, y + 84, x + cx + 12, y + 96], fill=(240, 220, 120))
    d.text((x + w // 2, y + 82), "AUKUS", font=font(SANS_B, 22),
           fill=(255, 255, 255), anchor="ma")
    for wx in range(x + 6, x + w - 6, 26):  # wave ticks
        d.arc([wx, y + h - 16, wx + 24, y + h + 2], 180, 360, fill=(255, 255, 255), width=3)


def pic_strike(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(238, 226, 205))
    d.rectangle([x + 16, y + 52, x + 150, y + h - 8], fill=(150, 60, 50))  # factory
    d.rectangle([x + 170, y + 30, x + 196, y + h - 8], fill=(120, 45, 40))  # chimney
    for sx in (36, 76, 116):
        d.rectangle([sx, y + 68, sx + 24, y + 92], fill=(250, 230, 150))
    d.polygon([(x + 16, y + 52), (x + 83, y + 22), (x + 150, y + 52)], fill=(110, 40, 36))
    for px, col in ((225, RED), (275, TEAL), (325, GOLD)):  # picket signs
        d.rectangle([px + 8, y + 40, px + 12, y + h - 10], fill=(70, 60, 50))
        d.rectangle([px - 14, y + 18, px + 34, y + 46], fill=(255, 255, 255),
                    outline=col, width=3)
        d.text((px - 8, y + 24), "5%", font=font(SANS_B, 18), fill=col)
    for i in range(3):  # marching heads
        cx = x + 240 + i * 42
        d.ellipse([cx, y + h - 42, cx + 22, y + h - 20], fill=(245, 205, 160))
        d.rectangle([cx - 2, y + h - 20, cx + 24, y + h - 6], fill=INK)


def pic_ballot(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(226, 234, 244))
    for i in range(4):  # skyline
        bx = x + 14 + i * 46
        d.rectangle([bx, y + 18 + (i % 2) * 16, bx + 32, y + 66], fill=(110, 130, 155))
    d.rectangle([x + 215, y + 52, x + 330, y + h - 12], fill=(200, 60, 55))  # box
    d.rectangle([x + 205, y + 44, x + 340, y + 58], fill=(160, 40, 38))
    d.rectangle([x + 255, y + 48, x + 290, y + 54], fill=(40, 40, 40))
    d.polygon([(x + 250, y + 8), (x + 292, y + 8), (x + 282, y + 46), (x + 258, y + 46)],
              fill=(255, 255, 255), outline=INK, width=2)  # ballot paper
    d.line([(x + 264, y + 20), (x + 272, y + 30), (x + 284, y + 14)], fill=RED, width=4)
    for i in range(4):  # queue
        cx = x + 30 + i * 40
        d.ellipse([cx, y + h - 46, cx + 22, y + h - 24], fill=(245, 205, 160))
        d.rectangle([cx - 2, y + h - 24, cx + 24, y + h - 8], fill=(60, 90, 140))


def pic_talks(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 226, 208))
    d.rectangle([x + 40, y + 78, x + w - 40, y + h - 14], fill=(120, 82, 40))  # table
    d.rectangle([x + 40, y + 78, x + w - 40, y + 90], fill=(150, 105, 55))
    d.rectangle([x + 60, y + 18, x + 76, y + 78], fill=(90, 60, 30))  # flag poles
    d.rectangle([x + w - 76, y + 18, x + w - 60, y + 78], fill=(90, 60, 30))
    d.polygon([(x + 76, y + 18), (x + 128, y + 28), (x + 76, y + 40)], fill=(40, 90, 180))
    d.polygon([(x + w - 76, y + 18), (x + w - 128, y + 28), (x + w - 76, y + 40)],
              fill=(255, 255, 255), outline=(40, 90, 180), width=2)
    for cx in (110, 270):  # two seated figures
        d.ellipse([cx, y + 30, cx + 30, y + 60], fill=(245, 205, 160))
        d.polygon([(cx - 8, y + 62), (cx + 38, y + 62), (cx + 30, y + 96), (cx, y + 96)],
                  fill=INK)
    d.ellipse([x + 158, y + 84, x + 222, y + 108], fill=(255, 255, 255), outline=GOLD, width=2)
    d.text((x + 190, y + 89), "48 / 120", font=font(SANS_B, 12), fill=INK, anchor="ma")


def pic_tennis(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(58, 120, 80))  # court
    d.rectangle([x + 30, y + 12, x + w - 30, y + h - 12], outline=(255, 255, 255), width=3)
    d.line([x + w // 2, y + 12, x + w // 2, y + h - 12], fill=(255, 255, 255), width=2)
    d.rectangle([x + 14, y + h // 2 - 6, x + w - 14, y + h // 2 + 6], fill=(30, 30, 30))
    for nx in range(x + 14, x + w - 14, 12):
        d.line([nx, y + h // 2 - 6, nx, y + h // 2 + 6], fill=(200, 200, 200), width=1)
    d.ellipse([x + 44, y + 22, x + 68, y + 46], fill=(200, 230, 60), outline=(255, 255, 255),
              width=2)  # ball
    d.arc([x + 44, y + 22, x + 68, y + 46], 300, 60, fill=(255, 255, 255), width=2)
    d.text((x + 84, y + 22), "ZVEREV  vs  ALCARAZ", font=font(SANS_B, 17),
           fill=(255, 255, 255))
    # small trophy
    tx, ty = x + w - 66, y + h - 52
    d.polygon([(tx, ty), (tx + 34, ty), (tx + 30, ty + 26), (tx + 4, ty + 26)], fill=GOLD)
    d.rectangle([tx + 12, ty + 26, tx + 22, ty + 34], fill=GOLD)
    d.rectangle([tx + 4, ty + 34, tx + 30, ty + 40], fill=GOLD)


# ---------------------------------------------------------------- page
def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=3)
    d.rectangle([22, 22, W - 23, H - 23], outline=INK, width=1)

    # Masthead
    d.text((W // 2, 44), "THE WORLD IN ONE DAY", font=font(SERIF, 56),
           fill=INK, anchor="ma")
    d.line([60, 108, W - 60, 108], fill=INK, width=2)
    d.text((W // 2, 118), "SUNDAY, 22 NOVEMBER 2026", font=font(SANS_B, 26),
           fill=RED, anchor="ma")
    d.text((W // 2, 148), "Five stories from around the globe  |  Sydney  ·  Berlin  ·  Hong Kong  ·  Jerusalem  ·  Turin",
           font=font(SANS, 15), fill=MUTED, anchor="ma")
    d.line([60, 172, W - 60, 172], fill=INK, width=2)

    # Lead story: AUKUS
    lx, ly = 44, 188
    kicker(d, lx, ly, "DEFENCE  ·  AUSTRALIA")
    y = headline(d, lx, ly + 22, "Australia rejects US budget office warning over AUKUS subs",
                 30, 540, 36)
    y = para(d, lx, y + 6,
             "Defence Minister Richard Marles said in Sydney on Sunday that a "
             "US Congressional Budget Office report was wrong to claim selling "
             "Virginia-class submarines to Australia would shrink the US "
             "attack-submarine fleet. He said AUKUS \u201cis actually happening\u201d "
             "and US production is \u201cabsolutely increasing\u201d.",
             font(SANS, 17), 540, INK, 23)
    pic_submarine(d, 612, 188, 368, 168)
    para(d, 612, 362, "A Virginia-class submarine. Australia has pledged "
         "A$368bn to AUKUS over 30 years.", font(SANS, 13), 368, MUTED, 17)
    d.line([44, 396, W - 44, 396], fill=INK, width=2)

    # Four stories in a grid
    cells = [
        (44, 414, "LABOUR  ·  GERMANY",
         "German union calls 23,000 workers out on strike on Monday",
         "IG Metall announced on Sunday a 24-hour walkout at 19 firms in "
         "northern Germany, including Mercedes-Benz, Meyer Werft and "
         "Siemens Gamesa, in a pay dispute. The union wants a 5% rise; "
         "employers offer no permanent rise for 20 months.",
         pic_strike),
        (524, 414, "ELECTION  ·  HONG KONG",
         "Hong Kong votes for its 1,500-seat Election Committee",
         "Polls opened at 9am on Sunday, with 856 candidates standing for "
         "723 seats in 31 subsectors. The committee, serving five years "
         "from 1 February 2027, will choose the chief executive in "
         "March 2027.",
         pic_ballot),
        (44, 700, "POLITICS  ·  ISRAEL",
         "Eisenkot invites Likud to talks on a unity government",
         "Gadi Eisenkot, tasked with forming Israel\u2019s next government, "
         "invited Benjamin Netanyahu\u2019s Likud party to talks starting "
         "on Sunday, aiming for the broadest unity government. His bloc "
         "holds 48 of 120 seats, 13 short of a majority.",
         pic_talks),
        (524, 700, "SPORT  ·  ITALY",
         "Zverev meets Alcaraz in the ATP Finals title match",
         "The singles final is in Turin on Sunday evening, not before "
         "18:00 local time. Zverev, unbeaten in four matches, chases a "
         "third title; Alcaraz, on a 13-match winning run, chases his "
         "first. The doubles final is at 15:00.",
         pic_tennis),
    ]
    for (cx, cy, kick, head, body, pic) in cells:
        pic(d, cx, cy, 456, 96)
        kicker(d, cx, cy + 106, kick)
        y = headline(d, cx, cy + 128, head, 21, 456, 25)
        para(d, cx, y + 4, body, font(SANS, 15), 456, INK, 20)
        d.line([cx, cy + 268, cx + 456, cy + 268], fill=(180, 175, 160), width=1)

    # Footer with sources
    d.text((W // 2, 978), "Sources: Reuters  ·  China Daily Asia  ·  The Daily Jagran  ·  Tennis Tour Calendar / ATP Tour  —  all five stories first reported on 22 November 2026.",
           font=font(SANS, 12), fill=MUTED, anchor="ma")

    img.save("entry.png", optimize=True)


if __name__ == "__main__":
    main()
