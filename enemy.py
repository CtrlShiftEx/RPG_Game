class Enemy:
    def __init__(self, name, enemy_type):
        self.name = name
        self.enemy_type = enemy_type
        self.stats = {
            "health": 50,
            "attack": 8,
            "defense": 3
        }
        self.loot = []
        self.is_alive = True

    def display_stats(self):
        print(f"\n--- {self.name} the {self.enemy_type} ---")
        for stat, value in self.stats.items():
            print(f"  {stat.capitalize()}: {value}")

    def take_damage(self, amount):
        self.stats["health"] -= amount
        if self.stats["health"] <= 0:
            self.stats["health"] = 0
            self.is_alive = False
            print(f"{self.name} has been defeated!")
        else:
            print(f"\n{self.name} takes {amount} damage! Remaining health: {self.stats['health']}")