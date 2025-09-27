"""CP1404 Practical 02 - score_menu.py
Menu program for scores using functions.
"""

from score import determine_status

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
MIN_SCORE = 0
MAX_SCORE = 100


def main():
    """Run the score menu program."""
    # Get an initial valid score BEFORE the menu loop (as required)
    score = get_valid_score(MIN_SCORE, MAX_SCORE)

    print(MENU)
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score(MIN_SCORE, MAX_SCORE)
        elif choice == "P":
            print(determine_status(score))
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").strip().upper()
    print("Farewell.")


def get_valid_score(min_score: int, max_score: int) -> float:
    """Prompt until a numeric score within [min_score, max_score] is entered."""
    text = f"Score ({min_score}-{max_score}): "
    raw = input(text).strip()
    while True:
        try:
            value = float(raw)
            if min_score <= value <= max_score:
                return value
            print(f"Score must be between {min_score} and {max_score}.")
        except ValueError:
            print("Enter a valid number.")
        raw = input(text).strip()


main()
