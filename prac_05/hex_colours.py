COLOR_TO_CODE = {'absolutezero': '#0048ba', 'acidgreen': '#b0bf1a', 'aliceblue': '#f0f8ff', 'amber': '#ffbf00',
                 'aqua': '#00ffff', 'ashgrey': '#b2beb5', 'aurelin': '#fdee00', 'babyblue': '#89cff0',
                 'Baby Pink': '#f4c2c2', 'Beige': '#f5f5dc'}

print(COLOR_TO_CODE)


colour_choice = input('Colour name: ').strip().lower()
while colour_choice != "":
    if colour_choice in COLOR_TO_CODE:
        print(f"{COLOR_TO_CODE[colour_choice]}")
    else:
        print("Invalid Colour")
    colour_choice = input('Colour name: ')
