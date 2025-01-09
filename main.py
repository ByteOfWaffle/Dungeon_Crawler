import os
import time
from character import Character #order from import is name, health, damage 
from weapon import Weapon #Order from input is wpn_name, wpn_damage
from enemy import Enemy #Order from import is e_name, e_health, e_attack, e_damage
weapon = Weapon("plundger attack", 20)
player = Character("plundger man", 100, weapon.wpn_damage) 
enemy = Enemy("Skibidi grunt", 100, "Bite", 10)


def battle():
    os.system("cls")
    print("1. Thrust")
    print("2. Slash")
    print("3. Bonk")
    choice = input("What attack will you use?")
    if choice = 1
    
    print("--------------------------------------------------------------------------------------------------")
    print(player.name)
    time.sleep(1)
    print(weapon.wpn_name)
    time.sleep(1)
    print(f"{enemy.e_name} was hit")
    time.sleep(1)
    print(enemy.e_name)
    print(enemy.e_attack)
    print(f"{player.name} was hit")
    player.attack(enemy)
    time.sleep(0.5)
    print("--------------------------------------------------------------------------------------------------")
# Main battle loop
while True: #loops
    battle()
    if enemy.e_health <= 0:
        print("You win")
        break #Break ends loop
    elif player.health <= 0:
        print("You lose")
        break