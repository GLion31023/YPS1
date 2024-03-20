import random
from english_words import get_english_words_set


def set_an_own_word():
    while True:
        word = input("Please enter a secret word between 5-10 letters: ")

        if len(word) < 5 or len(word) > 10:
            print('The word should be between 5 to 10 letters.')
            continue

        if not word.isalpha():
            print('A word cannot contain numbers or special characters!')
            continue

        return word.lower()


def get_word():
    random_words = ([w for w in get_english_words_set(['web2'], lower=True) if 5 <= len(w) <= 10])
    while True:
        type_of_play = input("Choose a mode: Select 'r' to play with a random word or 's' to set your own word: ")
        if type_of_play.lower() == 'r':
            word = random.choice(random_words)
            print('A random word has been generated:')
            return word
        elif type_of_play.lower() == 's':
            word = set_an_own_word()
            return word
        else:
            print(f"Invalid type_of_play: {type_of_play}. Please select 'r' for random or 's' to set a word")
            continue


def get_initial_positions(length):
    return [i == 0 or i == length - 1 for i in range(length)]


def hide_word(word, positions):
    return ''.join(word[i] if positions[i] else '-' for i in range(len(word)))


def get_valid_guess():
    while True:
        guess_letter = input("Guess a letter: ").lower()

        if guess_letter.isalpha() and len(guess_letter) == 1:
            return guess_letter
        else:
            print('Please enter a single alphabetic character.')


def check_guess(word, letter, positions):
    new_positions = positions.copy()
    letter = letter.lower()
    for let in range(len(word)):
        if word[let] == letter:
            new_positions[let] = True

    return new_positions


def check_for_win(positions):
    if all(positions):
        return True
    return False


# to be implemented - stages
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
