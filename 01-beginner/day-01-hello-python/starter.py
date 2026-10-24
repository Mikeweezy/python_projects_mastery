"""Day 01 - Hello, Python! | Greeting Bot

Built on Day 1: a bot that meets the user, does a little math,
and comments on their favorite language.

Concepts: print, input, variables, f-strings, int(), while, if/else.
Run with: python starter.py
"""

WIDTH = 40  # banner width; change it and see what happens


def draw_banner() -> None:
    """Print the welcome banner."""
    print("=" * WIDTH)
    print("WELCOME TO THE GREETING BOT".center(WIDTH))
    print("=" * WIDTH)


def ask_age() -> int:
    """Keep asking until the user types a whole number, then return it."""
    age_text = input("How old are you? ").strip()
    while not age_text.isdigit():
        print("That doesn't look like a whole number. Try again.")
        age_text = input("How old are you? ").strip()
    return int(age_text)  # only now is int() safe


def main() -> None:
    # 1. welcome banner: "=" * WIDTH repeats the string; .center() pads it
    draw_banner()

    # 2. meet the user
    # input() always returns a string; .strip() removes stray spaces
    name = input("\nWhat's your name? ").strip()
    age = ask_age()
    language = input("Favorite programming language? ").strip()

    # 3. greet by name: f-strings put variables directly into text
    print(f"\nHello, {name}! Welcome to your Python journey.")

    # 4. a little math (requirement: age in days, leap years ignored)
    days_alive = age * 365
    print(f"That works out to about {days_alive:,} days.")

    # bonus 2: years until 100
    years_to_100 = 100 - age
    if years_to_100 > 0:
        print(f"At {age}, you will turn 100 in {years_to_100} years.")
    else:
        print("You are 100 or older.")

    # 5. the language check: .lower() makes it case-insensitive
    if language.lower() == "python":
        print("Good choice. Python is a great first language.")
    else:
        print(f"{language} is a solid choice. Give Python a try too.")

    # 6. sign off
    print("\n" + "=" * WIDTH)
    print("Thanks for stopping by. See you tomorrow for Day 2.".center(WIDTH))
    print("=" * WIDTH)


if __name__ == "__main__":
    # def only defines a function; nothing runs until it is called.
    # This if means "run main() only when executed directly".
    main()
