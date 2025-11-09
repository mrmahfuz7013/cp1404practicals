"""
CP1404 – Project Management program
Estimate: 90 mins
Actual 75 mins

Load/manage/save projects from a tab-delimited file using the Project class.
"""

from __future__ import annotations
from datetime import datetime
from typing import List

from project import Project, DATE_FORMAT

DEFAULT_FILENAME = "projects.txt"

MENU = (
    "- (L)oad projects\n"
    "- (S)ave projects\n"
    "- (D)isplay projects\n"
    "- (F)ilter projects by date\n"
    "- (A)dd new project\n"
    "- (U)pdate project\n"
    "- (Q)uit"
)


def main() -> None:
    """Run the Project Management menu program."""
    projects: List[Project] = load_projects(DEFAULT_FILENAME, quiet=True)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")
    print(MENU)
    choice = input(">>> ").strip().lower()

    while choice != "q":
        if choice == "l":
            filename = input("Filename to load: ").strip()
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename to save: ").strip()
            save_projects(projects, filename)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").strip().lower()

    # on quit, optional save to default file
    answer = input(f"Would you like to save to {DEFAULT_FILENAME}? ").strip()
    if answer.lower().startswith("y"):
        save_projects(projects, DEFAULT_FILENAME)
    print("Thank you for using custom-built project management software.")


# ---------- File I/O ----------

def load_projects(filename: str, quiet: bool = False) -> List[Project]:
    """Load projects from a tab-delimited file; skip header."""
    loaded: List[Project] = []
    with open(filename, "r", encoding="utf-8") as in_file:
        header = in_file.readline()  # discard header
        for line in in_file:
            if line.strip():
                loaded.append(Project.from_record(line))
    if not quiet:
        print(f"Loaded {len(loaded)} projects from {filename}")
    return loaded


def save_projects(projects: List[Project], filename: str) -> None:
    """Save projects to a tab-delimited file (write header first)."""
    with open(filename, "w", encoding="utf-8") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(project.to_record() + "\n")
    print(f"Saved {len(projects)} projects to {filename}")


# ---------- Actions ----------

def display_projects(projects: List[Project]) -> None:
    """Display incomplete and completed groups, each sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])
    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects:")
    for p in complete:
        print(f"  {p}")


def filter_projects_by_date(projects: List[Project]) -> None:
    """Ask for a date and show projects starting after that date, sorted by date."""
    date_string = input("Show projects that start after date (dd/mm/yy or dd/mm/yyyy): ").strip()
    # Accept 2-digit or 4-digit year
    fmt = "%d/%m/%y" if len(date_string.split("/")[-1]) == 2 else DATE_FORMAT
    after_date = datetime.strptime(date_string, fmt).date()
    filtered = [p for p in projects if p.start_date >= after_date]
    filtered.sort(key=lambda p: p.start_date)
    for p in filtered:
        print(p)


def add_new_project(projects: List[Project]) -> None:
    """Prompt for details and append a new Project."""
    print("Let's add a new project")
    name = input("Name: ").strip()
    date_string = input("Start date (dd/mm/yy or dd/mm/yyyy): ").strip()
    fmt = "%d/%m/%y" if len(date_string.split("/")[-1]) == 2 else DATE_FORMAT
    start = datetime.strptime(date_string, fmt).date()
    priority = safe_int(input("Priority: "))
    estimate = safe_float(input("Cost estimate: $"))
    percent = safe_int(input("Percent complete: "))
    projects.append(Project(name, start, priority, estimate, percent))


def update_project(projects: List[Project]) -> None:
    """Select a project by index, then update percent and/or priority."""
    # Show projects sorted by name for easier picking (matches sample feel)
    indexed = sorted(enumerate(projects), key=lambda ip: ip[1].name.lower())
    for idx, proj in indexed:
        print(f"{idx} {proj}")
    try:
        choice = int(input("Project choice: "))
    except ValueError:
        print("Update cancelled.")
        return
    if not (0 <= choice < len(projects)):
        print("Invalid project index.")
        return
    project = projects[choice]
    print(project)
    percent_text = input("New Percentage: ").strip()
    priority_text = input("New Priority: ").strip()
    if percent_text:
        project.percent_complete = safe_int(percent_text)
    if priority_text:
        project.priority = safe_int(priority_text)


# ---------- Small input helpers (minimal validation; blank = error if not allowed) ----------

def safe_int(text: str) -> int:
    """Convert text to int, defaulting to 0 on failure."""
    try:
        return int(text)
    except ValueError:
        return 0


def safe_float(text: str) -> float:
    """Convert text to float, defaulting to 0.0 on failure."""
    try:
        return float(text)
    except ValueError:
        return 0.0


if __name__ == "__main__":
    main()
