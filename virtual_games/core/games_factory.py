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
            raise ValueError(f'Invalid game name or command: {game_name}. Please select again:')
        game_instance = game_class()
        return game_instance.play()
