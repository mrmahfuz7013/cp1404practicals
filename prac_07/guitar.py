"""
CP1404 Practical 07
Guitar class (supports sorting by year)
"""

from dataclasses import dataclass

CURRENT_YEAR = 2025


@dataclass
class Guitar:
    """Represent a guitar with a name, year and cost."""
    name: str
    year: int
    cost: float

    def __str__(self) -> str:
        """Return a nicely formatted string for a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def is_vintage(self) -> bool:
        """Return True if the guitar is 50 years or older."""
        return CURRENT_YEAR - self.year >= 50

    def __lt__(self, other: "Guitar") -> bool:
        """Order guitars by year (oldest first)."""
        return self.year < other.year
