from virtual_games.games.Hangman.helpers import get_word, get_initial_positions, hide_word, check_guess, check_for_win
from virtual_games.core.games_factory import GamesFactory


class Hangman:
    def __init__(self):
        self.word = None
        self.lives = 5
        self.guessed_letters = set()
        self.is_game_over = False

    def play(self, new_game=True):
        if new_game:
            print(self)

        self.word = get_word()
        if len(self.word) >= 7:
            self.lives = 7

        positions = get_initial_positions(len(self.word))
        print(hide_word(self.word, positions))

        while not self.is_game_over:
            guess_letter = input("Guess a letter: ").lower()

            if not guess_letter.isalpha() or len(guess_letter) > 1:
                print('Please enter a single alphabetic character.')
                continue

            new_positions = check_guess(self.word, guess_letter, positions)

            if new_positions == positions:
                if guess_letter in self.guessed_letters:
                    print(f"You have already guessed '{guess_letter}'")
                    print(hide_word(self.word, new_positions))
                else:
                    self.guessed_letters.add(guess_letter)
                    self.lives -= 1
                    if self.lives > 0:
                        print(f'Sorry, this letter is not in the word. Remaining lives: {self.lives} ')
                        print(hide_word(self.word, new_positions))
                    else:
                        self.is_game_over = True
                        print(f'You lost! The word was: {self.word}')

            elif check_for_win(new_positions):
                print(f'Congratulations, you have guessed the word -> {self.word}!')
                self.is_game_over = True

            else:
                print('Good guess!')
                self.guessed_letters.add(guess_letter)
                print(hide_word(self.word, new_positions))
                positions = new_positions

        self.play_again()

    def reset_game(self):
        self.word = None
        self.lives = 5
        self.guessed_letters = set()
        self.is_game_over = False

    def play_again(self):
        play_again = input("Fancy another game? y/n? ").lower()
        while True:
            if play_again not in ['y', 'n']:
                print("Invalid choice. Please answer with 'y' or 'n'")
                continue
            if play_again == 'y':
                self.reset_game()
                self.play(new_game=False)
            return

    def __str__(self):
        return (
            "Welcome to Hangman! Try to guess the word before you run out of lives.\n"
            "- Words are up to 10 characters long.\n"
            "- Choose your mode: set the word yourself or let the game pick a random one.\n"
            "- You get 5 lives for words under 7 characters, and 7 lives for longer words.\n"
            "Let's start the game!"
        )


GamesFactory.register_game('Hangman', Hangman)
