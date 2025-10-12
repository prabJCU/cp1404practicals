"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_data = load_data(FILENAME)
    display_data(subject_data)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_data = []
    with open(filename, "r") as in_file:
        for line in in_file:
            line = line.strip()
            parts = line.split(",")
            parts[2] = int(parts[2])
            subject_data.append(parts)
    return subject_data


def display_data(subject_data):
    """Display data from file in sentence like structure"""
    for parts in subject_data:
        subject = parts[0]
        lecturer = parts[1]
        number_of_students = int(parts[2])
        print(f"{subject} is taught by {lecturer} and has {number_of_students} students")

main()
