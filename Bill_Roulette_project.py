import random

names = input("Input everyone's name, separated by comma: ")
string_convert = names.split(',')


    #to generate random index among names
random_name = random.randint(0,len(string_convert) -1)

    #to pick a random index name
name_picked = string_convert[random_name]

print(f"{name_picked} is going to buy the meal today!")