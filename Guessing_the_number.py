# import math
# import random
#
# lower_bond = int(input("enter lower bond: "))
# upper_bond = int(input("enter upper bond: "))
# chances = int(input("Enter number of chances to guess: "))
# print(f"You've only {chances} to guess the integer!")
#
# number_of_guessed_times = 0
#
#
# # guessed_number = 0
#
#
# def cal_chances_of_users(a, b):
#     # generate random numbers
#     random_number = random.randint(a, b)
#     math.log(upper_bond - lower_bond + 1, 2)
#
#     while number_of_guessed_times <= chances:
#         guessed_number = input("guess a number: ")
#         if guessed_number < random_number:
#             print("you guessed too small!")
#         elif guessed_number > random_number:
#             print("you guessed too  high!")
#         elif guessed_number == random_number:
#             print("you guessed right!")
#         else:
#             print(f"the number is {random_number}")
#             print("Better luck ne3xt time!")
#
#
# print(cal_chances_of_users(upper_bond, lower_bond))


import math
import random

print("Welcome to the guessing game. Enjoy!")
lower_bound = int(input("enter lower bound: "))
upper_bound = int(input("enter upper bound: "))
random_number = random.randint(lower_bound, upper_bound)

print(f"Number guessed by the computer is: {random_number}")
no_of_attempt = int(input("Enter the number of attempts user can guess: "))
number = int(input("enter your own guessed number: "))
counter = 1
guessed_number = number
while counter < no_of_attempt:

    if guessed_number == random_number:
        print("you guessed right!")
        break
    elif guessed_number < random_number:
        print("you guessed too small!")
        guessed_number = int(input("enter your own guessed number: "))
    elif guessed_number > random_number:
        print("you guessed too  high!")
        guessed_number = int(input("enter your own guessed number: "))

    counter += 1

else:
    print(f"the number is {random_number}")
    print("Better luck ne3xt time!")
