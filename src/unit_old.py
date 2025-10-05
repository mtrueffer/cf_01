class Unit:
    def __init__(self, name, battlefield_length, from_left=True, speed=1, health=10):
        self.name = name
        self.speed = speed
        self.health = health
        self.battlefield_length = battlefield_length

        self.direction =  1 if from_left else -1
        self.position = 0 if from_left else battlefield_length

    def move(self):
        self.position += self.speed * self.direction
        print(f"{self.name} moves to {self.position}")

    def is_alive(self):
        return self.health > 0

class Footman(Unit):
    _count = 0

    def __init__(self, battlefield_length, from_left):
        Footman._count += 1
        name = f"Footman {Footman._count}"
        super().__init__(name,battlefield_length=battlefield_length, from_left=from_left, speed=1, health=10)

class Knight(Unit):
    _count = 0

    def __init__(self, battlefield_length, from_left):
        Knight._count += 1
        name = f"Knight {Knight._count}"
        super().__init__(name,battlefield_length=battlefield_length, from_left=from_left, speed=2, health=15)

