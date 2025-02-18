import random

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")
    while player.is_alive() and enemy.is_alive():
        action = input("Attack (a) or Run (r)? ").lower()
        if action == 'a':
            enemy.health -= player.attack
            print(f"You attack {enemy.name} for {player.attack} damage.")
            if enemy.is_alive():
                player.health -= enemy.attack
                print(f"{enemy.name} attacks you for {enemy.attack} damage.")
        elif action == 'r':
            print("You ran away!")
            return
        else:
            print("Invalid action!")

    if player.is_alive():
        print(f"You defeated {enemy.name}!")
    else:
        print("You were defeated!")

def main():
    player = Character("Hero", 100, 20)
    enemies = [Character("Goblin", 30, 10), Character("Orc", 50, 15), Character("Dragon", 100, 25)]

    print("Welcome to the RPG Game!")
    while player.is_alive() and enemies:
        battle(player, enemies.pop(0))
        if player.is_alive():
            print("You move to the next area...")
        else:
            print("Game Over!")
            break

if __name__ == "__main__":
    main()
