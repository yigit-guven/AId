import json
import os
import re
import sys

def get_notes(changelog_path: str, version: str) -> str:
    if not os.path.exists(changelog_path):
        return ""

    with open(changelog_path, encoding="utf-8") as f:
        text = f.read()

    match = re.search(rf"(?m)^##\s+\[?v?{re.escape(version.lstrip('v'))}\]?(?:\s+-\s+[^\n]+)?\s*$", text)
    if not match:
        return ""

    start = match.end()
    nxt = re.search(r"(?m)^##\s+\[?[0-9a-zA-Zv\.\-]+\]?", text[start:])
    return (text[start:start + nxt.start()] if nxt else text[start:]).strip()

def sync_citation(version: str):
    if not os.path.exists("CITATION.md"):
        return
    with open("CITATION.md", encoding="utf-8") as f:
        content = f.read()
    content = re.sub(r"version = \{[^\}]+\}", f"version = {{{version}}}", content)
    content = re.sub(r"\(Version [^\)]+\)", f"(Version {version})", content)
    with open("CITATION.md", "w", encoding="utf-8") as f:
        f.write(content)

def sync_security(version: str):
    if not os.path.exists("SECURITY.md"):
        return
    # Determine branch series (e.g. 0.1.x or 1.0.x)
    parts = version.split(".")
    major_minor = f"{parts[0]}.{parts[1]}.x" if len(parts) >= 2 else f"{parts[0]}.x"
    cutoff = f"{parts[0]}.{parts[1]}.0" if len(parts) >= 2 else f"{parts[0]}.0.0"

    with open("SECURITY.md", encoding="utf-8") as f:
        content = f.read()

    table_pattern = r"(\| Version \| Supported\s+\|\n\| -+ \| -+ \|\n)(\| [^\n]+\|\n\| [^\n]+\|)"
    replacement = rf"\g<1>| {major_minor:<7} | :white_check_mark: |\n| < {cutoff:<5} | :x:                |"
    new_content = re.sub(table_pattern, replacement, content)

    with open("SECURITY.md", "w", encoding="utf-8") as f:
        f.write(new_content)

def main():
    if not os.path.exists("RELEASE.json"):
        sys.exit("RELEASE.json not found")

    with open("RELEASE.json", encoding="utf-8") as f:
        cfg = json.load(f)

    version = str(cfg.get("version", "")).strip()
    if not version:
        sys.exit("Missing version in RELEASE.json")

    tag = f"v{version.lstrip('v')}"
    prerelease = cfg.get("prerelease", any(k in version.lower() for k in ["-rc", "-alpha", "-beta", "-dev"]))
    title = cfg.get("title") or f"Release {tag}"

    # Auto sync version-dependent documents
    sync_citation(version)
    sync_security(version)

    notes = get_notes("CHANGELOG.md", version) or f"Release {tag}"
    with open("release_notes.md", "w", encoding="utf-8") as f:
        f.write(notes + "\n")

    gh_out = os.environ.get("GITHUB_OUTPUT")
    if gh_out:
        with open(gh_out, "a", encoding="utf-8") as f:
            f.write(f"version={version}\ntag_name={tag}\nrelease_title={title}\nis_prerelease={'true' if prerelease else 'false'}\nnotes_path=release_notes.md\n")

if __name__ == "__main__":
    main()
