from typing import Optional

from virtual_games.games.game import Game
from virtual_games.games.Hangman.helpers import (get_word, get_initial_positions, hide_word, get_valid_guess,
                                                 check_guess, check_for_win)


class Hangman(Game):
    def __init__(self):
        super().__init__()
        self._word: Optional[str | None] = None
        self._lives: int = 5
        self._guessed_letters = set()

    def play(self, load_game: bool = True) -> None:
        self.set_up_game(load_game)
        positions = get_initial_positions(len(self._word))
        print(hide_word(self._word, positions))

        while self._game_is_active:
            guess = get_valid_guess()
            new_positions = check_guess(self._word, guess, positions)

            if new_positions == positions:
                self.handle_unsuccessful_guess(guess, new_positions)
            else:
                positions = self.handle_successful_guess(guess, new_positions)

        self.play_again()

    def set_up_game(self, load_game: bool) -> None:
        if load_game:
            print(self)

        self._word = get_word()

        if len(self._word) >= 7:
            self._lives = 7

    def handle_unsuccessful_guess(self, guess: str, new_positions: list[bool]) -> None:
        if guess in self._guessed_letters:
            print(f"You have already guessed '{guess}'")
        else:
            self._guessed_letters.add(guess)
            self._lives -= 1

            if self._lives == 0:
                self._game_is_active = False
                print(f'You lost! The word was: {self._word}')
                return

            print(f"Sorry, '{guess}' is not in the word. Remaining lives: {self._lives} ")

        print(hide_word(self._word, new_positions))

    def handle_successful_guess(self, guess: str, new_positions: list[bool]) -> Optional[list | None]:
        if check_for_win(new_positions):
            print(f'Congratulations, you have guessed the word -> {self._word}!')
            self._game_is_active = False
            return
        print('Good guess!')
        self._guessed_letters.add(guess)
        print(hide_word(self._word, new_positions))
        positions = new_positions
        return positions

    def reset_game(self) -> None:
        self._word = None
        self._lives = 5
        self._guessed_letters = set()
        self._game_is_active = True

    def __str__(self):
        return (
            "Welcome to Hangman! Try to guess the word before you run out of lives.\n"
            "- Words are up to 10 characters long.\n"
            "- Choose your mode: set the word yourself or let the game pick a random one.\n"
            "- You get 5 lives for words under 7 characters, and 7 lives for longer words.\n"
            "Let's start the game!"
        )
