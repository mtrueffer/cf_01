import time
import random

from .unit import Unit
from .utils import load_unit_stats

class Game:
    def __init__(self, battlefield_length=20, unit_stats_file="src/unit_stats.csv", tick_time=1):
        self.units = []
        self.battlefield_length = battlefield_length
        self.unit_stats = load_unit_stats(unit_stats_file)
        self.unit_counters = {}
        self.tick_time = tick_time
        self.tick_count = 0

    def spawn_unit(self, unit_type, from_left=True):
        if unit_type not in self.unit_stats:
            raise ValueError(f"Unknown unit type: {unit_type}")

        stats = self.unit_stats[unit_type]
        if unit_type not in self.unit_counters:
            self.unit_counters[unit_type] = 1
        else:
            self.unit_counters[unit_type] += 1
        name = f"{unit_type} {self.unit_counters[unit_type]}"
        unit = Unit(
            name=name,
            speed=stats["speed"],
            health=stats["health"],
            damage=stats["damage"],
            range=stats["range"],
            battlefield_length=self.battlefield_length,
            from_left=from_left
        )
        self.units.append(unit)
        print(f"{name} spawned on the {'left' if from_left else 'right'} side at {unit.position}")

    def spawn_random_unit(self):
        unit_type = random.choice(list(self.unit_stats.keys()))
        from_left = random.choice([True, False])
        self.spawn_unit(unit_type, from_left)

    def update(self):
        self.tick_count += 1
        print(f"\n--- Tick {self.tick_count} ---")

        for unit in self.units:
            if unit.is_alive():
                unit.move()
                if unit.position >= self.battlefield_length:
                    print(f"{unit.name} reached the end!")
            else:
                print(f"{unit.name} is dead and does not move.")

    def run(self, ticks=10):
        for _ in range(ticks):
            self.update()
            time.sleep(self.tick_time)
