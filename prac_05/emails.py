"""
Emails
Estimate: 180 minutes
Actual: 300 minutes
"""


def main():
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = extract_name_to_email(email)

        confirmation = input(f"Verify your name: {name} Y / N?: ").upper()
        if confirmation != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_to_email(email):
    address_sign = email.split("@")[0]
    parts = address_sign.split(".")
    name = " ".join(parts).title()
    return name


main()
