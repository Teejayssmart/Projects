# does user wants to add mushroom?

mini_burger = 5
normal_burger = 8
large_burger = 10
mini = 1
normal = 1
large = 2
bill = 0
print("Welcome to Burger shop!")
burger_size = input("What size of burger do you want? M, N, or L ")

if burger_size == "M":
    # do this
    mushroom = input("do you want mushroom? Y or N ")
    if mushroom == "Y":
        bill = mini_burger + 1
    else:
        bill = mini_burger + 0

    extra_cheese = input("do you want extra cheese? Y or N ")

    if extra_cheese == "Y":
        bill += 1

    print(f"Your final bill is £{bill}")

elif burger_size == "N":
     mushroom = input("do you want mushroom? Y or N ")
     if mushroom == "Y":
        bill = normal_burger + 1

     else:
        bill = normal_burger + 0

     extra_cheese = input("do you want extra cheese? Y or N ")

     if extra_cheese == "Y":
        bill += 1

     print(f"Your bill is £{bill}")

elif burger_size == "L":
    mushroom = input("do you want mushroom? Y or N ")
    if mushroom == "Y":
        bill = large_burger + 1

    else:
        bill = large_burger + 0

    extra_cheese = input("do you want extra cheese? Y or N ")

    if extra_cheese == "Y":
        bill += 1

    print(f"Your bill is £{bill}")

