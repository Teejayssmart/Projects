hours = input("Enter Hours: ")

try:
    hours = float(hours)

except ValueError:
    print("There is an error")

    quit()

rate = input("Enter rate: ")

try:
    rate = float(rate)
except ValueError:
    print("There has been an error")

    quit()

else:

    overtime_rate = 1.5
    extra_hours = 0

    if hours < 40:
        pay = round(rate * hours, 2)
        print(f"Pay is {pay}")

    else:
        overtime_rate = 1.5

        extra_hours = hours - 40
        extra_pay = overtime_rate * extra_hours * rate

        pay = (40 * rate) + extra_pay

        print(f"Pay is {pay}")


finally:
    print("thanks for using our calculator")
