#!/usr/bin/env python3
"""Repo-level consistency checks for agency-os.

Run from the repository root:  python3 scripts/validate_frontmatter.py

Checks every plugin skill, command, and agent:
- SKILL.md / command / agent files have parseable YAML frontmatter
- skills declare `name` + `description`; name matches the directory name
- descriptions stay under 1024 characters
- marketplace.json and every plugin.json are valid JSON with matching names
- every references/*.md link inside a SKILL.md points to a file that exists

Exit code 0 = clean, 1 = findings (printed).
"""
import json
import os
import re
import sys
import glob

try:
    import yaml
except ImportError:
    print("pyyaml missing — install with: pip install pyyaml")
    sys.exit(2)

FINDINGS = []


def check(cond, msg):
    if not cond:
        FINDINGS.append(msg)


def frontmatter(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---(\n|$)", text, re.S)
    if not m:
        return None, text
    return yaml.safe_load(m.group(1)), text


def main():
    # --- skills ---
    skills = sorted(glob.glob("plugins/*/skills/*/SKILL.md"))
    check(skills, "no skills found — run from the repository root")
    for path in skills:
        dirname = os.path.basename(os.path.dirname(path))
        try:
            fm, text = frontmatter(path)
        except yaml.YAMLError as e:
            FINDINGS.append(f"{path}: YAML error — {str(e).splitlines()[0]}")
            continue
        check(fm is not None, f"{path}: missing frontmatter")
        if fm is None:
            continue
        check(fm.get("name"), f"{path}: missing `name`")
        check(fm.get("description"), f"{path}: missing `description`")
        if fm.get("name"):
            check(fm["name"] == dirname,
                  f"{path}: name `{fm['name']}` != directory `{dirname}`")
        if fm.get("description"):
            check(len(fm["description"]) < 1024,
                  f"{path}: description {len(fm['description'])} chars (limit 1024)")
        # referenced files must exist
        base = os.path.dirname(path)
        for ref in re.findall(r"\]\((references/[^)#\s]+)\)", text):
            check(os.path.exists(os.path.join(base, ref)),
                  f"{path}: broken reference link `{ref}`")

    # --- commands & agents: frontmatter must parse ---
    for path in sorted(glob.glob("plugins/*/commands/*.md") +
                       glob.glob("plugins/*/agents/*.md")):
        try:
            fm, _ = frontmatter(path)
            check(fm is not None, f"{path}: missing frontmatter")
            if fm is not None:
                check(fm.get("description") or fm.get("name"),
                      f"{path}: frontmatter has neither description nor name")
        except yaml.YAMLError as e:
            FINDINGS.append(f"{path}: YAML error — {str(e).splitlines()[0]}")

    # --- manifests ---
    mp_path = ".claude-plugin/marketplace.json"
    mp = json.load(open(mp_path))
    declared = {p["name"] for p in mp["plugins"]}
    on_disk = {os.path.basename(p) for p in glob.glob("plugins/*")}
    check(declared == on_disk,
          f"marketplace/plugins mismatch — only in manifest: {declared - on_disk}, "
          f"only on disk: {on_disk - declared}")
    for pj in sorted(glob.glob("plugins/*/.claude-plugin/plugin.json")):
        d = json.load(open(pj))
        plugin_dir = pj.split("/")[1]
        check(d.get("name") == plugin_dir,
              f"{pj}: name `{d.get('name')}` != directory `{plugin_dir}`")
        check(d.get("version"), f"{pj}: missing version")

    if FINDINGS:
        print(f"FAIL — {len(FINDINGS)} finding(s):")
        for f in FINDINGS:
            print(f"  - {f}")
        sys.exit(1)
    n_skills = len(skills)
    print(f"OK — {n_skills} skills, all commands/agents/manifests consistent")


if __name__ == "__main__":
    main()
