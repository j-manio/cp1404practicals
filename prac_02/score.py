"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    print(determine_result(score))
    random_score = random.randint(1, 100)
    print(f"Random score is {random_score} and is considered {determine_result(random_score)}")


def determine_result(score):
    """Determine the result based on a given valid score"""
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Pass"
        else:
            return "Bad"


main()
