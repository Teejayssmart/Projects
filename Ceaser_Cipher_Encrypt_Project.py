alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

message = input("Enter your message: ").upper()

shift_number = int(input("Enter the shift number: "))


# create function
def encrypt_function(P_message, P_shift_number):
    # create a new variable to hold new cipher message
    cipher_message = ""
    # loop through message entered by user
    for char in P_message:
        if char in alphabet:
            # To find index in a list, use index method
            position = alphabet.index(char)

            new_position = position + P_shift_number
            while new_position > 25:
                new_position = new_position - 26

            new_character = alphabet[new_position]

            cipher_message += new_character
        else:
            cipher_message += char
    return f"The encoded message is {cipher_message}"


result = encrypt_function(message, shift_number)
print(result)
