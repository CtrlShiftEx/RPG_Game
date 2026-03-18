import sys
sys.path.insert(0, ".")

from character import Character

def test_character_creation():
    hero = Character("Aldric", "Warrior")
    assert hero.name == "Aldric"
    assert hero.character_class == "Warrior"
    assert hero.level == 1
    assert hero.experience == 0
    print("test_character_creation PASSED ✅")

def test_character_stats():
    hero = Character("Aldric", "Warrior")
    assert hero.stats["health"] == 100
    assert hero.stats["attack"] == 10
    assert hero.stats["defense"] == 5
    print("test_character_stats PASSED ✅")

def test_character_inventory():
    hero = Character("Aldric", "Warrior")
    assert hero.inventory == []
    hero.inventory.append("sword")
    assert hero.inventory == ["sword"]
    print("test_character_inventory PASSED ✅")

# Run all tests
test_character_creation()
test_character_stats()
test_character_inventory()