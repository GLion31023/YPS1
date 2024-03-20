from virtual_games.games.Craps.helpers import roll_dice, insufficient_funds


class Craps:
    def __init__(self):
        self._stack = 0

    def play(self, load_game=True):
        self.set_up_game(load_game)

        while True:
            if self._stack >= 10:
                stake = self.place_a_bet()
                if stake:
                    self.roll_dice(stake)
                else:
                    print(f"Cash out: {self._stack}")
                    break
            else:
                decision = insufficient_funds(self._stack)
                if decision == 'a':
                    self.buy_in_chips()
                elif decision == 'e':
                    break

        print(f"Thanks for playing!")
        self.play_again()

    def roll_dice(self, stake):
        result = roll_dice()
        if result in (7, 11):
            self.win(stake)
        elif result in (2, 3, 12):
            self.lose()
        else:
            self.roll_point(result, stake)

    def roll_point(self, point, stake):
        while True:
            print(f"Rolling again..")
            new_roll = roll_dice()
            if new_roll == point:
                self.win(stake)
                break
            elif new_roll == 7:
                self.lose()
                break

    def win(self, stake):
        self._stack += stake * 2
        print(f"Congrats, you won {stake * 2}! Available chips: {self._stack}")

    def lose(self):
        print(f"You lost! Available chips: {self._stack}. Better luck next time!")

    def place_a_bet(self):
        while True:
            try:
                bet_amount = int(input(f"Place your bet please: "))

                if bet_amount < 10:
                    print("Min bet is 10.")
                    continue

                if bet_amount > self._stack:
                    decision = insufficient_funds(self._stack)
                    if decision == 'a':
                        self.buy_in_chips()
                    elif decision == 'e':
                        return False

                self._stack -= bet_amount
                return bet_amount

            except ValueError:
                print("Please enter a valid number")

    def set_up_game(self, load_game):
        if load_game:
            print(self)

        self.buy_in_chips()

    def buy_in_chips(self):
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

    def play_again(self):
        while True:
            play_again = input("Would you like to play again? y/n? ").lower()
            if play_again == 'y':
                self._stack = 0
                self.play(load_game=False)
                break
            elif play_again == 'n':
                break
            else:
                print("Invalid choice. Continue with 'y' or 'n'")

    def __str__(self):
        return (
            """Welcome to Craps! This is a game of chance and it is played by one player who tosses 2 dice. 
            - The player wins if they roll a 7 or 11 on the first roll.
            - The player loses if they roll a 2, 3, or 12 on the first roll.
            - If the player rolls any other number, the game continues until they either roll their point again,
              (in which case they win) or rolls a 7 (in which case they lose). 
            - Minimum bet is 10. Winning bets pay out double. - Set your balance at the beginning of the game.
            - Good luck! Let's Play!"""
        )