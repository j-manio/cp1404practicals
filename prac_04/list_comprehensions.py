"""
CP1404/CP5632 Practical
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)

# list comprehension that creates a list containing the initials
# this splits each name and adds the first letters of each part to a string
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

# this example uses filtering to select only the names that start with A
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# and here's the join string method being used to create a single string from the names like:
# 'Ada Alan Angel Bob Jimi'
print(" ".join(sorted(names)))

# print a list of all the full_names in lowercase format
lowercase_full_names = [full_name.lower() for full_name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
# Prints a list of integers from the above list of strings
numbers = tuple([int(number) for number in almost_numbers])
print(numbers)


# Prints a list of only the numbers that are
# greater than 9 from the numbers (not strings)
greater_number = [number for number in numbers if number > 9]
print(greater_number)

# Prints a list of last names
# if the length of their full name is greater than 11

# the result should be: 'Harlem, Hendrix, Lovelace'
parts = " ".join(last_name.split()[-1] for last_name in full_names if len(last_name) > 11)
print(parts)
