"""
CP1404 Practical 07
Read guitars from CSV, display, sort, add new ones, and save back to CSV.
"""

from typing import List
from guitar import Guitar

FILENAME = "guitars.csv"


def main() -> None:
    """Coordinate loading, displaying, sorting, adding, and saving guitars."""
    guitars = load_guitars(FILENAME)
    print("These are the guitars from file:")
    display_guitars(guitars)

    print("\nGuitars sorted by year (oldest to newest):")
    guitars.sort()  # uses Guitar.__lt__
    display_guitars(guitars)

    print("\nAdd new guitars (blank name to finish):")
    new_guitars = prompt_for_new_guitars()
    if new_guitars:
        guitars.extend(new_guitars)
        print("\nAll guitars including new ones, sorted by year:")
        guitars.sort()
        display_guitars(guitars)
        save_guitars(FILENAME, guitars)
        print(f"\nSaved {len(guitars)} guitars to {FILENAME}")
    else:
        print("\nNo new guitars added.")


def load_guitars(filename: str) -> List[Guitar]:
    """Load guitars from a CSV file (Name,Year,Cost)."""
    guitars: List[Guitar] = []
    try:
        with open(filename, "r", encoding="utf-8") as in_file:
            for line in in_file:
                line = line.strip()
                if not line:
                    continue
                name, year_text, cost_text = [part.strip() for part in line.split(",")]
                guitars.append(Guitar(name, int(year_text), float(cost_text)))
    except FileNotFoundError:
        # Start with an empty list if the file doesn't exist yet
        pass
    return guitars


def display_guitars(guitars: List[Guitar]) -> None:
    """Print guitars in a numbered list, tagging vintage ones."""
    if not guitars:
        print("(no guitars)")
        return
    for i, guitar in enumerate(guitars, start=1):
        vintage_tag = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar}{vintage_tag}")


def prompt_for_new_guitars() -> List[Guitar]:
    """Interactively collect new guitars from the user."""
    new_guitars: List[Guitar] = []
    name = input("Name: ").strip()
    while name:
        year = _get_int("Year: ")
        cost = _get_float("Cost: $")
        new_guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.")
        name = input("Name: ").strip()
    return new_guitars


def save_guitars(filename: str, guitars: List[Guitar]) -> None:
    """Write all guitars to CSV (Name,Year,Cost)."""
    with open(filename, "w", encoding="utf-8") as out_file:
        for g in guitars:
            out_file.write(f"{g.name},{g.year},{g.cost}\n")


def _get_int(prompt: str) -> int:
    """Get a valid integer from input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input; enter a whole number.")


def _get_float(prompt: str) -> float:
    """Get a valid float from input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input; enter a number (e.g., 1234.56).")


if __name__ == "__main__":
    main()
