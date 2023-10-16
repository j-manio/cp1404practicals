"""List Exercises"""

numbers = []

for i in range(5):
    number = input("Number: ")
    numbers.append(int(number))

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
