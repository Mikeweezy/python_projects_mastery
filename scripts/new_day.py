"""Scaffold a new day folder for the Python Daily Journey.

Usage:
    python scripts/new_day.py --phase 1 --day 2 --title "Mad Libs Generator" --concepts "strings,input"

Creates  01-beginner/day-02-mad-libs-generator/  containing README.md,
starter.py and notes.md generated from the files in templates/.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PHASES = {1: "01-beginner", 2: "02-intermediate", 3: "03-advanced", 4: "04-pro"}


def slugify(title: str) -> str:
    """Turn a title into a URL/day-folder friendly slug."""
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    if not slug:
        raise SystemExit("❌ Title must contain at least one letter or number.")
    return slug


def fill_template(template_name: str, values: dict[str, str]) -> str:
    """Read a template and replace {PLACEHOLDER} tokens with values."""
    text = (ROOT / "templates" / template_name).read_text(encoding="utf-8")
    for key, value in values.items():
        text = text.replace("{" + key + "}", value)
    return text


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold a new day folder.")
    parser.add_argument("--phase", type=int, required=True, choices=sorted(PHASES),
                        help="1=beginner, 2=intermediate, 3=advanced, 4=pro")
    parser.add_argument("--day", type=int, required=True, help="day number, e.g. 2")
    parser.add_argument("--title", required=True, help='e.g. "Mad Libs Generator"')
    parser.add_argument("--concepts", default="to be filled in",
                        help="comma-separated concepts, e.g. 'strings,input'")
    args = parser.parse_args()

    slug = slugify(args.title)
    day_dir = ROOT / PHASES[args.phase] / f"day-{args.day:02d}-{slug}"
    if day_dir.exists():
        raise SystemExit(f"❌ {day_dir} already exists — nothing was created.")
    day_dir.mkdir(parents=True)

    values = {
        "DAY": str(args.day),
        "TITLE": args.title,
        "PHASE": PHASES[args.phase],
        "CONCEPTS": args.concepts,
        "DATE": dt.date.today().isoformat(),
    }

    (day_dir / "README.md").write_text(fill_template("daily_readme_template.md", values), encoding="utf-8")
    (day_dir / "starter.py").write_text(fill_template("daily_starter_template.py", values), encoding="utf-8")
    (day_dir / "notes.md").write_text(fill_template("daily_notes_template.md", values), encoding="utf-8")

    print(f"✅ Created {day_dir.relative_to(ROOT)}")
    print("   → read README.md, code starter.py, then log it in PROGRESS.md")


if __name__ == "__main__":
    main()
