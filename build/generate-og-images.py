#!/usr/bin/env python3
"""Generate 1200x630 Open Graph cards in the site's 'playful' style.

Run after adding a post:  python3 build/generate-og-images.py
Requires Pillow. Reads title + first tag from each post's front matter.

One per post plus a site default. Re-runnable: overwrites deterministically.
"""
import glob, os, re, textwrap
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'static/assets/img/og')
W, H = 1200, 630

BASE = '#efece5'; PANEL = '#f9f5ec'; INK = '#15171f'
COBALT = '#2240e8'; CORAL = '#ff5b3c'; LILAC = '#b9a8ff'
MINT = '#b6e84a'; MUSTARD = '#f0c63a'

AV = '/System/Library/Fonts/Avenir Next.ttc'
def font(size, style='bold'):
    return ImageFont.truetype(AV, size, index={'bold': 0, 'demi': 2, 'medium': 5, 'regular': 7}[style])

TOPIC = {  # slug -> (label, fill, text colour)
 'homelab':    ('Homelab',    MUSTARD, INK),
 'networking': ('Networking', MINT,    INK),
 'cloud':      ('Cloud',      LILAC,   INK),
 'ai':         ('AI',         COBALT,  '#ffffff'),
 'web':        ('Web',        MINT,    INK),
 'python':     ('Python',     COBALT,  '#ffffff'),
 'tools':      ('Tools',      PANEL,   INK),
 'security':   ('Security',   CORAL,   '#ffffff'),
 'career':     ('Career',     MUSTARD, INK),
 'money':      ('Money',      MUSTARD, INK),
 'life':       ('Life',       LILAC,   INK),
}


M, OFF, R = 34, 10, 26


def base_card(c1, c2):
    """Cream page, offset shadow, thick-bordered panel, accent blobs clipped
    inside the panel so they never escape the frame."""
    img = Image.new('RGB', (W, H), BASE)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([M + OFF, M + OFF, W - M + OFF, H - M + OFF], radius=R, fill=INK)
    d.rounded_rectangle([M, M, W - M, H - M], radius=R, fill=PANEL)

    blob = Image.new('RGB', (W, H), PANEL)
    bd = ImageDraw.Draw(blob)
    bd.ellipse([W - 300, -70, W + 60, 290], fill=c1)
    bd.ellipse([W - 210, H - 250, W + 100, H + 60], fill=c2)

    mask = Image.new('L', (W, H), 0)
    ImageDraw.Draw(mask).rounded_rectangle([M, M, W - M, H - M], radius=R, fill=255)
    img.paste(blob, (0, 0), mask)

    ImageDraw.Draw(img).rounded_rectangle([M, M, W - M, H - M], radius=R, outline=INK, width=5)
    return img


def pill(d, xy, text, fill, fg):
    f = font(24, 'demi')
    x, y = xy
    tw = d.textlength(text, font=f)
    pad_x, h = 24, 50
    d.rounded_rectangle([x, y, x + tw + pad_x * 2, y + h], radius=25, fill=fill, outline=INK, width=4)
    d.text((x + pad_x, y + h / 2), text, font=f, fill=fg, anchor='lm')


def wrap_to(d, text, f, max_w):
    """Greedy wrap using real glyph metrics, not a character-count guess."""
    lines, cur = [], ''
    for word in text.split():
        trial = f'{cur} {word}'.strip()
        if cur and d.textlength(trial, font=f) > max_w:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


def fit(d, text, max_w, max_h, max_lines, hi=76, lo=32):
    """Largest size where the wrapped title fits both the column and the
    vertical budget above the footer."""
    for size in range(hi, lo - 1, -2):
        f = font(size)
        lines = wrap_to(d, text, f, max_w)
        step = int(size * 1.16)
        if len(lines) <= max_lines and len(lines) * step <= max_h:
            return f, lines, step
    f = font(lo)
    return f, wrap_to(d, text, f, max_w)[:max_lines], int(lo * 1.16)


def footer(d, right_text):
    f = font(23, 'demi')
    y = H - 96
    d.ellipse([80, y - 6, 80 + 42, y + 36], fill=CORAL, outline=INK, width=4)
    d.text((138, y + 15), 'Pramesh Bajracharya', font=f, fill=INK, anchor='lm')
    fr = font(22, 'medium')
    d.text((W - 90, y + 15), right_text, font=fr, fill=INK, anchor='rm')


def card(path, title, topic_slug):
    label, fill, fg = TOPIC.get(topic_slug, ('Notes', PANEL, INK))
    img = base_card(fill, LILAC if fill != LILAC else MINT)
    d = ImageDraw.Draw(img)

    pill(d, (80, 96), label, fill, fg)
    TOP, BOTTOM = 194, 486          # title band, clear of the pill and the footer
    f, lines, step = fit(d, title, max_w=W - 300, max_h=BOTTOM - TOP, max_lines=4)
    y = TOP + (BOTTOM - TOP - len(lines) * step) // 2
    for ln in lines:
        d.text((80, y), ln, font=f, fill=INK)
        y += step
    footer(d, 'prameshbajra.com')
    img.save(path, 'PNG', optimize=True)


def default_card(path):
    img = base_card(MUSTARD, MINT)
    d = ImageDraw.Draw(img)
    pill(d, (80, 108), 'prameshbajra.com', CORAL, '#ffffff')
    d.text((80, 208), 'Pramesh', font=font(104), fill=INK)
    d.text((80, 318), 'Bajracharya.', font=font(104), fill=COBALT)
    d.text((80, 452), 'Software engineer in Hamburg — cloud,', font=font(30, 'medium'), fill=INK)
    d.text((80, 494), 'homelab, networking, and 3D printing.', font=font(30, 'medium'), fill=INK)
    img.save(path, 'PNG', optimize=True)


def main():
    os.makedirs(OUT, exist_ok=True)
    default_card(os.path.join(OUT, 'default.png'))
    n = 0
    for p in sorted(glob.glob(os.path.join(ROOT, '_posts', '*.md'))):
        txt = open(p, encoding='utf-8').read()
        fm = re.match(r'^---\s*\n(.*?)\n---\s*\n', txt, re.S).group(1)
        title = re.search(r'^title:\s*(.*)$', fm, re.M).group(1).strip().strip('"')
        tags = re.search(r'^tags:\s*\[(.*?)\]', fm, re.M).group(1)
        primary = [t.strip() for t in tags.split(',')][0]
        slug = re.search(r'^image:.*/og/(.*)\.png', fm, re.M).group(1)
        card(os.path.join(OUT, f'{slug}.png'), title, primary)
        n += 1
    print(f'generated {n} post cards + default.png in {OUT}')


main()
