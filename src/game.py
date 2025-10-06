import time
import random

from .unit import Unit
from .utils import load_unit_stats
from .logger import Logger
from .spatial_grid import SpatialGrid # type: ignore

class Game:
    def __init__(self, battlefield_length=20, ticks=20, console_level="info", unit_stats_file="src/unit_stats.csv", tick_time=1):
        self.units = []
        self.length = battlefield_length
        self.unit_stats = load_unit_stats(unit_stats_file)
        self.unit_counters = {}
        self.tick_time = tick_time
        self.ticks = ticks
        self.tick = 0
        self.logger = Logger(console_level=console_level)
        self.grid = SpatialGrid(self.length // 4, self.logger, self.tick)

        self.logger.log("none",f"New game with battlefield length of {self.length} that will last {self.ticks} turns.", None, "system") 

    def spawn_unit(self, unit_type, faction, from_left=True):
        if unit_type not in self.unit_stats:
            raise ValueError(f"Unknown unit type: {unit_type}")

        stats = self.unit_stats[unit_type]

        if unit_type not in self.unit_counters:
            self.unit_counters[unit_type] = 1
        else:
            self.unit_counters[unit_type] += 1

        name = f"{unit_type} {self.unit_counters[unit_type]}"
        unit = Unit(
            game=self,
            name=name,
            speed=stats["speed"],
            health=stats["health"],
            damage=stats["damage"],
            range=stats["range"],
            faction=faction,
            from_left=from_left
        )
        self.units.append(unit)
        self.grid.add(unit)

    def spawn_random_unit(self):
        unit_type = random.choice(list(self.unit_stats.keys()))
        faction = random.choice(["Blue", "Red"])
        from_left = random.choice([True, False])
        self.spawn_unit(unit_type, faction, from_left)

    def update(self):
        self.tick += 1

        for unit in self.units:
            if unit.is_alive():
                nearby_units = []
                nearby_units = self.grid.nearby(unit, vision_range=unit.vision)
                for nearby_unit in nearby_units:
                    self.logger.log(unit.faction, f"{unit.name} can see {nearby_unit.name}.", self.tick, "debug")

                unit.move()
                self.grid.move(unit)
                if unit.position >= self.length:
                    self.logger.log(unit.faction, f"{unit.name} reached the end!", self.tick)
            else:
                self.rem_from_bin(unit)
                self.logger.log(unit.faction, f"{unit.name} is dead and does not move.", self.tick)

    def run(self):
        for _ in range(self.ticks):
            self.update()
            time.sleep(self.tick_time)
