# Hangman

## Description

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

A class Hangman has been created to achieve this.

    """
    A hangman game. The user is asked for a letter and the computer checks if it is in the word.
    A random word is chosen from the word_list and the game starts with a default number of lives.

    Parameters:
    ----------
    word_list: list
        This is a list of words used in the game.
    num_lives: int
        Number of lives the player has.

    Attributes:
    ----------
    word: str
        The word to be guessed chosen randomly from the word_list.
    word_guessed: list
        List of letters from the word, a '_' is used fot letters that haven't been guessed.
        After a letter is guessed correctly the '_' is replaced with the corresponding letter.
    num_letters: int
        The number of unique letters in the word which haven't been guessed yet by the player.
    num_lives: int
        The number of lives the player has.
    word_list: list
        This is a list of words used in the game.
    list_of_guesses: list
        This is a list of the letters which have been already tried by the player.
    
    Methods:
    ----------
    check_guess(guess)
        Checks if the guessed letter is in the word chosen by the game.
    ask_for_input()
        Asks the user to input a letter.
    """

This project was built for the AiCore Data Analyst bootcamp in order to practice python programming skills.
This project has given me the opportunity to better my understanding on builiding python classes and functions.

## Installation Instructions

Standard python installation is required.

## Usage Instructions

The user can play the game by calling the play_game function.

## File structure

File milestone_2 contains a list of words from which the computer randomly picks one to be used in the game.

File milestone_3 contains the ask_for_input function which is used to ask the user to guess a letter.
This file also checks whether the letter chosen is in the word or not.

File milestone_4 contains the class Hangman which builds uppon the work in the previous two files.

File milestone_5 contains the full Hangman class referenced in the description which is used to play the final version of the game.

## License Information

The author of this repository is mihai0813.