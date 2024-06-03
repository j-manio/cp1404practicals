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
    print(MENU)
    user_choice = str(input(">>>: ").upper())
    while user_choice != "Q":
        if user_choice == "G":
            valid_score = int(input(">>>: "))
            while valid_score < 0 or valid_score > 100:
                print("Invalid score")
                valid_score = int(input(">>>: "))
        elif user_choice == "P":
            print("Print Result")
        elif user_choice == "S":
            print("Show Stars")
        else:
            print("Invalid Choice")
        print(MENU)
        user_choice = str(input(">>>: ").upper())
    print("Farewell")


main()
