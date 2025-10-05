from src import Game

def main():
    game = Game(battlefield_length=20)
    game.spawn_random_unit()
    game.spawn_random_unit()
    game.spawn_unit("Mage",from_left=True)
    game.spawn_unit("Mage",from_left=False)
    game.run(ticks=20)

if __name__ == "__main__":
    main()
