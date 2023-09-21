"""" Score Menu Program """
from prac_02 import score

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


main()
