import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBER_OF_LINE = 6

num_pick = int(input("How many picks? "))

for i in range(num_pick):
    quick_pick_list = []
    for g in range(NUMBER_OF_LINE):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in quick_pick_list:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_pick_list.append(number)
        quick_pick_list.sort()
    for l in range(NUMBER_OF_LINE):
        print(f"{quick_pick_list[l]:>2}", end=" ")
    print()