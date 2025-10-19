"""
CP1404 Practical - Wimbledon
Estimate: 25 minutes
Actual: 38 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    data = load_data(FILENAME)
    champions = count_champions(data)
    countries = get_countries(data)

    print(f"Wimbledon Champions:")
    for name, wins in sorted(champions.items()):
        print(f"{name} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def load_data(filename=FILENAME):
    """Read data from file into a list of lists"""
    wimbledon_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip header line
        for line in in_file:
            parts = line.strip().split(",")
            parts[0] = int(parts[0])  # Convert year to int
            wimbledon_data.append(parts)
    return wimbledon_data


def count_champions(data):
    """Count the number of champions present in the data."""
    champions = {}
    for record in data:
        champion = record[2]
        champions[champion] = champions.get(champion, 0) + 1
    return champions


def get_countries(data):
    """Return a set of countries containing champions."""
    countries = set()
    for record in data:
        countries.add(record[1])
    return countries


main()
