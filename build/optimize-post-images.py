#!/usr/bin/env python3
"""Resize and re-encode post images to roughly 2x their rendered size.

Screenshots were being shipped at full capture resolution — iPhone grabs at
1170x2532 displayed in a 250px column, for example — which put 6.6MB on a
single post page. Nothing here upscales, and PNG stays lossless so text in
screenshots does not pick up compression artefacts.

    python3 build/optimize-post-images.py --dry-run
    python3 build/optimize-post-images.py

Requires Pillow.
"""
import argparse, glob, io, os, re, shutil, subprocess, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# .ply-wrap is 1240px and .ply-article adds up to 48px padding each side.
CONTENT_PX = 1144
# Retina headroom without shipping absurd files.
MAX_W = 1600
JPEG_Q, WEBP_Q = 85, 85


def display_width(attr):
    """Rendered CSS width in px from the tag's width attribute."""
    if not attr:
        return CONTENT_PX
    attr = attr.strip()
    if attr.endswith('%'):
        try:
            return CONTENT_PX * float(attr[:-1]) / 100
        except ValueError:
            return CONTENT_PX
    m = re.match(r'(\d+(?:\.\d+)?)', attr)
    return float(m.group(1)) if m else CONTENT_PX


def collect():
    """(abs_path, target_width) for every <img> in a post, widest target wins."""
    targets = {}
    for post in sorted(glob.glob(os.path.join(ROOT, '_posts', '*.md'))):
        for tag in re.findall(r'<img[^>]*>', open(post, encoding='utf-8').read()):
            src = re.search(r'src="([^"]+)"', tag)
            if not src or src.group(1).startswith(('http://', 'https://')):
                continue
            rel = src.group(1).lstrip('/')
            path = os.path.join(ROOT, rel)
            if not os.path.isfile(path):
                print(f'  !! missing: {src.group(1)}', file=sys.stderr)
                continue
            w = re.search(r'width\s*=\s*"([^"]+)"', tag)
            want = min(round(display_width(w.group(1) if w else None) * 2), MAX_W)
            targets[path] = max(targets.get(path, 0), want)
    return targets


def resample(im, target):
    if im.width <= target:
        return im, False
    h = round(im.height * target / im.width)
    return im.resize((target, h), Image.LANCZOS), True


def encode(im, ext):
    """Re-encode into memory so the result can be size-checked before it lands."""
    buf = io.BytesIO()
    if ext in ('.jpg', '.jpeg'):
        im.convert('RGB').save(buf, 'JPEG', quality=JPEG_Q, optimize=True, progressive=True)
    elif ext == '.webp':
        im.save(buf, 'WEBP', quality=WEBP_Q, method=6)
    elif ext == '.png':
        im.save(buf, 'PNG', optimize=True)
    else:
        return None
    return buf.getvalue()


def shrink_gif(path, target, dry):
    """PIL rebuilds animated GIFs frame-by-frame and destroys inter-frame
    compression (one file went 1.9MB -> 51MB that way). ffmpeg's
    palettegen/paletteuse keeps it intact."""
    before = os.path.getsize(path)
    if not shutil.which('ffmpeg'):
        return before, before, 'gif — no ffmpeg, left alone'
    if dry:
        return before, 0, f'gif -> {target}px via ffmpeg'
    tmp = path + '.tmp.gif'
    vf = (f'scale={target}:-1:flags=lanczos,split[s0][s1];'
          f'[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer:bayer_scale=3')
    r = subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', path,
                        '-vf', vf, '-loop', '0', tmp], capture_output=True)
    if r.returncode != 0 or not os.path.isfile(tmp):
        if os.path.exists(tmp):
            os.remove(tmp)
        return before, before, 'gif — ffmpeg failed, left alone'
    after = os.path.getsize(tmp)
    if after >= before:
        os.remove(tmp)
        return before, before, 'gif — no gain, left alone'
    os.replace(tmp, path)
    return before, after, f'gif -> {target}px'


def process(path, target, dry):
    before = os.path.getsize(path)
    ext = os.path.splitext(path)[1].lower()
    im = Image.open(path)

    if ext == '.gif' and getattr(im, 'n_frames', 1) > 1:
        # Retina width costs 2x on every frame, so animations get 1x instead.
        target = round(target / 2)
        if im.width <= target:
            return before, before, f'{im.width}px animated — kept'
        return shrink_gif(path, target, dry)

    out, resized = resample(im, target)
    note = f'{im.width}->{out.width}px' if resized else f'{im.width}px kept'
    if dry:
        return before, 0, note
    data = encode(out, ext)
    if data is None:
        return before, before, 'unhandled type — skipped'
    # Several of these are screenshots whose original encoder beat Pillow even
    # at a smaller size. Never write a file that got bigger.
    if len(data) >= before:
        return before, before, f'{note}, original smaller — kept'
    with open(path, 'wb') as fh:
        fh.write(data)
    return before, len(data), note


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()
    targets = collect()
    tb = ta = 0
    for path, target in sorted(targets.items(), key=lambda kv: -os.path.getsize(kv[0])):
        b, a, note = process(path, target, args.dry_run)
        tb += b
        ta += a if a else b
        rel = path[len(ROOT) + 1:]
        if args.dry_run:
            print(f'  {b/1024:7.0f}K  target {target:>5}px  {note:<22} {rel[-46:]}')
        else:
            print(f'  {b/1024:7.0f}K -> {a/1024:6.0f}K  {note:<22} {rel[-46:]}')
    print(f'\n  {len(targets)} images | before {tb/1024/1024:.1f} MB'
          + ('' if args.dry_run else f' -> after {ta/1024/1024:.1f} MB'
             f' ({100*(tb-ta)/tb:.0f}% smaller)'))


main()
