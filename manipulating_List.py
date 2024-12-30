import math


def square_list(p_list):
    for i in range(len(p_list)):
        p_list[i] = p_list[i] * p_list[i]
    return p_list


result = square_list([1, 2, 3,4,5])

print(result)
