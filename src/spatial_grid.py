from .utils import have_same_sign

class SpatialGrid:
    def __init__(self, bin_size, logger=None, tick=0):
        self.bin_size = bin_size
        self.bins = {}
        self.logger = logger
        self.tick = tick

    def get_bin_index(self, position):
        return int(position // self.bin_size)

    def add(self, unit):
        idx = self.get_bin_index(unit.position)
        self.bins.setdefault(idx, []).append(unit)
        unit.bin_index = idx

    def remove(self, unit):
        self.bins[unit.bin_index].remove(unit)

    def move(self, unit):
        new_idx = self.get_bin_index(unit.position)
        if new_idx != unit.bin_index:
            self.remove(unit)
            self.add(unit)

    def nearby(self, unit, vision_range):
        idx = unit.bin_index
        nearby_units = []
        for neighbour_idx in (idx - 1, idx, idx + 1):
            for other in self.bins.get(neighbour_idx, []):
                if other is not unit:
                    dist = other.position - unit.position
                    if self.logger:
                        self.logger.log(
                            "",
                            f"unit: {unit.name}, dist: {dist}, range: {vision_range}, unit direction: {unit.direction}",
                            self.tick,
                            "debug"
                        )
                    if abs(dist) <= vision_range and have_same_sign(dist,unit.direction):
                        nearby_units.append(other)
        return nearby_units