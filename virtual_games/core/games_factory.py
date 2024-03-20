from virtual_games.games.Craps.craps import Craps
from virtual_games.games.Hangman.hangman import Hangman


class GamesFactory:
    _games = {}

    @classmethod
    def register_game(cls, game_name, game_class):
        cls._games[game_name.lower()] = game_class

    @staticmethod
    def get_games():
        return list(GamesFactory._games.keys())

    def play(self, game_name):
        game_name = game_name.lower()
        game_class = self._games.get(game_name)
        if not game_class:
            raise ValueError(f'Invalid game name: {game_name}. Please try again:')
        game_instance = game_class()
        return game_instance.play()


GamesFactory.register_game('Hangman', Hangman)
GamesFactory.register_game('Craps', Craps)
