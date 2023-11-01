import random

from numpy import append

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        self.guess = guess.lower()
        if any(self.guess in self.word and len(self.word) > 1 for self.word in self.word.split()) == True:
            print("Good guess! {} is in the word.".format(self.guess))
            for i, letter in self.word:
                if letter == self.guess:
                    self.word_guessed[i] = letter
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print("Sorry, {} is not in the word.".format(self.guess))
            print("You have {} lives left.".format(self.num_lives))

    def ask_for_input(self):
        while True:
            self.guess = input("Guess a letter:", )
            if len(self.guess) != 1 and self.guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif self.guess in self.list_of_guesses:
                print("You already tried that letter!.")
            else:
                self.check_guess(self.guess)
                self.list_of_guesses.append(self.guess)
