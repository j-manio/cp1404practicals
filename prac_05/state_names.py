"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

is_valid_input = False
while is_valid_input:
    try:
        state_code = str(input("Enter short state: ").upper())
        if state_code in CODE_TO_NAME:
            print(state_code, "is", CODE_TO_NAME[state_code])
            is_valid_input = True
        else:
            print("Invalid state code")
    except KeyError:
        print("State code not found in the dictionary")

for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")