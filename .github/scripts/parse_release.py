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

    notes = get_notes("CHANGELOG.md", version) or f"Release {tag}"
    with open("release_notes.md", "w", encoding="utf-8") as f:
        f.write(notes + "\n")

    gh_out = os.environ.get("GITHUB_OUTPUT")
    if gh_out:
        with open(gh_out, "a", encoding="utf-8") as f:
            f.write(f"version={version}\ntag_name={tag}\nrelease_title={title}\nis_prerelease={'true' if prerelease else 'false'}\nnotes_path=release_notes.md\n")

if __name__ == "__main__":
    main()
