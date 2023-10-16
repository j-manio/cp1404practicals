"""Quick picks - Lottery Ticket Generator"""
import random
MIN_VALUE = 1
MAX_VALUE = 45
ENTRIES_PER_LINE = 6

num_pick = int(input("How many quick picks? "))
quick_picks_list = []
for i in range(ENTRIES_PER_LINE):
    number = random.randint(MIN_VALUE, MAX_VALUE)
    quick_picks_list.append(number)
print(quick_picks_list)



