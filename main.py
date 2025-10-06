from src import Game

def main():
    game = Game(battlefield_length=20,ticks=10,console_level="debug")
    #game.spawn_random_unit()
    #game.spawn_random_unit()
    game.spawn_unit("Footman","Red",from_left=True)
    game.spawn_unit("Footman","Blue",from_left=False)
    game.spawn_unit("Footman","Red",from_left=True)
    game.spawn_unit("Footman","Blue",from_left=False)
    game.run()

if __name__ == "__main__":
    main()
