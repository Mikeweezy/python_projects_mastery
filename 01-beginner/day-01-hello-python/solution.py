"""Day 01 — Hello, Python! | Solution

A friendly greeting bot: meets the user, does some math, tells a joke.
Run with: python solution.py

Note: input is not validated yet on purpose — bulletproofing input is Day 19!
"""


def main() -> None:
    print("=" * 40)
    print("     🤖  WELCOME TO THE GREETING BOT")
    print("=" * 40)

    name = input("What's your name? ").strip()
    age = int(input("How old are you? ").strip())
    language = input("Favorite programming language? ").strip()

    print(f"\nHello, {name}! Welcome to your Python journey. 🚀")
    print(f"Fun fact: you've been alive for about {age * 365:,} days.")

    if language.lower() == "python":
        print("Excellent taste — Python is the perfect choice for this journey! 🐍")
    else:
        print(f"{language} is cool, but give Python a week — you might switch sides. 😏")

    years_to_100 = 100 - age
    if years_to_100 > 0:
        print(f"Only {years_to_100} more years until you turn 100. Start coding now!")
    else:
        print("You're 100+?! Officially the wisest coder here. 🧙")


if __name__ == "__main__":
    main()
