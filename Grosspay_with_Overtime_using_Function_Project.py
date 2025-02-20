def compute_pay(p_hour, p_rate):
    if p_hour < 40:
        pay = round(p_rate * p_hour, 2)
    else:
        overtime_rate = 1.5

        overtime = p_hour - 40
        extra_pay = overtime_rate * overtime * p_rate

        pay = (40 * p_rate) + extra_pay
    return pay


def check_for_float(p_value):
    try:
        p_val = float(p_value)
        return p_val
    except ValueError:
        print("There is an error")
        quit()

hours = input("Enter Hours: ")
hour = check_for_float(hours)
rate = input("Enter rate: ")
rate = check_for_float(rate)


result = compute_pay(hour, rate)
print(f"Pay: {result}")
