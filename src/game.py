import time
import random

from .unit import Footman, Knight

class Game:
    def __init__(self, length=20, tick_time=1):
        self.units = []
        self.length = length
        self.tick_time = tick_time
        self.tick_count = 0

    def spawn_unit(self, unit_class, from_left=True):
        unit = unit_class(battlefield_length=self.length, from_left=from_left)
        self.units.append(unit)
        side = "left" if from_left else "right"
        print(f"{unit.name} spawned on the {side} side at {unit.position}")

    def spawn_random_unit(self, from_left=True):
        unit_class = random.choice([Footman, Knight])
        self.spawn_unit(unit_class, from_left=from_left)

    def update(self):
        self.tick_count += 1
        print(f"\n--- Tick {self.tick_count} ---")

        for unit in self.units:
            if unit.is_alive():
                unit.move()
                if unit.position >= self.length:
                    print(f"{unit.name} reached the end!")
            else:
                print(f"{unit.name} is dead and does not move.")

    def run(self, ticks=10):
        for _ in range(ticks):
            self.update()
            time.sleep(self.tick_time)
