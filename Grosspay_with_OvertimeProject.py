hours = int(input("Enter Hours: "))
rate = int(input("Enter rate: "))

if hours < 40:
    pay = round(rate * hours, 2)
    print(f"Pay is {pay}")

else:
    overtime_rate = 1.5

    overtime = hours - 40
    extra_pay = overtime_rate * overtime * rate

    pay = (40 * rate) + extra_pay

    print(f"Pay is {pay}")
