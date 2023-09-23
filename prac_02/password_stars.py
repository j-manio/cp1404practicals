""" Password Stars """

"""
Pseudocode
Program that ask user for a password, with error checking to repeat if the password doesn't meet
the minimum length set by the variable.

get user password
error check if the input doesn't match the minimum length

the program should print "*" same length as the password

"""

MINIMUM_LENGTH = 8


def main():
    password = get_password()
    print_stars(password)


def print_stars(password):
    """Prints star that equals to password length"""
    if password:
        character = len(password) * "*"
        print(character)


def get_password():
    """Prompt user to input pass no less than 8"""
    user_password = input("Password: ")
    while len(user_password) < MINIMUM_LENGTH:
        print("Password must be minimum of 8")
        user_password = input("Password: ")
    return user_password


main()
