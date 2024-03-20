from typing import Optional

from virtual_games.games.Craps.helpers import roll_dice, insufficient_funds


class Craps:
    def __init__(self):
        self.game_is_active: bool = True
        self._stack: int = 0

    def play(self, load_game: bool = True) -> None:
        self.set_up_game(load_game)

        while self.game_is_active:
            if self._stack < 10:
                decision = insufficient_funds(self._stack)

                if decision == 'a':
                    self.buy_in_chips()
                else:
                    self.game_is_active = False

            else:
                stake = self.place_a_bet()

                if stake:
                    self.roll_dice(stake)
                else:
                    print(f"Cash out: {self._stack}")
                    self.game_is_active = False

        self.play_again()

    def roll_dice(self, stake) -> None:
        result = roll_dice()
        if result in (7, 11):
            self.win(stake)
        elif result in (2, 3, 12):
            self.lose()
        else:
            self.roll_point(result, stake)

    def roll_point(self, point, stake) -> None:
        while True:
            print(f"Rolling again..")
            new_roll = roll_dice()
            if new_roll == point:
                self.win(stake)
                break
            elif new_roll == 7:
                self.lose()
                break

    def win(self, stake) -> None:
        self._stack += stake * 2
        print(f"Great! You won {stake * 2}! \nAvailable chips: {self._stack}")

    def lose(self) -> None:
        print(f"You lost! Better luck next time!")
        if self._stack >= 10:
            print(f"Available chips: {self._stack}")

    def place_a_bet(self) -> Optional[int | bool]:
        while True:
            try:
                bet_amount = int(input(f"Place your bet please: "))

                if bet_amount < 10:
                    print("The minimum bet is 10.")
                    continue

                if bet_amount % 10 != 0:
                    print("Your stake must be a multiple of 10 (e.g., 10, 20, 30, ...).")
                    continue

                if bet_amount > self._stack:
                    decision = insufficient_funds(self._stack, method='place_a_bet')
                    if decision == 'a':
                        self.buy_in_chips()
                    elif decision == 'b':
                        continue
                    else:
                        return False

                self._stack -= bet_amount

                return bet_amount

            except ValueError:
                print("Please enter a valid number")

    def buy_in_chips(self) -> None:
        while True:
            try:
                add_chips = int(input('Buy-in chips: '))
                self._stack += add_chips
                if self._stack >= 10:
                    print(f"Available chips: {self._stack}")
                    break
                print(f"Available stack: {self._stack}. Minimum bets is 10.")
            except ValueError:
                print("Please enter a valid number")

    def set_up_game(self, load_game) -> None:
        if load_game:
            print(self)

        self.buy_in_chips()

    def reset_game(self) -> None:
        self.game_is_active = True
        self._stack = 0

    def play_again(self) -> None:
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
        return (
            """Welcome to Craps! This is a game of chance and it is played by one player who tosses 2 dice. 
            - The player wins if they roll a 7 or 11 on the first roll.
            - The player loses if they roll a 2, 3, or 12 on the first roll.
            - If the player rolls any other number, the game continues until they either roll their point again,
              (in which case they win) or rolls a 7 (in which case they lose). 
            - Minimum bet is 10. Winning bets pay out double.
            - Set your balance at the beginning of the game.
            - Good luck! Let's Play!"""
        )
