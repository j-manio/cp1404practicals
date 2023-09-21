"""" Score Menu Program """

MENU = ("(G)et valid score\n"
        "(P)rint result\n"
        "(S)how stars\n"
        "(Q)uit")


def main():
    print(MENU)
    user_choice = str(input(">>>: ").upper())
    while user_choice != "Q":
        print("Invalid score")
        user_choice = str(input(">>>: ").upper())


main()
