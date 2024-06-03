"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# score = float(input("Enter score: "))
# if score < 0 or score > 100:
#     print("Invalid score")
# else:
#     if score >= 90:
#         print("Excellent")
#     elif score >= 50:
#         print("Pass")
#     elif score < 50:
#         print("Bad")

import random


def main():
    score = get_score()
    check_score(score)
    random_score = random.randint(1, 100)
    print(check_score(score))
    print(f"Random score is {random_score} and is considered {check_score(random_score)}")


def check_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


def get_score():
    score = float(input("Enter score: "))
    return score


main()
