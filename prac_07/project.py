"""
CP1404 – Project class
Estimate: 45 mins
Actual: 53 mins

Represent a project and provide helpers for sorting/printing/file I/O.
"""

from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime


DATE_FORMAT = "%d/%m/%Y"  # file and display format (dd/mm/yyyy)


@dataclass
class Project:
    """Store details about one project."""
    name: str
    start_date: date
    priority: int
    cost_estimate: float
    percent_complete: int

    # ---------- Comparisons & helpers ----------

    def __lt__(self, other: "Project") -> bool:
        """Order projects by priority (lower number = higher priority)."""
        return self.priority < other.priority

    def is_complete(self) -> bool:
        """Return True if this project is 100% complete."""
        return self.percent_complete >= 100

    def start_date_str(self) -> str:
        """Return the start date formatted for display/file writing."""
        return self.start_date.strftime(DATE_FORMAT)

    def to_record(self) -> str:
        """Return a tab-delimited record suitable for saving to file."""
        return f"{self.name}\t{self.start_date_str()}\t{self.priority}\t{self.cost_estimate}\t{self.percent_complete}"

    # ---------- Constructors ----------

    @classmethod
    def from_record(cls, line: str) -> "Project":
        """Create a Project from a tab-delimited line (skipping header elsewhere)."""
        parts = line.strip().split("\t")
        name = parts[0]
        start = datetime.strptime(parts[1], DATE_FORMAT).date()
        priority = int(parts[2])
        estimate = float(parts[3])
        percent = int(parts[4])
        return cls(name, start, priority, estimate, percent)

    # ---------- String reps ----------

    def __str__(self) -> str:
        """Friendly display string (matches prac sample style)."""
        return (f"{self.name}, start: {self.start_date_str()}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:,.2f}, completion: {self.percent_complete}%")
