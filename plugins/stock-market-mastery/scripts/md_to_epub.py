#!/usr/bin/env python3
"""Build a Kindle-friendly EPUB from a Stock Market Mastery company output folder.

Usage:
  python scripts/md_to_epub.py output/TSM
  python scripts/md_to_epub.py output/TSM --out output/TSM/book.epub

Supports local images referenced from Markdown (`![alt](path)` or `<img src>`).
Prefers pandoc when available; otherwise uses ebooklib + markdown.
"""

from __future__ import annotations

import argparse
import html
import json
import mimetypes
import re
import shutil
import subprocess
import sys
import urllib.parse
import zipfile
from pathlib import Path

CHAPTER_ORDER = [
    "00-front-matter.md",
    "01-market.md",
    "02-industry.md",
    "03-company.md",
    "04-financials.md",
    "05-earnings.md",
    "06-products.md",
    "07-supply-chain.md",
    "08-document-literacy.md",
    "09-capstone.md",
    "10-quizzes.md",
]

# Markdown image: ![alt](url "title")
MD_IMAGE_RE = re.compile(
    r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"([^\"]*)\")?\)"
)
# HTML img src="..." or src='...'
HTML_IMG_SRC_RE = re.compile(
    r"""<img\b[^>]*?\bsrc\s*=\s*["']([^"']+)["'][^>]*>""",
    re.IGNORECASE,
)

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp"}

KINDLE_CSS = (
    "body{font-family:serif;line-height:1.45;}"
    "h1,h2,h3{page-break-before:avoid;}"
    "blockquote{margin:1em 0;padding-left:1em;border-left:3px solid #444;}"
    "code,pre{font-family:monospace;font-size:0.9em;}"
    "p{margin:0.6em 0;}"
    "img{max-width:100%;height:auto;display:block;margin:1em auto;}"
    "figure{margin:1em 0;text-align:center;}"
    "figcaption{font-size:0.9em;color:#444;margin-top:0.4em;}"
)


def read_meta(folder: Path) -> dict:
    meta_path = folder / "meta.json"
    if meta_path.exists():
        return json.loads(meta_path.read_text(encoding="utf-8"))
    return {"ticker": folder.name, "companyName": folder.name}


def collect_markdown(folder: Path) -> list[tuple[str, Path]]:
    if (folder / "book.md").exists():
        return [("Full curriculum", folder / "book.md")]
    chapters: list[tuple[str, Path]] = []
    for name in CHAPTER_ORDER:
        path = folder / name
        if path.exists():
            title = name.replace(".md", "").replace("-", " ").title()
            chapters.append((title, path))
    if not chapters:
        md_files = sorted(
            p for p in folder.glob("*.md") if p.name not in {"grading-report.md"}
        )
        chapters = [(p.stem, p) for p in md_files]
    if not chapters:
        raise SystemExit(f"No markdown chapters found in {folder}")
    return chapters


def strip_md_heading(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        return "\n".join(lines[1:]).lstrip() + "\n"
    return text


def is_remote_url(src: str) -> bool:
    return bool(re.match(r"^(https?|data|ftp):", src, re.IGNORECASE))


def extract_image_refs(md: str) -> list[str]:
    """Return image source paths/URLs referenced in Markdown or HTML."""
    refs: list[str] = []
    seen: set[str] = set()
    for match in MD_IMAGE_RE.finditer(md):
        src = match.group(2).strip()
        if src and src not in seen:
            seen.add(src)
            refs.append(src)
    for match in HTML_IMG_SRC_RE.finditer(md):
        src = match.group(1).strip()
        if src and src not in seen:
            seen.add(src)
            refs.append(src)
    return refs


def resolve_image_path(src: str, md_path: Path, folder: Path) -> Path | None:
    """Resolve a local image path relative to the markdown file, then the folder."""
    if is_remote_url(src):
        return None
    # Strip optional query/fragment from local paths (rare in MD, safe)
    cleaned = urllib.parse.unquote(src.split("?")[0].split("#")[0])
    candidates = [
        (md_path.parent / cleaned).resolve(),
        (folder / cleaned).resolve(),
    ]
    folder_resolved = folder.resolve()
    for candidate in candidates:
        try:
            candidate.relative_to(folder_resolved)
        except ValueError:
            # Allow images just outside folder if they exist (e.g. shared assets)
            pass
        if candidate.is_file():
            return candidate
    return None


def media_type_for(path: Path) -> str:
    guessed, _ = mimetypes.guess_type(str(path))
    if guessed:
        return guessed
    ext = path.suffix.lower()
    return {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".webp": "image/webp",
        ".svg": "image/svg+xml",
        ".bmp": "image/bmp",
    }.get(ext, "application/octet-stream")


def collect_images(
    chapters: list[tuple[str, Path]], folder: Path
) -> tuple[dict[str, Path], list[str]]:
    """Map original markdown src → absolute local Path. Return warnings for misses."""
    mapping: dict[str, Path] = {}
    warnings: list[str] = []
    for _, md_path in chapters:
        text = md_path.read_text(encoding="utf-8")
        for src in extract_image_refs(text):
            if src in mapping:
                continue
            if is_remote_url(src):
                warnings.append(
                    f"Skipping remote image (not embedded): {src} (from {md_path.name})"
                )
                continue
            resolved = resolve_image_path(src, md_path, folder)
            if resolved is None:
                warnings.append(f"Image not found: {src} (from {md_path.name})")
                continue
            mapping[src] = resolved
    return mapping, warnings


def rewrite_md_images(md: str, src_to_epub: dict[str, str]) -> str:
    """Rewrite Markdown/HTML image sources to EPUB-internal paths."""

    def md_repl(match: re.Match[str]) -> str:
        alt, src, title = match.group(1), match.group(2), match.group(3)
        new_src = src_to_epub.get(src, src)
        if title:
            return f'![{alt}]({new_src} "{title}")'
        return f"![{alt}]({new_src})"

    def html_repl(match: re.Match[str]) -> str:
        full = match.group(0)
        src = match.group(1)
        new_src = src_to_epub.get(src, src)
        if new_src == src:
            return full
        return full.replace(src, new_src, 1)

    rewritten = MD_IMAGE_RE.sub(md_repl, md)
    rewritten = HTML_IMG_SRC_RE.sub(html_repl, rewritten)
    return rewritten


def md_to_simple_html(md: str) -> str:
    """Minimal Markdown → HTML for offline EPUB (headings, lists, quotes, code, images)."""
    try:
        import markdown as md_lib  # type: ignore

        return md_lib.markdown(
            md,
            extensions=["extra", "sane_lists", "tables", "fenced_code"],
        )
    except Exception:
        pass

    out: list[str] = []
    in_ul = False
    in_ol = False
    in_code = False
    para: list[str] = []

    def flush_para() -> None:
        nonlocal para
        if para:
            out.append("<p>" + " ".join(para) + "</p>")
            para = []

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def format_inline(text: str) -> str:
        # Images first (before escaping would break paths)
        def img_sub(m: re.Match[str]) -> str:
            alt = html.escape(m.group(1))
            src = html.escape(m.group(2), quote=True)
            title = m.group(3)
            title_attr = f' title="{html.escape(title, quote=True)}"' if title else ""
            return f'<img src="{src}" alt="{alt}"{title_attr} />'

        text = MD_IMAGE_RE.sub(img_sub, text)
        # Escape remaining text carefully: split on already-built <img> tags
        parts = re.split(r"(<img\b[^>]*>)", text)
        built: list[str] = []
        for part in parts:
            if part.startswith("<img"):
                built.append(part)
            else:
                escaped = html.escape(part)
                escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
                escaped = re.sub(r"`(.+?)`", r"<code>\1</code>", escaped)
                escaped = re.sub(
                    r"\[([^\]]+)\]\(([^)]+)\)",
                    r'<a href="\2">\1</a>',
                    escaped,
                )
                built.append(escaped)
        return "".join(built)

    for raw in md.splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            flush_para()
            close_lists()
            if in_code:
                out.append("</code></pre>")
                in_code = False
            else:
                out.append("<pre><code>")
                in_code = True
            continue
        if in_code:
            out.append(html.escape(line))
            continue
        if not line.strip():
            flush_para()
            close_lists()
            continue
        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            flush_para()
            close_lists()
            level = len(heading.group(1))
            out.append(f"<h{level}>{html.escape(heading.group(2))}</h{level}>")
            continue
        if re.match(r"^>\s?", line):
            flush_para()
            close_lists()
            out.append(
                f"<blockquote><p>{html.escape(line.lstrip('> ').strip())}</p></blockquote>"
            )
            continue
        if re.match(r"^[-*]\s+", line):
            flush_para()
            if in_ol:
                out.append("</ol>")
                in_ol = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            item = re.sub(r"^[-*]\s+", "", line)
            out.append(f"<li>{format_inline(item)}</li>")
            continue
        if re.match(r"^\d+\.\s+", line):
            flush_para()
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            item = re.sub(r"^\d+\.\s+", "", line)
            out.append(f"<li>{format_inline(item)}</li>")
            continue
        # Standalone image line → block figure
        img_only = MD_IMAGE_RE.fullmatch(line.strip())
        if img_only:
            flush_para()
            close_lists()
            out.append(f"<p>{format_inline(line.strip())}</p>")
            continue
        close_lists()
        para.append(format_inline(line))

    flush_para()
    close_lists()
    if in_code:
        out.append("</code></pre>")
    return "\n".join(out)


def build_with_pandoc(folder: Path, out: Path, meta: dict) -> bool:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        return False
    chapters = collect_markdown(folder)
    title = f"{meta.get('companyName', folder.name)} ({meta.get('ticker', folder.name)})"
    # Resource path lets pandoc resolve relative images from chapter / folder / images/
    resource_path = f"{folder}:{folder / 'images'}:{folder / 'assets'}"
    args = [
        pandoc,
        "-f",
        "markdown",
        "-t",
        "epub3",
        "-o",
        str(out),
        f"--metadata=title:{title}",
        "--metadata=creator:Stock Market Mastery",
        "--metadata=language:en",
        "--toc",
        "--toc-depth=2",
        f"--resource-path={resource_path}",
    ]
    args.extend(str(p) for _, p in chapters)
    subprocess.run(args, check=True, cwd=str(folder))
    return True


def _epub_image_name(path: Path, used: set[str]) -> str:
    """Stable unique EPUB-internal filename under images/."""
    base = path.name
    # Sanitize for EPUB paths
    safe = re.sub(r"[^\w.\-]+", "_", base)
    name = safe
    stem = Path(safe).stem
    suffix = Path(safe).suffix
    n = 1
    while name in used:
        name = f"{stem}_{n}{suffix}"
        n += 1
    used.add(name)
    return f"images/{name}"


def build_with_ebooklib(folder: Path, out: Path, meta: dict) -> None:
    try:
        from ebooklib import epub  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            "Neither pandoc nor ebooklib is available.\n"
            "Install one of:\n"
            "  brew install pandoc\n"
            "  pip install ebooklib markdown\n"
            "  ./scripts/setup-epub-env.sh\n"
        ) from exc

    chapters = collect_markdown(folder)
    image_map, warnings = collect_images(chapters, folder)
    for warn in warnings:
        print(warn, file=sys.stderr)

    book = epub.EpubBook()
    ticker = meta.get("ticker", folder.name)
    company = meta.get("companyName", ticker)
    book.set_identifier(f"stock-market-mastery-{ticker}")
    book.set_title(f"{company} ({ticker}) — Stock Market Mastery")
    book.set_language("en")
    book.add_author("Stock Market Mastery")

    css = epub.EpubItem(
        uid="style",
        file_name="style/kindle.css",
        media_type="text/css",
        content=KINDLE_CSS.encode("utf-8"),
    )
    book.add_item(css)

    # Embed images once; map original src → EPUB path
    src_to_epub: dict[str, str] = {}
    used_names: set[str] = set()
    embedded_paths: set[Path] = set()
    for src, abs_path in image_map.items():
        if abs_path in embedded_paths:
            # Same file referenced under different relative paths
            for existing_src, existing_epub in src_to_epub.items():
                if image_map.get(existing_src) == abs_path:
                    src_to_epub[src] = existing_epub
                    break
            continue
        epub_name = _epub_image_name(abs_path, used_names)
        item = epub.EpubItem(
            uid=f"img_{len(embedded_paths) + 1}",
            file_name=epub_name,
            media_type=media_type_for(abs_path),
            content=abs_path.read_bytes(),
        )
        book.add_item(item)
        src_to_epub[src] = epub_name
        embedded_paths.add(abs_path)

    spine = ["nav"]
    toc = []
    for idx, (title, path) in enumerate(chapters, start=1):
        md = path.read_text(encoding="utf-8")
        raw = md if path.name == "book.md" else strip_md_heading(md)
        raw = rewrite_md_images(raw, src_to_epub)
        body = md_to_simple_html(raw)
        if not body.strip():
            body = f"<p>{html.escape(md[:2000])}</p>"
        chapter = epub.EpubHtml(title=title, file_name=f"chap_{idx:02d}.xhtml", lang="en")
        # ebooklib wraps this in <html>/<body>; pass fragment only.
        chapter.content = f"<h1>{html.escape(title)}</h1>\n{body}"
        chapter.add_item(css)
        book.add_item(chapter)
        spine.append(chapter)
        toc.append(chapter)

    book.toc = tuple(toc)
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = spine
    epub.write_epub(str(out), book)

    if embedded_paths:
        print(f"Embedded {len(embedded_paths)} image(s)", file=sys.stderr)


def validate_epub(path: Path, expect_images: bool = False) -> None:
    if not path.exists() or path.stat().st_size < 1000:
        raise SystemExit(f"EPUB looks empty or missing: {path}")
    with zipfile.ZipFile(path, "r") as zf:
        names = zf.namelist()
        if "mimetype" not in names:
            raise SystemExit("Invalid EPUB: missing mimetype")
        if not any(n.endswith(".opf") for n in names):
            raise SystemExit("Invalid EPUB: missing OPF package document")
        if expect_images:
            image_files = [
                n
                for n in names
                if Path(n).suffix.lower() in IMAGE_EXTENSIONS
            ]
            if not image_files:
                raise SystemExit("EPUB validation failed: expected embedded images, found none")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path, help="Company output folder, e.g. output/TSM")
    parser.add_argument("--out", type=Path, default=None, help="Output .epub path")
    args = parser.parse_args()
    folder = args.folder.resolve()
    if not folder.is_dir():
        raise SystemExit(f"Not a directory: {folder}")
    meta = read_meta(folder)
    out = args.out or (folder / "book.epub")
    out.parent.mkdir(parents=True, exist_ok=True)

    chapters = collect_markdown(folder)
    image_map, _ = collect_images(chapters, folder)
    expect_images = bool(image_map)

    # Prefer pandoc for higher-quality EPUB3
    try:
        if build_with_pandoc(folder, out, meta):
            validate_epub(out, expect_images=expect_images)
            print(f"Wrote {out} (pandoc)")
            return
    except subprocess.CalledProcessError as exc:
        print(f"pandoc failed ({exc}); falling back to ebooklib", file=sys.stderr)

    build_with_ebooklib(folder, out, meta)
    validate_epub(out, expect_images=expect_images)
    print(f"Wrote {out} (ebooklib)")


if __name__ == "__main__":
    main()
