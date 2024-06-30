"""
Estimate: 40 minutes
Actual:   1 hour
"""
from prac_06.guitar import Guitar


guitars = []
print("My Guitars")
guitar_name = input("Name: ")
while guitar_name != "":
    year = int(input("Year: "))
    cost = int(input("Cost: "))
    guitar = Guitar(guitar_name, year, cost)
    guitars.append(Guitar(guitar_name, year, cost))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"

        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year:4}), worth ${guitar.cost:>10,.2f} {vintage_string}")

    guitar_name = input("Name: ")
