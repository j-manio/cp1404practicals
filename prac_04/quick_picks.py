"""Quick picks - Lottery Ticket Generator"""
import random

MIN_VALUE = 1
MAX_VALUE = 45
ENTRIES_PER_LINE = 6

num_pick = int(input("How many quick picks? "))

for i in range(num_pick):
    quick_picks_list = []
    for j in range(ENTRIES_PER_LINE):
        number = random.randint(MIN_VALUE, MAX_VALUE)
        while number in quick_picks_list:
            number = random.randint(MIN_VALUE, MAX_VALUE)
        quick_picks_list.append(number)
        quick_picks_list.sort()
    for l in range(ENTRIES_PER_LINE):
        print(f"{quick_picks_list[l]:>2}", end=" ")
    print()
