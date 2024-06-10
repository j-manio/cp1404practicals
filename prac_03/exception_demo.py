"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When an input is not an integer i.e. strings
2. When will a ZeroDivisionError occur?
It will occur when the denominator is zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Using while loop can keep asking the user if they input a 0 as the denominator (Infinite loop).
"""
# while True:
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
