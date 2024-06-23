"""
Emails
Estimate: 30 minutes
Actual:
"""


email = input('Enter your email: ')
while email != "":
    address_sign = email.split('@')[0]
    parts = address_sign.split(".")
    name = " ".join(parts).title()
    email = input('Enter your email: ')