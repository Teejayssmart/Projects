
import random
def print_map(p_map):
    print('\n'.join([' '.join(['{:2}'.format(item) for item in row]) for row in p_map]))

map1 = [["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"]]
print("This is our initial map...")
print_map(map1)




user_input = input("What do you think: where is the Golden Star in the map? ")

#convert user input to a list of integers
num_list = list(map(int, user_input))

#need 2 variables , each to hold spot for row and column and also generate numbers
row_number_generated = random.randint(0,2)
column_number_generated = random.randint(0,2)



#equate both generated numbers to "*"/ or place star on map
map1[row_number_generated][column_number_generated] = "*"

#concertenate both numbers and print generated location
print(str(row_number_generated+1) + " " + str(column_number_generated+1))

# assign a variable to the above concatenation
computer_position = str(row_number_generated+1) + " " + str(column_number_generated+1)

#compare user input with generated position
if user_input == computer_position:
    print("congratulations , you found the gold star!")

    # for user input
else:


    row_number = num_list[0] -1
    vertical_number =  num_list[1]-1
    map1[row_number][vertical_number]= "x"

    print("unfortunately, you couldnt find it. ")
