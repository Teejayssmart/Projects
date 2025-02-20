name1 = input("Enter first name ")
name2 = input("enter second name ")

name = name1 + name2
lower_case_name = name.lower()

t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")

true = t + r + u + e

l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")

love = l + o + v + e

# Concentrate
true_love = str(true) + str(love)
# print(true_love)

if  int(true_love) < 10 or int(true_love) > 85:
    print(f"Your score is {true_love}, you go together like coke and mentos")
elif int(true_love) >= 40 and int(true_love) <= 70:
    print(f"Your score is {true_love}, you are alright together")

else:
    print(f"Your score is {true_love}")
