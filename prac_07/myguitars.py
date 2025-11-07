"""
CP1404 Practical - My Guitars
"""

from prac_07.guitar import Guitar


def main():
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        guitars.sort()
    in_file.close()

    for guitar in guitars:
        print(guitar)


main()
