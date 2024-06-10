"""
Displays all the odd numbers between
1 and 20 with a space between each one.
"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""
Count in 10s from 0 to 100
"""
for i in range(0, 101, 10):
    print(i, end=' ')
print()

"""
Count down from 20 to 1
"""
for i in range(20, 0, -1):
    print(i, end=" ")
print()

"""
Print n stars. Ask the user for a number, then print that many stars (*), all on one line.
"""
star = ''
number_of_stars = int(input("Number of stars '*': "))
for i in range(number_of_stars):
    star += '*'
    print(star)
print()
