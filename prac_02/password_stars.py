""" Password Stars """

"""
Pseudocode
Program that ask user for a password, with error checking to repeat if the password doesn't meet
the minimum length set by the variable.

get user password
error check if the input doesn't match the minimum length

the program should print "*" same length as the password

"""
minimum_length = 8

user_password = input("Password: ")
while len(user_password) < minimum_length:
    print("Password must be minimum of 8")
    user_password = input("Password: ")

if user_password:
    character = len(user_password) * "*"
    print(character)



