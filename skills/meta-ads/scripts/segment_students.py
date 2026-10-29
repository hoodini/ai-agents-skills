#!/usr/bin/env python3
"""Turn course-platform student exports into sales segments (who to sell what next).

Input: one JSON file per course, as returned by a course platform's "list course students"
call (for Schooler's MCP: `list_course_students`, which returns `students` = enrolled/paid and
`interested_students` = signed up but did not pay). Large MCP results are usually saved to a file
by the client; pass those files here instead of pasting personal data into the conversation.

  python scripts/segment_students.py --out ./private/segments \
      --course "Course A=./course_a.json" --course "Course B=./course_b.json"

Prints only COUNTS (safe to show the user), and writes one CSV per segment (name,email,phone)
into --out, ready to import into the mailing tool:
  - <course>__signed_up_not_paid       interested, never enrolled in that course
  - <course>__not_started               enrolled with 0% progress (activation email)
  - <A>__students_without__<B>          cross-sell: bought A, not B (for every ordered pair)

Keep --out outside version control: these files hold students' personal data.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


def load(path: str) -> dict:
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    # Accept the bare payload, {"data": {...}}, or an MCP content wrapper.
    if isinstance(raw, dict) and "data" in raw:
        raw = raw["data"]
    if isinstance(raw, list) and raw and isinstance(raw[0], dict) and "text" in raw[0]:
        raw = json.loads(raw[0]["text"]).get("data", {})
    return raw


def rows(people: list[dict]) -> dict[str, tuple]:
    out = {}
    for p in people or []:
        email = (p.get("student_email") or "").strip().lower()
        if email:
            out[email] = ((p.get("student_name") or "").strip(), email, p.get("student_phone") or "")
    return out


def slug(s: str) -> str:
    return re.sub(r"[^\w-]+", "-", s.strip()).strip("-").lower() or "course"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--course", action="append", required=True, help='"Name=path/to/students.json" (repeat)')
    ap.add_argument("--out", required=True, help="directory for the CSVs (keep it out of git)")
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    courses = {}
    for spec in args.course:
        name, _, path = spec.partition("=")
        d = load(path)
        enrolled = rows(d.get("students"))
        interested = {k: v for k, v in rows(d.get("interested_students")).items() if k not in enrolled}
        not_started = {e: rows([s])[e] for s in d.get("students") or []
                       if (e := (s.get("student_email") or "").strip().lower())
                       and float(s.get("lesson_complete_percentage") or 0) == 0}
        courses[name] = {"enrolled": enrolled, "interested": interested, "not_started": not_started}

    def write(fname: str, data: dict) -> int:
        with open(out / f"{fname}.csv", "w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f)
            w.writerow(["name", "email", "phone"])
            w.writerows(data.values())
        return len(data)

    summary = {}
    for name, c in courses.items():
        s = slug(name)
        summary[name] = {
            "enrolled": len(c["enrolled"]),
            "signed_up_not_paid": write(f"{s}__signed_up_not_paid", c["interested"]),
            "not_started": write(f"{s}__not_started", c["not_started"]),
        }
    for a, ca in courses.items():
        for b, cb in courses.items():
            if a != b:
                seg = {k: v for k, v in ca["enrolled"].items() if k not in cb["enrolled"]}
                summary[f"{a} -> without {b}"] = write(f"{slug(a)}__students_without__{slug(b)}", seg)

    print(json.dumps({"ok": True, "out": str(out), "counts": summary}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
