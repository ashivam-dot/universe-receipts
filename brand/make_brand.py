"""Build the Universe Receipts brand kit: avatar, banner, watermark, and the banner credits.

Run from the pipeline project so its dependencies are available:
    cd pipeline && uv run --no-sync python ../brand/make_brand.py
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import urllib.parse
import urllib.request
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

BRAND = Path(__file__).resolve().parent
PIPELINE = BRAND.parent / "pipeline"
FONTS = PIPELINE / "assets/fonts"
ANTON = FONTS / "Anton-Regular.ttf"
MONTSERRAT_XB = FONTS / "Montserrat-ExtraBold.ttf"
MONTSERRAT_BLACK = FONTS / "Montserrat-Black.ttf"

NAVY = (11, 15, 26)
NAVY_GLOW = (24, 36, 66)
CYAN = (61, 245, 255)
WHITE = (255, 255, 255)

COMMONS_API = "https://commons.wikimedia.org/w/api.php"
USER_AGENT = f"UniverseReceiptsBrand/1.0 ({os.environ.get('YTC_CONTACT') or 'akshshivam5@gmail.com'})"
# Commons licenses that allow commercial reuse without share-alike.
OPEN_LICENSES = re.compile(r"^(public domain|pd\b.*|cc0.*|cc by 4\.0|no restrictions)$", re.I)

# name: (Commons file title, download width, display title, author as the source credits it)
PICTURES = {
    "carina": ("File:NASA’s Webb Reveals Cosmic Cliffs, Glittering Landscape of Star Birth.jpg", 3200,
               "\"Cosmic Cliffs\" in the Carina Nebula (James Webb Space Telescope, 2022)", "NASA, ESA, CSA, and STScI"),
    "pillars": ("File:Pillars of Creation (NIRCam Image).jpg", 1400,
                "Pillars of Creation, NIRCam image (James Webb Space Telescope, 2022)",
                "NASA, ESA, CSA, STScI; image processing by Joseph DePasquale, Anton M. Koekemoer, and Alyssa Pagan "
                "(STScI)"),
    "earthrise": ("File:NASA-Apollo8-Dec24-Earthrise.jpg", 2400, "Earthrise (Apollo 8, December 24, 1968)",
                  "NASA / Bill Anders"),
}


def _plain(html) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", str(html or ""))).strip()


def _fetch_picture(name: str, title: str, width: int, cache: Path) -> tuple[Image.Image, dict]:
    """Download a Commons picture once, refusing anything not public domain, CC0, or CC BY 4.0."""
    cache.mkdir(parents=True, exist_ok=True)
    path, meta_path = cache / f"{name}.jpg", cache / f"{name}.json"
    if not meta_path.exists():
        query = urllib.parse.urlencode({"action": "query", "prop": "imageinfo", "iiprop": "extmetadata|url",
                                        "iiurlwidth": width, "titles": title, "format": "json"})
        request = urllib.request.Request(f"{COMMONS_API}?{query}", headers={"User-Agent": USER_AGENT})
        page = next(iter(json.load(urllib.request.urlopen(request, timeout=60))["query"]["pages"].values()))
        info = page["imageinfo"][0]
        meta = {k: _plain(v.get("value", "")) for k, v in info["extmetadata"].items()}
        license_name = meta.get("LicenseShortName", "")
        if not OPEN_LICENSES.match(license_name):
            raise RuntimeError(f"{title}: license {license_name!r} isn't public domain, CC0, or CC BY 4.0")
        credit = {"title": page["title"].removeprefix("File:"), "author": meta.get("Artist", ""),
                  "credit": meta.get("Credit", ""), "license": license_name,
                  "url": info["descriptionurl"], "download": info.get("thumburl") or info["url"]}
        subprocess.run(["curl", "-sSfL", "-A", USER_AGENT, "-o", str(path), credit["download"]], check=True)
        meta_path.write_text(json.dumps(credit, indent=2, ensure_ascii=False), encoding="utf-8")
    return Image.open(path).convert("RGB"), json.loads(meta_path.read_text(encoding="utf-8"))


def _zigzag(x0: float, x1: float, y: float, tooth: float, down: bool = True) -> list[tuple[float, float]]:
    """Points of a torn-paper zigzag running from x1 back to x0 along y."""
    count = max(2, round((x1 - x0) / tooth))
    step = (x1 - x0) / count
    depth = step * 0.55 * (1 if down else -1)
    points = []
    for i in range(count, -1, -1):
        points.append((x0 + i * step, y))
        if i:
            points.append((x0 + (i - 0.5) * step, y + depth))
    return points


def _mark(size: int) -> Image.Image:
    """The receipt mark on a transparent square: a white receipt with a torn bottom holding a ringed planet."""
    layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    cx = size / 2
    w, h = size * 0.52, size * 0.68
    left, right, top = cx - w / 2, cx + w / 2, size * 0.5 - h / 2 - size * 0.015
    bottom = top + h
    tooth = w / 7
    corner = size * 0.045
    outline = [(left, bottom), (left, top + corner)]
    outline += [(left + corner * (1 - np.cos(a)), top + corner * (1 - np.sin(a))) for a in np.linspace(0, np.pi / 2, 12)]
    outline += [(right - corner * (1 - np.cos(a)), top + corner * (1 - np.sin(a))) for a in np.linspace(np.pi / 2, 0, 12)]
    outline += [(right, bottom)]
    outline += _zigzag(left, right, bottom, tooth)
    draw.polygon(outline, fill=WHITE)

    pcx, pcy, pr = cx, top + h * 0.40, size * 0.125
    ring_w, ring_h, ring_t = size * 0.215, size * 0.066, size * 0.036
    planet = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    pdraw = ImageDraw.Draw(planet)
    box = [pcx - ring_w, pcy - ring_h, pcx + ring_w, pcy + ring_h]
    pdraw.arc(box, 180, 360, fill=NAVY, width=round(ring_t))
    gap = size * 0.028
    pdraw.ellipse([pcx - pr - gap, pcy - pr - gap, pcx + pr + gap, pcy + pr + gap], fill=WHITE)
    pdraw.ellipse([pcx - pr, pcy - pr, pcx + pr, pcy + pr], fill=NAVY)
    outer = [box[0] - gap, box[1] - gap, box[2] + gap, box[3] + gap]
    pdraw.arc(outer, 0, 180, fill=WHITE, width=round(ring_t + 2 * gap))
    pdraw.arc(box, 0, 180, fill=NAVY, width=round(ring_t))
    planet = planet.rotate(18, resample=Image.BICUBIC, center=(pcx, pcy))
    layer.alpha_composite(planet)

    bar_h = size * 0.042
    for y, bar_w, color in ((top + h * 0.71, w * 0.62, NAVY), (top + h * 0.82, w * 0.38, CYAN)):
        draw.rounded_rectangle([cx - bar_w / 2, y, cx + bar_w / 2, y + bar_h], radius=bar_h / 2, fill=color)
    return layer


def _badge(size: int, tilt: float = -8) -> Image.Image:
    """The circular badge used for the avatar and watermark, drawn 4x and scaled down for clean edges."""
    big = size * 4
    yy, xx = np.mgrid[0:big, 0:big].astype(np.float32)
    dist = np.hypot(xx - big / 2, yy - big / 2) / (big / 2)
    glow = np.clip(1 - dist, 0, 1)[..., None] ** 1.4
    bg = np.array(NAVY, np.float32) + (np.array(NAVY_GLOW, np.float32) - np.array(NAVY, np.float32)) * glow
    badge = Image.fromarray(bg.astype(np.uint8), "RGB").convert("RGBA")
    mark = _mark(big).rotate(tilt, resample=Image.BICUBIC)
    shadow = Image.new("RGBA", mark.size, (0, 0, 0, 0))
    shadow.putalpha(mark.getchannel("A").point(lambda a: a * 0.55))
    shadow = shadow.filter(ImageFilter.GaussianBlur(big * 0.02))
    badge.alpha_composite(shadow, (0, int(big * 0.015)))
    badge.alpha_composite(mark)
    return badge.resize((size, size), Image.LANCZOS)


def make_avatar(out: Path, size: int = 800) -> Image.Image:
    avatar = _badge(size).convert("RGB")
    avatar.save(out)
    return avatar


def make_watermark(out: Path, size: int = 150) -> None:
    badge = _badge(size * 4)
    mask = Image.new("L", badge.size, 0)
    ImageDraw.Draw(mask).ellipse([0, 0, badge.width - 1, badge.height - 1], fill=255)
    badge.putalpha(mask)
    badge.resize((size, size), Image.LANCZOS).save(out)


def _cover(image: Image.Image, w: int, h: int, focus: tuple[float, float], zoom: float = 1.0) -> Image.Image:
    """Crop to w x h around the focus point (fractions of the picture), zoom times tighter than a plain cover."""
    scale = max(w / image.width, h / image.height) * zoom
    crop_w, crop_h = w / scale, h / scale
    left = min(max(focus[0] * image.width - crop_w / 2, 0), image.width - crop_w)
    top = min(max(focus[1] * image.height - crop_h / 2, 0), image.height - crop_h)
    return image.resize((w, h), Image.LANCZOS, box=(left, top, left + crop_w, top + crop_h))


def _torn_mask(w: int, h: int, side: str, tooth: int = 36) -> Image.Image:
    """Mask for a side panel whose inner edge is torn like a receipt."""
    mask = Image.new("L", (w, h), 0)
    step = h / max(2, round(h / tooth))
    depth = step * 0.55
    edge = []
    for i in range(round(h / step) + 1):
        edge.append((w - depth if side == "left" else depth, i * step))
        edge.append((w if side == "left" else 0, i * step + step / 2))
    edge = [(x, min(y, h)) for x, y in edge]
    polygon = [(0, 0), *edge, (0, h)] if side == "left" else [(w, 0), *edge, (w, h)]
    ImageDraw.Draw(mask).polygon(polygon, fill=255)
    return mask


def make_banner(out: Path, cache: Path) -> list[dict]:
    w, h = 2560, 1440
    safe_w, safe_h = 1546, 423
    pictures = {name: _fetch_picture(name, title, width, cache) for name, (title, width, *_) in PICTURES.items()}
    for name, (*_, label, author) in PICTURES.items():
        pictures[name][1].update(label=label, author=author)

    center = _cover(pictures["carina"][0], w, h, (0.5, 0.62))
    arr = np.asarray(center, np.float32)
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    # Darken toward the middle so the name reads, keeping the nebula's glow at the edges.
    focus = np.exp(-(((xx - w / 2) / (safe_w * 0.62)) ** 2 + ((yy - h / 2) / (safe_h * 0.95)) ** 2))
    shade = 0.55 - 0.33 * focus
    navy = np.array(NAVY, np.float32)
    arr = arr * shade[..., None] + navy * (1 - shade[..., None])
    banner = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB")

    # The side pictures stop just outside the mobile crop, so phones see only the name on the nebula.
    side_w = (w - safe_w) // 2 - 10
    panels = (("pillars", "left", (0.47, 0.42), 1.0), ("earthrise", "right", (0.585, 0.51), 1.6))
    for name, side, focus_point, zoom in panels:
        panel = _cover(pictures[name][0], side_w, h, focus_point, zoom)
        mask = _torn_mask(side_w, h, side)
        x = 0 if side == "left" else w - side_w
        edge = mask.filter(ImageFilter.MaxFilter(15))
        banner.paste(Image.new("RGB", (side_w, h), CYAN), (x, 0), edge)
        banner.paste(panel, (x, 0), mask)

    draw = ImageDraw.Draw(banner)
    title_font = ImageFont.truetype(str(ANTON), 196)
    tag_font = ImageFont.truetype(str(MONTSERRAT_BLACK), 58)
    small_font = ImageFont.truetype(str(MONTSERRAT_XB), 30)
    words = [("UNIVERSE", WHITE), ("RECEIPTS", CYAN)]
    tagline = "SPACE FACTS. WITH RECEIPTS."
    small = "NEW SHORTS EVERY DAY  ·  EVERY CLAIM SOURCED"

    word_gap = 40
    widths = [draw.textlength(word, font=title_font) for word, _ in words]
    _, t_top, _, t_bottom = draw.textbbox((0, 0), "UNIVERSE RECEIPTS", font=title_font)
    _, g_top, _, g_bottom = draw.textbbox((0, 0), tagline, font=tag_font)
    _, s_top, _, s_bottom = draw.textbbox((0, 0), small, font=small_font)
    gap_title, gap_tag = 34, 30
    block = (t_bottom - t_top) + gap_title + (g_bottom - g_top) + gap_tag + (s_bottom - s_top)
    # Keep everything inside the 1546x423 area that every device shows (centered at y=720).
    assert block <= safe_h - 40 and sum(widths) + word_gap <= safe_w - 80
    top = h / 2 - block / 2

    x = (w - (sum(widths) + word_gap)) / 2
    for (word, color), word_w in zip(words, widths):
        draw.text((x, top - t_top), word, font=title_font, fill=color)
        x += word_w + word_gap

    tag_y = top + (t_bottom - t_top) + gap_title - g_top
    tag_w = draw.textlength(tagline, font=tag_font)
    draw.text(((w - tag_w) / 2, tag_y), tagline, font=tag_font, fill=WHITE)
    small_y = tag_y + g_bottom + gap_tag - s_top
    small_w = draw.textlength(small, font=small_font)
    draw.text(((w - small_w) / 2, small_y), small, font=small_font, fill=(170, 205, 225))
    banner.save(out, quality=92)
    return [credit for _, credit in pictures.values()]


def write_credits(credits: list[dict]) -> str:
    lines = ["# Banner image credits", "",
             "Pictures from Wikimedia Commons, checked to be public domain, CC0, or CC BY 4.0 (no share-alike, "
             "no NonCommercial). The avatar and watermark are original drawings.", ""]
    for c in credits:
        lines += [f"- **{c['label']}**", f"  - File: {c['title']}", f"  - Author: {c['author']}",
                  f"  - License: {c['license']}", f"  - Link: {c['url']}"]
    text = "\n".join(lines) + "\n"
    (BRAND / "CREDITS.md").write_text(text, encoding="utf-8")
    return text


def main() -> None:
    out = BRAND / "out"
    out.mkdir(exist_ok=True)
    make_avatar(out / "avatar-800.png")
    make_watermark(out / "watermark-150.png")
    credits = make_banner(out / "banner-2560x1440.jpg", BRAND / "src")
    print(write_credits(credits))


if __name__ == "__main__":
    main()
