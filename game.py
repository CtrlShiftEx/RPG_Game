from character import Character, create_character

hero = create_character()
hero.display_stats()

game_running = True

while game_running:
    command = input("\nWhat do you want to do?")

    if command == "quit":
        print("Goodbye!")
        game_running = False