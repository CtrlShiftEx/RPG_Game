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
        print(f"\n--- {self.name} the {self.character_class} ---")
        print(f"Level: {self.level}")
        print(f"Experience: {self.experience}")
        for stat, value in self.stats.items():
            print(f" {stat.capitalize()}: {value}")

    def level_up(self):
        self.level += 1
        self.stats["health"] += 20
        self.stats["attack"] += 5
        self.stats["defense"] += 3
        print(f"\n {self.name} leveled up! Now level {self.level}!")

def create_character():
    print("=== Create Your Character ===")
    name = input("Enter your character's name: ")
    print("\n Choose your class: ")
    print("   1. Warrior")
    print("   2. Mage")
    print("   3. Rogue")
    choice = input("Enter 1, 2, or 3: ")

    classes = {
        "1": "Warrior",
        "2": "Mage",
        "3": "Rogue"
    }

    character_class = classes.get(choice, "Warrior")
    hero = Character(name, character_class)
    print(f"\nWelcome, {hero.name} the {hero.character_class}!")
    return hero
