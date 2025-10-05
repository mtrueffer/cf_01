class Unit:
    def __init__(self, game, name, speed, health, damage, range, faction, from_left=True):
        self.game = game
        self.name = name
        self.speed = speed
        self.health = health
        self.damage = damage
        self.range = range
        self.faction = faction

        self.direction =  1 if from_left else -1
        self.position = 0 if from_left else game.length

        self.bin_index = None

        self.game.logger.log(
            self.faction,
            f"{self.name} of the {self.faction} team spawned on the {'left' if from_left else 'right'}!",
            self.game.tick
        )

    def move(self):
        if 0 < self.position + self.speed * self.direction < self.game.length:
            self.position += self.speed * self.direction
            self.game.logger.log(
                self.faction,
                f"{self.name} moves to {self.position} in bin {self.bin_index}",
                self.game.tick
            )
        else:
            self.direction *= -1
            self.game.logger.log(
                self.faction,
                f"{self.name} turns around!",
                self.game.tick
            )
            
    def is_alive(self):
        return self.health > 0
