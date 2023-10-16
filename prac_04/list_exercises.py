"""List Exercises"""

numbers = []

for i in range(5):
    number = input("Number: ")
    numbers.append(int(number))

print(f"The first number is {numbers[0]}")
