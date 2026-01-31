"""Generate apache redirect rules by following page history in the git log."""

import subprocess
from pathlib import Path

# Redirect window
SINCE = "6 months ago"

# Path to Markdown source files
DOCS_ROOT = "docs"


def run(cmd: list[str]) -> list[str]:
    """Run a command with arguments and return its output."""
    return subprocess.check_output(cmd, text=True).splitlines()


def current_pages() -> list[Path]:
    """Get relative paths to all current Markdown pages."""
    return [Path(p) for p in run(["git", "ls-files", DOCS_ROOT]) if p.endswith(".md")]


def previous_paths(path: Path) -> list[Path]:
    """Get all previous paths to the given Markdown page."""
    output = run([
        "git", "log", f"--since={SINCE}",
        "--follow", "--name-status", "--format=",
        "--", str(path)
    ])
    # Get the second word (old path) of each line with rename status
    return [Path(line.split()[1]) for line in output if line.startswith("R")]


def path_to_url(path: Path, index_name: str) -> str:
    """Convert a source file path to a normalized url."""
    # Remove docs root if present
    if path.is_relative_to(DOCS_ROOT):
        path = path.relative_to(DOCS_ROOT)
    # Remove index file if present
    if path.name == index_name:
        return str(path.parent)
    # Remove extension (txt or md)
    return str(path.with_suffix(""))


def main():
    rules: set[tuple[str, str]] = set()
    current_urls = {path_to_url(p, "index.md") for p in current_pages()}

    for new_path in current_pages():
        for old_path in previous_paths(new_path):
            # Convert the source file paths to urls
            old_url = path_to_url(old_path, "start.txt")
            new_url = path_to_url(new_path, "index.md")
            # Emit rule only if the path has changed and will not shadow an existing page
            if old_url != new_url and old_url not in current_urls:
                rules.add((old_url, new_url))

    for old_url, new_url in sorted(rules, key=lambda r: r[1]):
        # The old URL should not end with a slash, because Apache matches prefixes.
        # The new URL should end with a slash, because it represents a directory.
        print(f"Redirect 301 /{old_url} /{new_url}/")


if __name__ == "__main__":
    main()
