class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        self.stats = {
            "health": 100,
            "attack": 10,
            "defense": 5
        }
        self.inventory = []

def display_stats(self):
    print(f"/n--- {self.name} the {self.character_class} ---")
    print(f"Level: {self.level}")
    print(f"Experience: {self.experience}")
    for stat, value in self.stats.items():
        print(f" {stat.capitalize()}: {value}")