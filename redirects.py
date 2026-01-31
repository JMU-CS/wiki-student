"""Generate apache redirect rules by following page history in git log."""

import subprocess
from pathlib import Path

# Last change on DokuWiki before the migration
BASE_COMMIT = "45ced82"

# Path to Markdown source files on the site
DOCS_ROOT = "docs"


def run(cmd: list[str]) -> list[str]:
    """Run command with arguments and return its output."""
    return subprocess.check_output(cmd, text=True, stderr=subprocess.DEVNULL).splitlines()


def current_pages() -> list[Path]:
    """Get relative paths to all Markdown pages in docs."""
    return [Path(p) for p in run(["git", "ls-files", DOCS_ROOT]) if p.endswith(".md")]


def path_at_base_commit(path: Path) -> Path | None:
    """Get relative path of page at BASE_COMMIT if existed."""

    # Get the old version of the path
    output = run([
        "git", "log", f"{BASE_COMMIT}..HEAD",
        "--follow", "--name-status", "--format=",
        "--", str(path)
    ])

    # Path on last line, second word
    old = output[-1].split()[1]

    # Verify the path actually existed
    try:
        run(["git", "cat-file", "-e", f"{BASE_COMMIT}:{old}"])
    except subprocess.CalledProcessError:
        return None

    return DOCS_ROOT / Path(old)


def path_to_url(path: Path, index_name: str) -> str:
    """Convert a source file path to a normalized url."""
    path = path.relative_to(DOCS_ROOT)
    if path.name == index_name:
        return str(path.parent)
    return str(path.with_suffix(""))


def main():
    for new_path in current_pages():
        old_path = path_at_base_commit(new_path)
        if not old_path:
            continue

        # Convert the source file paths to urls
        old_url = path_to_url(old_path, "start.txt")
        new_url = path_to_url(new_path, "index.md")

        # Emit rule only if the path has changed
        if old_url != new_url:
            # The old URL should not end with a slash, because Apache matches prefixes.
            # The new URL should end with a slash, because it represents a directory.
            print(f"Redirect 301 /{old_url} /{new_url}/")


if __name__ == "__main__":
    main()
