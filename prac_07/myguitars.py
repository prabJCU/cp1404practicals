"""
CP1404 Practical - My Guitars
"""

from prac_07.guitar import Guitar


def main():
    guitars = []
    load_guitars(guitars)

    for guitar in guitars:
        print(guitar)

    add_guitar(guitars)
    save_guitars(guitars)


def load_guitars(guitars):
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
    in_file.close()
    guitars.sort()


def add_guitar(guitars):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost} added.")
        name = input("Name: ")


def save_guitars(guitars):
    out_file = open('guitars.csv', 'w')
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    out_file.close()


main()
