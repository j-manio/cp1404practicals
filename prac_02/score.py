"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# score = float(input("Enter score: "))
# if score < 0 or score > 100:
#     print("Invalid score")
# else:
#     if score >= 90:
#         print("Excellent")
#     elif score >= 50:
#         print("Pass")
#     elif score < 50:
#         print("Bad")

score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Bad")
