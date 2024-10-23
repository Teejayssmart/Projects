# Write a programme to calculate Gross Pay

userHours = input("Please enter number of hours worked: \n")
ratePerHour = input("Please enter rate per hour: \n")
hours = float(userHours)

rate = float(ratePerHour)
grossPay1 = round(hours * rate,2)
print(f"Your gross pay is {grossPay1}")
print("bye")

