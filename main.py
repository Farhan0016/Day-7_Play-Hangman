#Play-Hangman

#import modules and libraries
#import os
import random
from hangman_art import logo, stages
from hangman_words import word_list

#Declare variables
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
end_of_game = False
display = []

#print hangman logo
print(logo)

#Creating blanks
for _ in range(word_length):
    display.append("_")

#Loop through the program until the user use all their lives.
while not end_of_game:
    #Get user input
    guess = input("Guess a letter: ").lower()

    # Clear the screen
    #os.system('cls')

    #Check if the user guessed it before
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        if guess == chosen_word[position]:
            display[position] = guess

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        #Check if user uses all its life
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Print display list into string representation
    print(' '.join(display))

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Print the stages based on life remaining
    print(stages[lives])
