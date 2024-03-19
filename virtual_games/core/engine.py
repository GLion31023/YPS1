from virtual_games.core.games_factory import GamesFactory


class Engine:
    def __init__(self, factory: GamesFactory):
        self._games_factory = factory
        print('Welcome to Virtual Games!')

    def start(self):
        while True:
            games = self._games_factory.get_games()
            game_list = ', '.join(game.capitalize() for game in games)
            print(f'Currently available games: {game_list}')
            game_input = input("Select a game name or 'quit' to exit: ")
            game = game_input.strip().lower()

            if game == 'quit':
                print('Thank you for playing Virtual Games!')
                break
            try:
                self._games_factory.play(game)
            except ValueError as err:
                print(err.args[0])
