class Unit:
    def __init__(self, name, speed, health, damage, range, battlefield_length, from_left=True):
        self.name = name
        self.speed = speed
        self.health = health
        self.damage = damage
        self.range = range
        self.battlefield_length = battlefield_length

        self.direction =  1 if from_left else -1
        self.position = 0 if from_left else battlefield_length

    def move(self):
        if 0 < self.position + self.speed * self.direction < self.battlefield_length:
            self.position += self.speed * self.direction
            print(f"{self.name} moves to {self.position}")
        else:
            self.direction *= -1
            print(f"{self.name} turns around!")

    def is_alive(self):
        return self.health > 0
