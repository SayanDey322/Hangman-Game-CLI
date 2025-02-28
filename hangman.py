import random

from logo import hangman_logo
from art import stages
from word import word_list
print("Welcome to the game:)")
chosen_word = random.choice(word_list)
print(f"solution is {chosen_word}")
lives = 6
display = []
for some in chosen_word:
    display += ' '

while ' ' in display :
    guess = str(input("Guess a letter: ").lower())

    if guess in display:
        print(f"You've already guessed {guess}")
        continue
    elif guess in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if guess == letter:
                display[position] = guess
                print("You choose the correct letter!!")
    else :
        print(f"You gussed {guess},that's not in word,you lose a life.")
        lives -= 1
        if lives != 0:
            print(stages[lives])
        if lives == 0:
            break
    print(display)
if lives == 0:
    print("You lose..")
else:
    print("You Win:)")
