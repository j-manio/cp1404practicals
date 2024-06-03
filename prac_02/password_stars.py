"""
Pseudocode
Program that ask user for a password, with error checking to repeat if the password doesn't meet
the minimum length set by the variable.

get the user's password input
while the password doesn't meet the minimum length set by the variable. It will print invalid
if user inputs "Pythonista" 10 characters, the program should print 10 "*"

"""
MINIMUM_LENGTH = 10

user_password = input("Password: ")
while len(user_password) < MINIMUM_LENGTH:
    print("Password must be minimum of 10")
    user_password = input("Password: ")
print(len(user_password) * "*")

"""Module docstring"""


# imports
# CONSTANTS

def main():
    """Function docstring"""
    # statements...
    do_stuff()


def do_stuff():
    """Function docstring"""
    # statements...


main()