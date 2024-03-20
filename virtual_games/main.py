from virtual_games.core.games_factory import GamesFactory
from virtual_games.core.engine import Engine


games_factory = GamesFactory()
engine = Engine(games_factory)

engine.start()
