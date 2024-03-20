from virtual_games.games.Hangman.helpers import (get_word, get_initial_positions, hide_word, get_valid_guess,
                                                 check_guess, check_for_win)


class Hangman:
    def __init__(self):
        self._word = None
        self._lives = 5
        self._guessed_letters = set()
        self._is_game_over = False

    def play(self, load_game=True):
        self.set_up_game(load_game)
        positions = get_initial_positions(len(self._word))
        print(hide_word(self._word, positions))

        while not self._is_game_over:
            guess = get_valid_guess()
            new_positions = check_guess(self._word, guess, positions)

            if new_positions == positions:
                self.handle_unsuccessful_guess(guess, new_positions)
            else:
                positions = self.handle_successful_guess(guess, new_positions)

        self.play_again()

    def set_up_game(self, load_game):
        if load_game:
            print(self)

        self._word = get_word()

        if len(self._word) >= 7:
            self._lives = 7

    def handle_unsuccessful_guess(self, guess, new_positions):
        if guess in self._guessed_letters:
            print(f"You have already guessed '{guess}'")
        else:
            self._guessed_letters.add(guess)
            self._lives -= 1

            if self._lives == 0:
                self._is_game_over = True
                print(f'You lost! The word was: {self._word}')
                return

            print(f"Sorry, '{guess}' is not in the word. Remaining lives: {self._lives} ")

        print(hide_word(self._word, new_positions))

    def handle_successful_guess(self, guess, new_positions):
        if check_for_win(new_positions):
            print(f'Congratulations, you have guessed the word -> {self._word}!')
            self._is_game_over = True
            return
        print('Good guess!')
        self._guessed_letters.add(guess)
        print(hide_word(self._word, new_positions))
        positions = new_positions
        return positions

    def reset_game(self):
        self._word = None
        self._lives = 5
        self._guessed_letters = set()
        self._is_game_over = False

    def play_again(self):
        while True:
            play_again = input("Would you like to play again? y/n? ").lower()
            if play_again == 'y':
                self.reset_game()
                self.play(load_game=False)
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
