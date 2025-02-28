# Hangman-Game-CLI
 # Hangman Game
A simple, interactive console-based Hangman game implemented in Python. Test your word-guessing skills by attempting to guess letters in a randomly selected word from a list, with a limited number of lives.

# Game Description
In this Hangman game, you are tasked with guessing a hidden word by suggesting one letter at a time. If you guess correctly, the letter is revealed in the correct position. If you guess incorrectly, you lose one of your lives, bringing you closer to the hanging figure's completion.

The game ends when:

You guess the word correctly and win.
You exhaust all your lives (6 chances) and lose.
# How to Play
Run the program to start the game.
You will see a banner and a series of underscores representing each letter of the hidden word.
Enter a letter to guess.
If the letter is correct, it will reveal itself in the word.
If incorrect, you lose a life and the hangman drawing progresses.
Continue guessing until either:
You guess the word correctly, or
You run out of lives, in which case you lose.
# Features
Random Word Selection: The word is randomly chosen from a list of fruits.
Lives Display: The game keeps track of your remaining lives.
Hangman Visuals: Each wrong guess progresses the hangman drawing.
Prevent Double Guesses: If you guess a letter you've already tried, the game notifies you.
# Game Stages
The game displays a visual progression of the hangman in stages as lives are lost. Here’s the progression:

Starting with a blank gallows.
Incremental drawing as incorrect guesses are made.
Complete hangman figure if all lives are lost.
# Example Output
_ _ _ _ _ _
********** You have 6/6 lives left.************
Guess a letter: a
_ a _ a _ _
********** You have 5/6 lives left.************
Guess a letter: b
your guess is wrong. You lost a life.
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
# Requirements
Python 3.x
This game can be run in any Python IDE or from the command line.

# Future Enhancements
Possible additions to the game:

Enhanced wordlist with various difficulty levels.
Graphical user interface (GUI).
Score tracking and saving feature.
# License
This project is open-source and available for modification and distribution.
