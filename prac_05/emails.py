"""
Emails
Estimate: 30 minutes
Actual:
"""


def main():
    email_to_name = {}
    email = input('Enter your email: ')
    while email != "":
        name = extract_name(email)
        confirmation = input(f'Is your name: {name} Y/N?: ').upper()
        if confirmation != 'Y' or confirmation == "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input('Enter your email: ')

    for email, name in email_to_name.items():
        print(f"{name}: ({email})")


def extract_name(email):
    """Extract name from email"""
    address_sign = email.split('@')[0]
    parts = address_sign.split(".")
    name = " ".join(parts).title()
    return name


main()
