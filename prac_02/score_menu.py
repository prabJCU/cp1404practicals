"""
CP1404 - Practical
score menu
"""

def main():
    score = get_valid_score()

    choice = ""
    while choice != "Q":
        print_menu()
        choice = input(">>> ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(get_score_status(score))
        elif choice == "S":
            print("*" * int(score))
        elif choice == "Q":
            print("Farewell!")
        else:
            print("Invalid choice. Please try again.")


def print_menu():
    """ Prints program menu"""
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    """ Validate user input """
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


def get_score_status(score):
    """ Determine status of given score"""
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
