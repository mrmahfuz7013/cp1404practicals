"""
CP1404/CP5632 Practical
Wimbledon data-reading, processing and displaying
Estimate: 25 minutes
Actual:   ___ minutes
"""
FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read data file and print details about Wimbledon champions and countries."""
    records = load_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def process_records(records):
    """Create dictionary of champions and set of countries from records (list of lists)."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display champions and countries."""
    print("Wimbledon Champions:")
    for name in sorted(champion_to_count):  # sorted for deterministic, readable output
        print(f"{name} {champion_to_count[name]}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def load_records(filename):
    """Load records from file in list of lists form (handles UTF-8 with BOM)."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip header row
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
