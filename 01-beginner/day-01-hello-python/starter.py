"""Day 01 — Hello, Python! | Greeting Bot

Built together on Day 1: a bot that meets you, does a little math,
and shares an opinion about your favorite language.

Concepts: print, input, variables, f-strings, int(), while, if/else.
Run me with:  python starter.py
"""

WIDTH = 40  # banner width — tweak me and see what happens!


def draw_banner() -> None:
    """Print the welcome banner."""
    print("=" * WIDTH)
    print("🤖 WELCOME TO THE GREETING BOT".center(WIDTH))
    print("=" * WIDTH)


def ask_age() -> int:
    """Keep asking until the user types a whole number, then return it."""
    age_text = input("How old are you? ").strip()
    while not age_text.isdigit():
        print("🤔 That doesn't look like a whole number — try again!")
        age_text = input("How old are you? ").strip()
    return int(age_text)  # only now is int() safe


def main() -> None:
    # --- 1. welcome banner ----------------------------------------------
    # "=" * WIDTH repeats the string; .center() pads it with spaces.
    draw_banner()

    # --- 2. meet the user --------------------------------------------------
    # input() shows a prompt, waits, and ALWAYS returns a string.
    # .strip() removes accidental leading/trailing spaces.
    name = input("\nWhat's your name? ").strip()
    age = ask_age()
    language = input("Favorite programming language? ").strip()

    # --- 3. greet by name (f-strings drop variables right into text) ------
    print(f"\nHello, {name}! Welcome to your Python journey. 🚀")

    # --- 4. a little math (requirement: age in days) -----------------------
    days_alive = age * 365  # leap years ignored, on purpose — we keep it simple
    print(f"Fun fact: you've been alive for about {days_alive:,} days.")

    # Bonus 2: years until 100
    years_to_100 = 100 - age
    if years_to_100 > 0:
        print(f"Only {years_to_100} years until you turn 100 — start coding! 💪")
    else:
        print("100 or older?! Officially the wisest coder here. 🧙")

    # --- 5. the language opinion -------------------------------------------
    # .lower() makes the check case-insensitive: "PYTHON" == "python"
    if language.lower() == "python":
        print("Excellent taste — Python is the perfect first language! 🐍")
    else:
        print(f"{language} is cool... but give Python a week — you might switch sides. 😏")

    # --- 6. sign off ---------------------------------------------------------
    print("\n" + "=" * WIDTH)
    print("Thanks for hanging out! See you tomorrow for Day 2. 👋".center(WIDTH))
    print("=" * WIDTH)


if __name__ == "__main__":
    # def only DEFINES a function (a named box of code); nothing runs until
    # it is CALLED. This special if means "run main() only when executed
    # directly" — more on that around Day 13.
    main()
