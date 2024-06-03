"""
display menu
get choice
while choice != quit option
    if choice == first option
        do first task
    else if choice == <second option>
        do second task
    ...
    else if choice == <n-th option>
        do n-th task
    else
        display invalid input error message
    display menu
    get choice
do final thing, if needed
"""

MENU = ("(H)ello\n"
        "(G)oodbye\n"
        "(Q)uit\n")

get_name = input("Enter name: ")
print(MENU, end='')
get_choice = input(">>> ").upper()
while get_choice != "Q":
    if get_choice == "H":
        print(f"Hello {get_name}")
    elif get_choice == "G":
        print(f"Goodbye {get_name}")
    else:
        print("Invalid choice")
    print(MENU, end='')
    get_choice = input(">>> ").upper()
print("Finished")
