import time

from src import Game, Unit, Knight, Footman

if __name__ == "__main__":
	game = Game(length=10, tick_time=0.5)
	game.spawn_unit(Footman,from_left=True)
	game.spawn_random_unit(from_left=False)
	game.spawn_random_unit(from_left=False)
	game.run(ticks=10)
