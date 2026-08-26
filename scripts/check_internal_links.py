#!/usr/bin/env python3
"""
Checks that every internal link (in-page #anchor, or a relative link to
another file in this repo) actually resolves. Deliberately does NOT touch
the network, so it can't flake on external hosts (fonts.googleapis.com,
images.pexels.com, etc.) inside CI — see docs/LAUNCH_CHECKLIST.md #39/#36.

Usage: python3 scripts/check_internal_links.py file1.html file2.html ...
Exits non-zero (and prints each broken link) if anything is unresolved.
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

HREF_RE = re.compile(r'href="([^"]*)"')
ID_RE = re.compile(r'\bid="([^"]+)"')


class LinkCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "href" in attrs:
            self.hrefs.append(attrs["href"])
        if "id" in attrs:
            self.ids.add(attrs["id"])


def check_file(path: Path, all_ids_by_file):
    text = path.read_text(encoding="utf-8")
    collector = LinkCollector()
    collector.feed(text)

    problems = []
    for href in collector.hrefs:
        if href.startswith(("http://", "https://", "mailto:", "tel:")):
            continue  # external — not our concern here
        if href in ("", "#"):
            problems.append(f'bare "{href}" href (dead link)')
            continue
        if href.startswith("#"):
            anchor = href[1:]
            if anchor not in collector.ids:
                problems.append(f'#{anchor} has no matching id="{anchor}" in {path.name}')
            continue
        # relative file link, optionally with its own #fragment
        target_file, _, fragment = href.partition("#")
        target_path = (path.parent / target_file).resolve()
        if not target_path.exists():
            problems.append(f'links to missing file "{target_file}"')
            continue
        if fragment:
            target_ids = all_ids_by_file.get(target_path)
            if target_ids is not None and fragment not in target_ids:
                problems.append(f'links to {target_file}#{fragment}, no such id in {target_file}')
    return problems


def main(argv):
    if not argv:
        print("usage: check_internal_links.py file1.html [file2.html ...]")
        return 2

    files = [Path(p) for p in argv]

    # First pass: collect every id defined in every file we were given.
    all_ids_by_file = {}
    for f in files:
        collector = LinkCollector()
        collector.feed(f.read_text(encoding="utf-8"))
        all_ids_by_file[f.resolve()] = collector.ids

    had_problems = False
    for f in files:
        problems = check_file(f, all_ids_by_file)
        if problems:
            had_problems = True
            print(f"\n{f}:")
            for p in problems:
                print(f"  - {p}")

    if had_problems:
        print("\nInternal link check FAILED.")
        return 1

    print(f"Internal link check passed for {len(files)} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
