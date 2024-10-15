# Write a programme to calculate Gross Pay

userHours = input("Please enter number of hours worked: \n")
ratePerHour = input("Please enter rate per hour: \n")
hours = float(userHours)
rate1 = float(ratePerHour)
grossPay = round(hours * rate1,2)
print(f"Your gross pay is {grossPay}")

