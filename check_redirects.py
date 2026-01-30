"""Validate Apache Redirect rules in docs/.htaccess.

This script scans the docs/.htaccess file for Redirect 301 rules and
verifies that each redirect is valid and well-formed.

Checks performed:
- Ensures each Redirect rule uses the form:
    Redirect 301 /from/path /to/path/
- Verifies that the "from" path does NOT exist in the built site
  (redirects should only target removed or archived pages).
- Verifies that the "to" path DOES exist in the built site.
- Detects self-redirects (from == to) and comments out those lines
  to prevent redirect loops.

The built site is assumed to live in the "site/" directory, where
paths resolve to either:
- site/<path>/index.html
- site/<path>.html

This script is intended to be run after the site is built and is
suitable for use in CI to prevent broken or redundant redirects
from being deployed.

The .htaccess file is treated as the source of truth; this script
does not generate redirects, only validates and enforces policy.
"""

from pathlib import Path

HTACCESS_PATH = Path("docs/.htaccess")
SITE_ROOT = Path("site")


def path_exists(url_path: str) -> bool:
    """Check whether a URL path maps to a real file in the built site."""
    if not url_path.startswith("/"):
        return False
    rel = url_path.lstrip("/")
    candidates = [
        SITE_ROOT / rel / "index.html",
        SITE_ROOT / f"{rel}.html",
    ]
    return any(p.exists() for p in candidates)


def is_redirect_line(line: str) -> bool:
    stripped = line.strip().lstrip("#")
    return stripped.startswith("Redirect 301 ")


def parse_redirect(line: str):
    parts = line.strip().split()
    if len(parts) != 4:
        return None
    _, _, from_path, to_path = parts
    return from_path, to_path


def main():
    lines = HTACCESS_PATH.read_text().splitlines(keepends=True)
    new_lines: list[str] = []
    errors: list[str] = []
    commented: list[str] = []

    for lineno, line in enumerate(lines, start=1):
        if not is_redirect_line(line):
            new_lines.append(line)
            continue

        parsed = parse_redirect(line)
        if not parsed:
            errors.append(f"Line {lineno}: malformed Redirect rule")
            new_lines.append(line)
            continue

        from_path, to_path = parsed
        if path_exists(from_path):
            errors.append(f"Line {lineno}: FROM path exists in site: {from_path}")
        if not path_exists(to_path) and not to_path.startswith("/faculty"):
            errors.append(f"Line {lineno}: TO path does not exist in site: {to_path}")

        if from_path == to_path:
            if line.startswith("#"):
                new_lines.append(line)
            else:
                new_lines.append(f"#{line}")
            commented.append(str(lineno))
            continue

        new_lines.append(line)

    HTACCESS_PATH.write_text("".join(new_lines))
    print("Redirect validation complete")
    print()

    if commented:
        print("Commented out self-redirects on lines:", ", ".join(commented))
        print()

    if errors:
        print("Errors:")
        for err in errors:
            print(f"  - {err}")
        raise SystemExit(1)

    print("No errors found.")


if __name__ == "__main__":
    main()
