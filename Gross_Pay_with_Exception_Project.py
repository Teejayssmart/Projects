hours = input("Enter Hours: ")

try:
    hours = float(hours)

except ValueError:
    print("There is an error")

    quit()


rate = input("Enter rate: ")

try:
    rate =  float(rate)
except ValueError:
    print("There has been an error")

    quit()

else:

    pay = 0
    new_pay = 0
    overtime_rate = 1.5
    extra_hours = 0
    if hours == 40:
        pay = rate * hours
        print(f"Pay is {pay}")

    elif hours > 40:
        extra_hours = hours - 40
        extra_pay_hour = overtime_rate * extra_hours
        bonus = extra_pay_hour * extra_hours
        actual_pay = 40 * rate
        pay = round(actual_pay + bonus, 2)
        print(f"Pay is {pay}")

finally:
    print("thanks for using our calculator")
