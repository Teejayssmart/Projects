# Create a function that takes two digits number from console and returns sum of digits.
# e.g. if the input was 45, then the output should be 4 + 5 = 9
#
# Example Input
#
# sum_of_two_digits()
# Enter two digit number: 45

def sum_2_digits():
    two_digit_number = input("enter number: ")
    sum = int(two_digit_number[0]) + int(two_digit_number[1])
    return sum


result = sum_2_digits()
print(result)
