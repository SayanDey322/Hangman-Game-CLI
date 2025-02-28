banner = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / ` | ' \ / ` | ' ` _ \ / ` | ' \ 
| | | | (| | | | | (| | | | | | | (_| | | | |
|| ||\,|| ||\, || || ||\,|| |_|
                    __/ |                      
                   |_/  
'''
print(banner)

wordlist = ["mango", "apple", "orange", "pineapple", "banana"]

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

import random
word = random.choice(wordlist)
# print(word)
list = [char for char in word]

placeholder = ""
for i in range(0, len(list)):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
lives = 6

while not game_over:
    print(f"********** You have {lives}/6 lifes left.")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print("You've already guessed this letter.")
        continue

    display = ""
    for letter in list:
        if letter == guess:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in word:
        lives -= 1
        print("your guess is wrong. You lost a life.")

        if lives == 0:
            game_over = True
            print("You've lost. The word was:", word)

    print(stages[6 -lives])

    if "_" not in display:
        game_over = True
        print("Congratulations! You've guessed the right word:", word)