import random

ran_num = random.randint(1, 6)
print(f"Dice1 : {ran_num}")
ran_num = random.randint(1, 6)
print(f"Dice2 : {ran_num}")

answer = input("Roll the dice again: (Y/N) ")

while answer == "Y":
    ran_num = random.randint(1, 6)
    print(f"Dice1 : {ran_num}")
    ran_num = random.randint(1, 6)
    print(f"Dice2 : {ran_num}")
    answer = input("Roll the dice again: (Y/N) ")
    if answer == "N":
        quit()
