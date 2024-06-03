"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

"""Module docstring"""

MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = convert_celsius_to_fahrenheit()
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            celsius = convert_fahrenheit_to_celsius()
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit_to_celsius():
    """This function will convert Fahrenheit to Celsius"""
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)  # # Will convert Fahrenheit to celsius
    return celsius


def convert_celsius_to_fahrenheit():
    """This function will convert Celsius to Fahrenheit"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32  # Will convert celsius to Fahrenheit
    return fahrenheit


main()
