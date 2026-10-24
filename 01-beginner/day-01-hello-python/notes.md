# Day 01 Notes — Hello, Python! (Greeting Bot)

**Date:** 2026-10-24

## What I built

- A greeting bot: asks your name, age and favorite language, greets you by
  name, converts your age to days, counts years until 100, and judges your
  language choice (correctly, obviously).
- Two functions so far: `draw_banner()` and `ask_age()` (input validation!).

## New things I learned

- `input()` **always** returns a string — convert with `int()` before math.
- f-strings: `f"Hello, {name}"` — and `f"{days_alive:,}"` adds thousands separators.
- `"=" * 40` repeats a string; `.center(40)` lines text up inside a width.
- `.strip()` trims spaces; `.lower()` makes comparisons case-insensitive.
- `str.isdigit()` checks "is this a whole number?" **before** converting.
- `while` + `isdigit()` = keep asking until the input is valid (bonus #1).

## What tripped me up

- _(fill in whatever tripped YOU up — it's the most valuable part of this file!)_

## Questions to revisit

- What exactly does `if __name__ == "__main__":` do? (answer ~Day 13)
- How would I handle negative ages or huge numbers? (Day 19: bulletproof input)

## Confidence today (1–5)

- 4 — the pieces were small, but string-vs-number still feels new.
