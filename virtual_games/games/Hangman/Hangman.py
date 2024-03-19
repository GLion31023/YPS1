from virtual_games.games.Hangman.helpers import (get_word, get_initial_positions, hide_word, get_valid_guess,
                                                 check_guess, check_for_win)
from virtual_games.core.games_factory import GamesFactory


class Hangman:
    def __init__(self):
        self.word = None
        self.lives = 5
        self.guessed_letters = set()
        self.is_game_over = False

    def play(self, is_new_game=True):
        self.set_up_game(is_new_game)
        positions = get_initial_positions(len(self.word))
        print(hide_word(self.word, positions))

        while not self.is_game_over:
            guess = get_valid_guess()
            new_positions = check_guess(self.word, guess, positions)

            if new_positions == positions:
                self.handle_unsuccessful_guess(guess, new_positions)
            else:
                positions = self.handle_successful_guess(guess, new_positions)

        self.play_again()

    def set_up_game(self, new_game):
        if new_game:
            print(self)

        self.word = get_word()

        if len(self.word) >= 7:
            self.lives = 7

    def handle_unsuccessful_guess(self, guess, new_positions):
        if guess in self.guessed_letters:
            print(f"You have already guessed '{guess}'")
        else:
            self.guessed_letters.add(guess)
            self.lives -= 1

            if self.lives == 0:
                self.is_game_over = True
                print(f'You lost! The word was: {self.word}')
                return

            print(f"Sorry, '{guess}' is not in the word. Remaining lives: {self.lives} ")

        print(hide_word(self.word, new_positions))

    def handle_successful_guess(self, guess, new_positions):
        if check_for_win(new_positions):
            print(f'Congratulations, you have guessed the word -> {self.word}!')
            self.is_game_over = True
            return
        print('Good guess!')
        self.guessed_letters.add(guess)
        print(hide_word(self.word, new_positions))
        positions = new_positions
        return positions

    def reset_game(self):
        self.word = None
        self.lives = 5
        self.guessed_letters = set()
        self.is_game_over = False

    def play_again(self):
        while True:
            play_again = input("Fancy another game? y/n? ").lower()
            if play_again == 'y':
                self.reset_game()
                self.play(is_new_game=True)
                break
            elif play_again == 'n':
                break
            else:
                print("Invalid choice. Continue with 'y' or 'n'")

    def __str__(self):
        return (
            "Welcome to Hangman! Try to guess the word before you run out of lives.\n"
            "- Words are up to 10 characters long.\n"
            "- Choose your mode: set the word yourself or let the game pick a random one.\n"
            "- You get 5 lives for words under 7 characters, and 7 lives for longer words.\n"
            "Let's start the game!"
        )


GamesFactory.register_game('Hangman', Hangman)
