import csv

def load_unit_stats(filepath):
    unit_stats = {}
    with open(filepath,newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row["name"]
            unit_stats[name] = {
                "speed": float(row["speed"]),
                "health": int(row["health"]),
                "damage": int(row["damage"]),
                "damage_type": row["damage_type"],
                "attack_rate": float(row["attack_rate"]),
                "range": int(row["range"]),
                "armor": int(row["armor"]),
                "armor_type": row["armor_type"],
                "spawn_rate": float(row["spawn_rate"])
            }
    return unit_stats
