import  random
word_list = ["TEEJAY", "CATAPILLER", "BALOTELLI"]
ran_word = random.choice(word_list)
length_word = len(ran_word)
#empty list for new guessing
empty_list = []
#to loop the choice words and perform action
for _ in range(length_word):
    empty_list.append("-")
print(empty_list)

#ask user to guess a letter
guess = input("guess a letter: ").upper()


#check if letter is already guessed
#create blank list where all guessed letters
#will be stored
guessed_letters = []
if guess in guessed_letters:
    print("you have already guessed this letter!")
else:
    guessed_letters.append(guess)

#check if letter guessed is one of the letters in secret_word
for letter in ran_word:
    if guess == letter:
        print("exist")
    else:print("not exist")

#check if letter guessed is in the secret_word
for position in range(length_word):
    letter = ran_word[position]

    if guess == letter:
        empty_list[position] = letter


