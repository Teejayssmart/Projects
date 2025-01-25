import random

rock = 2
paper = 3
scissor = 1

all_selection = ["rock", "paper", "scissor"]

# First round of input
user_input = input("Enter a choice (rock, paper or scissor): ")
computer_selection = random.choice(all_selection)

print(f"You chose {user_input}, Computer chose {computer_selection}")
if user_input == computer_selection:
    print("It is a tie!")
elif user_input == "rock" and computer_selection == "scissor":
    print("Rock is greater than Scissor, you win!")
elif user_input == "paper" and computer_selection == "scissor":
    print("Scissor is greater than Paper, Computer wins!")
elif user_input == "scissor" and computer_selection == "rock":
    print("Rock is greater than Scissor, Computer wins!")
elif user_input == "scissor" and computer_selection == "paper":
    print("Scissor is greater than Paper, you win!")
elif user_input == "paper" and computer_selection == "rock":
    print("Paper is greater than Rock, you win!")
elif user_input == "rock" and computer_selection == "paper":
    print("Paper is greater than Rock, Computer wins!")

# Ask if the user wants to play again
user_input_2 = input("Play again (yes/no)? ")

# While loop to continue or stop based on user input
while user_input_2 == "yes":
    user_input = input("Enter a choice (rock, paper or scissor): ")
    computer_selection = random.choice(all_selection)
    print(f"You chose {user_input}, Computer chose {computer_selection}")

    if user_input == computer_selection:
        print("It is a tie!")
    elif user_input == "rock" and computer_selection == "scissor":
        print("Rock is greater than Scissor, you win!")
    elif user_input == "paper" and computer_selection == "scissor":
        print("Scissor is greater than Paper, Computer wins!")
    elif user_input == "scissor" and computer_selection == "rock":
        print("Rock is greater than Scissor, Computer wins!")
    elif user_input == "scissor" and computer_selection == "paper":
        print("Scissor is greater than Paper, you win!")
    elif user_input == "paper" and computer_selection == "rock":
        print("Paper is greater than Rock, you win!")
    elif user_input == "rock" and computer_selection == "paper":
        print("Paper is greater than Rock, Computer wins!")

    # After a round, ask if they want to play again
    user_input_2 = input("Play again (yes/no)? ")

print("Thanks for playing!")
