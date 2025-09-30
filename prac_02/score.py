"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

def main():
    # Ask user for score
    score = float(input("Enter score: "))
    get_score_status(score)

    # Generate random score
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score} -> ", end="")
    get_score_status(random_score)

def get_score_status(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
