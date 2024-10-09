# Convert celcius to fahreinheit

temp = input("Enter Temperature in Celsius: \n")

temparature = float(temp)
F = round(( temparature * 9/5) + 32,1)
print(f"{temp} Celsius = {F} Fahreinheit")