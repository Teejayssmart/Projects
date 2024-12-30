print("Welcome to the trip Calculator!")
days = int(input("how many days will you stay? "))
hotel_price = float(input("how much does hotel cost per night? $"))
flight_price = float(input("how much does flight cost per night $"))
car_price = float(input("if you need rental car please enter the price otherwise enter zero. $"))
other_expenses = float(input("Enter other expenses. $"))

#askFor = int(ask)
#hotelPrice = float(price)
#flightCost = float(flight)
#extraPrice = float(extra)


totalCost = round(days * hotel_price + flight_price + days * car_price + other_expenses, 2)
print(f"Total cost : ${totalCost}")


