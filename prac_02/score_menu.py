"""" Score Menu Program """

MENU = ("(G)et valid score\n"
        "(P)rint result\n"
        "(S)how stars\n"
        "(Q)uit")


def main():
    print(MENU)
    user_choice = str(input(">>>: ").upper())
    while user_choice != "Q":
        if user_choice == "G":
            valid_score = int(input("Score: "))
            while valid_score < 0 or valid_score > 100:
                print("Invalid score")
                valid_score = int(input("Score: "))
        elif user_choice == "P":
            pass
        elif user_choice == "S":
            pass
        else:
            print("Invalid choice")
        print(MENU)
        user_choice = str(input(">>>: ").upper())
    print("Farewell")


def determine_result(valid_score):
    if valid_score < 0 or valid_score > 100:
        return "Invalid score"
    else:
        if valid_score >= 90:
            return "Excellent"
        elif valid_score >= 50:
            return "Pass"
        else:
            return "Bad"


main()
