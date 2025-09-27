"""CP1404 Practical 02 -
Fixed program to determine score status, with function
"""

import random  # for the random score part

def main():
    """Get a numeric score and display its status, then show a random score result."""
    score = float(input("Enter score: "))
    print(determine_status(score))

    # Extra requirement: also generate a random score (0–100 inclusive) and print its result
    random_score = random.randint(0, 100)
    print(f"Random score {random_score}: {determine_status(random_score)}")


def determine_status(score):
    """Return the status for a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
