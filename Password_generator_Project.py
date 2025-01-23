import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"

letters_in_password = int(input("How many letters do you want in your password? "))
numbers_in_password = int(input("how many numbers do you want in your password? "))
symbols_in_password = int(input("how many symbols do you want in your password? "))

for letter in letters:
    generate = ''.join(random.choice(letters) for _ in range(letters_in_password))
print(generate)

for number in nums:
    generate_1 = ''.join(random.choice(nums) for _ in range(numbers_in_password))
print(generate_1)

for symbol in symbols:
    generate_2 = ''.join(random.choice(symbols) for _ in range(symbols_in_password))
print(generate_2)

print(f" Your password is {generate + generate_1 + generate_2}")

