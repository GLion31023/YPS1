from virtual_games.core.games_factory import GamesFactory
from virtual_games.core.engine import Engine

# This import register the game as a side effect
from virtual_games.games.Hangman.Hangman import Hangman

games_factory = GamesFactory()
engine = Engine(games_factory)

engine.start()
