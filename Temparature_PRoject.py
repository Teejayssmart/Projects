temp_value = int(input("enter temperature: "))


def temp(temp_1):
    if 18 <= temp_value <= 28:
        return "warm"
    elif temp_value > 28:
        return "hot"
    elif temp_value < 18:
        return "cold"

    return temp_1


result = temp(temp_value)
print(result)
