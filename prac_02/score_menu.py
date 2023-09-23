"""" Score Menu Program """

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
            valid_score = get_valid_score()
        elif user_choice == "P":
            print(f"Your score is {valid_score} is considered {determine_result(valid_score)}")
        elif user_choice == "S":
            print(f"Star: {print_stars(valid_score)}")
        else:
            print("Invalid choice")
        print(MENU)
        user_choice = str(input(">>>: ").upper())
    print("Farewell")


def print_stars(valid_score):
    character = valid_score * "*"
    return character


def get_valid_score():
    valid_score = int(input("Score: "))
    while valid_score < 0 or valid_score > 100:
        print("Invalid score")
        valid_score = int(input("Score: "))
    return valid_score


def determine_result(valid_score):
    if valid_score >= 90:
        return "Excellent"
    elif valid_score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
