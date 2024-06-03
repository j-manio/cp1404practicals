"""Score Menu Program"""
"""
Pseudocode:
display menu
get user choice from the menu
choice should be valid and if not it will show an error message

if user choose G, it will prompt user to input a valid score
this will error check it if the valid score is within 0 to 100

if user choose P, it will print the result of the given score

if user choose S, it will print stars equals to valid score

Q is to quit the program and print a farewell message

"""

MENU = ("(G)et valid score\n"
        "(P)rint result\n"
        "(S)how stars\n"
        "(Q)uit")


def main():
    valid_score = 0
    print(MENU)
    user_choice = str(input(">>>: ").upper())
    while user_choice != "Q":
        if user_choice == "G":
            valid_score = get_valid_score(valid_score)
        elif user_choice == "P":
            determine_result(valid_score)
            print(f"Your score is {valid_score} is considered {determine_result(valid_score)}")
        elif user_choice == "S":
            print(f"Star: {print_stars(valid_score)}")
        else:
            print("Invalid Choice")
        print(MENU)
        user_choice = str(input(">>>: ").upper())
    print("Farewell")


def print_stars(valid_score):
    print(valid_score * "*")


def determine_result(valid_score):
    if valid_score < 0 or valid_score > 100:
        return "Invalid score"
    elif valid_score >= 90:
        return "Excellent"
    elif valid_score >= 50:
        return "Pass"
    else:
        return "Bad"


def get_valid_score(valid_score):
    valid_score = int(input(">>>: "))
    while valid_score < 0 or valid_score > 100:
        print("Invalid score")
        valid_score = int(input(">>>: "))
    return valid_score


main()
