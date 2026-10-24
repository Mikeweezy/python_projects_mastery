"""Day 01 - Hello, Python! | Solution

A greeting bot: meets the user, does some math, comments on their language.
Run with: python solution.py

Note: input is not validated here on purpose; bulletproofing input is Day 19.
"""


def main() -> None:
    print("=" * 40)
    print("WELCOME TO THE GREETING BOT".center(40))
    print("=" * 40)

    name = input("What's your name? ").strip()
    age = int(input("How old are you? ").strip())
    language = input("Favorite programming language? ").strip()

    print(f"\nHello, {name}! Welcome to your Python journey.")
    print(f"That works out to about {age * 365:,} days.")

    if language.lower() == "python":
        print("Good choice. Python is a great first language.")
    else:
        print(f"{language} is a solid choice. Give Python a try too.")

    years_to_100 = 100 - age
    if years_to_100 > 0:
        print(f"At {age}, you will turn 100 in {years_to_100} years.")
    else:
        print("You are 100 or older.")


if __name__ == "__main__":
    main()
