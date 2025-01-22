def max_number(number1, number2, number3):
    highest_number = 0
    if number1 > number2:
        highest_number = number1
    else:
        highest_number = number2
    if number1 < number3:
        highest_number = number3
    return highest_number


print(max_number(3,-6,-5))