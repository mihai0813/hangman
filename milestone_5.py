import random

class Hangman:
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

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the word chosen by the game.
        If yes, it replaces '_' with the letter in word_guessed.
        If no, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The guess to be checked.
        """
        self.guess = guess.lower()
        if self.guess in self.word:
            print("Good guess! {} is in the word.".format(self.guess))
            for i, letter in enumerate(self.word):
                if letter == self.guess:
                    self.word_guessed[i] = letter
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print("Sorry, {} is not in the word.".format(self.guess))
            print("You have {} lives left.".format(self.num_lives))

    def ask_for_input(self):
        """
        Asks the user to input a letter.
        It checks whether the entry is valid and if its already been tried.
        If the checks are passed, it calls the check_guess function.
        """
        while True:
            guess = input("Guess a letter:", )
            if len(guess) != 1 or guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!.")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(self.word_guessed)
            break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game.")
            break
            

play_game(["hello", "mihai"])