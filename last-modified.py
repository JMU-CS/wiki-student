#!/usr/bin/env python3
"""
Post-build script that adds or updates a last-modified footer in each HTML
page under site/, using Git history of the corresponding Markdown source.
Commits on IMPORT_DATE are ignored, and history is followed across renames.
"""

import re
import subprocess
from pathlib import Path

DOCS_DIR = Path("docs")
SITE_DIR = Path("site")

SKIP_DATE = "2026-01-05"
BASE_URL = "https://github.com/JMU-CS/wiki-student/commit/"


def find_source(base: Path) -> Path | None:

    direct = DOCS_DIR / f"{base}.md"
    if direct.is_file():
        return direct

    index = DOCS_DIR / base / "index.md"
    if index.is_file():
        return index


def git_stamp(src_path: Path) -> str:

    # Get all commits for this file, following renames
    result = subprocess.run(
        [
            "git", "log", "--follow",
            "--format=%ad by %an (%h)",
            "--date=format:%Y-%m-%d %H:%M",
            "--", str(src_path),
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    # Validate the output from git
    lines = result.stdout.strip().splitlines()
    if not lines:
        return "Unknown"

    # Find the most recent commit after/before the import date
    for line in lines:
        if not line.startswith(SKIP_DATE):
            return line

    # All commits on import date; return the most recent commit
    return lines[0]


def inject_footer(html: str, stamp: str, src_path: Path) -> str:

    # Build the footer, including commit url
    info, hash = stamp.split(" (")
    hash = hash[:-1]
    url = BASE_URL + hash
    stamp = f'{info} (<a href="{url}">{hash}</a>)'
    footer = f'<p class="last-modified">Last modified: {stamp}</p>\n'

    # Replace existing footer if present
    if 'class="last-modified"' in html:
        return re.sub(
            r"<p class=\"last-modified\">.*?</p>",
            footer,
            html,
            count=1,
            flags=re.DOTALL,
        )

    # Otherwise, insert before </article>
    return html.replace("</article>", f"{footer}</article>", 1)


def main() -> None:
    print("Running last-modified.py")
    for html_path in SITE_DIR.glob("*/**/index.html"):

        # Get the Markdown source file
        base = Path(*html_path.parts[1:-1])
        src = find_source(base)
        if src:
            print("+", src)
        else:
            print(base, "not found")
            continue

        # Add last-modified to html file
        stamp = git_stamp(src)
        html = html_path.read_text(encoding="utf-8")
        updated = inject_footer(html, stamp, src)
        html_path.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
