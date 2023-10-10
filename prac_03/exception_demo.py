"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
It will occur if the input is not an integer
2. When will a ZeroDivisionError occur?
It will occur if denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
We could use a while loop for error checking, but exception error checking is the best method
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
