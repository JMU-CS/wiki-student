#!/usr/bin/env python3
"""
Post-build script that adds or updates a last-modified footer in each HTML
page under site/, using Git history of the corresponding Markdown source.
Commits on SKIP_DATE are ignored, and history is followed across renames.
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
            "--format=%n%n%ad by %an (%h)",
            "--date=format:%Y-%m-%d %H:%M",
            "--name-status",
            "--", str(src_path),
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    # The %n%n in --format puts two blank lines between each commit
    blocks = result.stdout.strip().split("\n\n\n")
    if not blocks:
        return "Unknown"

    # Find the most recent commit that was an actual page edit
    for block in blocks:
        lines = block.splitlines()
        header = lines[0]

        # Skip commits on the original import date
        if header.startswith(SKIP_DATE):
            continue

        # Collect file status lines (e.g., R100, M, A)
        statuses = [
            line.split()[0]
            for line in lines[1:]
            if line and line[0].isalpha()
        ]

        # Ignore commits that were only renames
        if statuses and all(status.startswith("R") for status in statuses):
            continue

        return header

    # Fallback: return the most recent commit header
    return blocks[0].splitlines()[0]


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
