from character import Character
from assasinys import Assasin


player1 = Character("Katia", 250, 20, 0)
player1.print_stats()

player2 = Assasin("Assasin", 200, 30, 0)
player2.print_stats()

player1.attack(player2)

print("\n\n")
player1.print_stats()
player2.print_stats()

print("\n")

while player1.health > 0 and player2.health > 0:
    player1_damage = player1.attack(player2)
    print(f"{player1.name} aтaкував {player2.name}  наніс {player1_damage} шкоди")
    print(f"{player2.name} лишилося {player2.health}  здоровя")
    player2_damage = player2.attack(player1)
    print(f"{player2.name} aтaкував {player1.name}  наніс {player2_damage-player1.defense} шкоди")
    print(f"{player1.name} лишилося {player1.health}  здоровя")
    print("")
