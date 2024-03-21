class Game:
    def __init__(self):
        self._game_is_active: bool = True

    def play(self, load_game: bool = True):
        pass

    def set_up_game(self, load_game: bool) -> None:
        pass

    def reset_game(self):
        pass

    def play_again(self):
        while True:
            play_again = input("Would you like to play again? y/n? ").lower()
            if play_again == 'y':
                self.reset_game()
                self.play(load_game=False)
                return
            elif play_again == 'n':
                print(f"Thanks for playing!")
                return
            else:
                print("Invalid choice. Continue with 'y' or 'n'")

    def __str__(self):
        pass
