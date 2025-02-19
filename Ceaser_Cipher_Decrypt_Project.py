alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

message = input("enter message: ").upper()
shift_number = int(input(" enter shift number: "))


def decrypt_function(p_message, p_shift_number):
    # variable to hold encrypt message
    cipher_message = ""

    # to locate each index of p_message in the alphabet
    # loop through the message
    for each_character in p_message:
        if each_character in alphabet:
            # create a variable to hold position
            position = alphabet.index(each_character)

            # create new variable for new position of message
            new_position = position - p_shift_number

            # to prevent against any error of exceeding
            while new_position < 0:
                new_position = new_position + 26

            # create variable and assign new position
            new_character = alphabet[new_position]

            cipher_message += new_character
        else:
            cipher_message += each_character
    return cipher_message


result = decrypt_function(message, shift_number)
print(result)
