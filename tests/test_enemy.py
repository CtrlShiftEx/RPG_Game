import sys
sys.path.insert(0, ".")

from enemy import Enemy

def test_enemy_creation():
    goblin = Enemy("Gruk", "Goblin")
    assert goblin.name == "Gruk"
    assert goblin.enemy_type == "Goblin"
    assert goblin.is_alive == True
    assert goblin.stats["health"] == 50
    print("test_enemy_creation PASSED")

def test_take_damage():
    goblin = Enemy("Gruk", "Goblin")
    goblin.take_damage(20)
    assert goblin.stats["health"] == 30
    assert goblin.is_alive == True
    print("test_take_damage PASSED")

def test_enemy_defeated():
    goblin = Enemy("Gruk", "Goblin")
    goblin.take_damage(999)
    assert goblin.stats["health"] == 0
    assert goblin.is_alive == False
    print("test_enemy_defeated PASSED")

test_enemy_creation()
test_take_damage()
test_enemy_defeated()