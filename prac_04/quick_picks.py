"""Quick picks - Lottery Ticket Generator"""
import random
MIN_VALUE = 1
MAX_VALUE = 45

num_pick = int(input("How many quick picks? "))
lines = []
for i in range(num_pick):
    line = random.randint(MIN_VALUE, MAX_VALUE)
    lines.append(line)
print(lines)


