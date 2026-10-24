# Day 01 - Hello, Python! (Greeting Bot)

**Phase:** Beginner · **Concepts:** `print` · `input` · variables · f-strings · basic math · `if` · **Date:** 2026-10-24

## Today's goal

Build your first interactive program: a greeting bot that asks for the user's
name, age and favorite programming language, then replies with a personalized
greeting and a little math.

## Requirements

- [ ] Print a welcome banner (multiple lines is fine)
- [ ] Ask the user's **name**, **age** and **favorite programming language** with `input()`
- [ ] Greet the user **by name** using an f-string
- [ ] Calculate and print their age in **days** (ignore leap years: `age * 365`)
- [ ] If their favorite language is **Python**, acknowledge it; otherwise print a friendly alternative message

## Hints

- `input("prompt: ")` always returns a **string**; convert with `int()` when you need a number
- f-strings: `f"Hello, {name}!"`, and expressions work inside the braces: `f"{age * 365}"`
- Format large numbers with a comma: `f"{days:,}"`
- Compare case-insensitively with `.lower()`; clean whitespace with `.strip()`
- Docs: [print](https://docs.python.org/3/library/functions.html#print) · [input](https://docs.python.org/3/library/functions.html#input)

## Acceptance criteria

- [ ] `python starter.py` runs without errors
- [ ] Works whether the user types `Python`, `python`, or `" PYTHON "`
- [ ] Committed as `Day 1: greeting bot`

## Bonus challenges

1. Validate the age: if the input isn't a number, ask again (see `str.isdigit()`; `try/except` arrives on Day 19)
2. Add a "years until you turn 100" line
3. Make the banner fancier with centered text or different border characters

---

When done, compare with [`solution.py`](solution.py), fill in [`notes.md`](notes.md), and tick Day 1 in [`PROGRESS.md`](../../PROGRESS.md).
