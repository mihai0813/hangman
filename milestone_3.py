from milestone_2 import word

def ask_for_input():
    while True:
        guess = input("Guess a letter:", )
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)


def check_guess(guess):
    guess = guess.lower()
    if any(guess in word and len(word) > 1 for word in word.split()) == True:
        print("Good guess! {} is in the word.".format(guess))
    else:
        print("Sorry, {} is not in the word. Try again.".format(guess))

ask_for_input()