"""
Program: Hangman game
Name:Sylwia Glod
Date: Decemeber 14th, 2020
"""

from string import ascii_lowercase
from randomWords import get_random_word


def get_minimum_word_length():
    # User gets to choose the minimum letter that are in the word.
    while True:
        min_word_length = input(
            'What minimum word length do you want? [4-16] ')
        try:
            min_word_length = int(min_word_length)
            if 4 <= min_word_length <= 16:
                return min_word_length
            else:
                print('{0} is not between 4 and 16'.format(min_word_length))
        except ValueError:
            print('{0} is not an integer between 4 and 16'.format(
                min_word_length))


def get_number_of_attempts():
    # User gets to choose how many input they get!
    while True:
        number_attempts = input(
            'How many tries do you wish to have? [1-25] ')
        try:
            number_attempts = int(number_attempts)
            if 1 <= number_attempts <= 25:
                return number_attempts
            else:
                print('{0} is not between the numbers of 1 and 25'.format(number_attempts))
        except ValueError:
            print('{0} is not a number between 1 and 25'.format(
                number_attempts))


def get_next_letter(remaining_letters):
    # Get the user-inputted next letter.
    if len(remaining_letters) == 0:
        raise ValueError('You ran out of letters!')
    while True:
        next_letter = input('Please choose the your next letter: ').lower()
        if len(next_letter) != 1:
            print('{0} is not a single letter'.format(next_letter))
        elif next_letter not in ascii_lowercase:
            print('{0} is not a letter'.format(next_letter))
        elif next_letter not in remaining_letters:
            print('Youve guessed {0} before'.format(next_letter))
        else:
            remaining_letters.remove(next_letter)
            return next_letter


def get_display_word(word, idxs):
    # Get the word for display
    if len(word) != len(idxs):
        raise ValueError('Word length and indices length are not the same')
    displayed_word = ''.join(
        [letter if idxs[i] else '*' for i, letter in enumerate(word)])
    return displayed_word.strip()


def play_hangman():
    # This is the play for the game. Asks if you want to retry at the end

    # Let player specifiy how many attempts they want
    print('Starting our super fun game of Hangman...')
    attempts_remaining = get_number_of_attempts()
    min_word_length = get_minimum_word_length()

    # Select the word randomly
    print('Choosing a word!')
    word = get_random_word(min_word_length)
    print()

    # Initialize variables
    idxs = [letter not in ascii_lowercase for letter in word]
    remaining_letters = set(ascii_lowercase)
    wrong_letters = []
    word_solved = False

    # Main game loop
    while attempts_remaining > 0 and not word_solved:
        # Print current game state
        print('Word: {0}'.format(get_display_word(word, idxs)))
        print('Attempts Remaining: {0}'.format(attempts_remaining))
        print('Previous Guesses: {0}'.format(' '.join(wrong_letters)))

        # Get player's next letter guess
        next_letter = get_next_letter(remaining_letters)

        # Checking if letter guess is in word
        if next_letter in word:
            # Guessed correctly
            print('{0} is in the word!'.format(next_letter))

            # Reveals matching letters in game
            for i in range(len(word)):
                if word[i] == next_letter:
                    idxs[i] = True
        else:
            # Guessed incorrect letter
            print('{0} is NOT in the word!'.format(next_letter))

            # Decrement num of attempts left and append guess to wrong guesses
            attempts_remaining -= 1
            wrong_letters.append(next_letter)

        # Check if word is completed
        if False not in idxs:
            word_solved = True
        print()

    # The game is over: reveal the word
    print('The word is {0}'.format(word))

    # Notify player of win or loss!
    if word_solved:
        print('Congratulations! You won my game of hangman!')
    else:
        print('Oops! You lost! Try again next time!')

    # Ask player if he/she wants to try again
    try_again = input('Would you like to give it another try? [y/Y] ')
    return try_again.lower() == 'y'


if __name__ == '__main__':
    while play_hangman():
        print()
