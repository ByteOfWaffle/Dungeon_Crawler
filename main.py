import os
from character import Character #order from import is name, health, damage 
from weapon import Weapon #Order from input is wpn_name, wpn_damage
from enemy import Enemy #Order from import is e_name, e_health
weapon = Weapon("plundger", 20)
player = Character("plundger man", 100, weapon.wpn_damage) 
enemy = Enemy("Skibidi grunt", 100,)

os.system("cls")
print("--------------------------------------------------------------------------------------------------")
print(player.name)
print(weapon.wpn_name)
print(enemy.e_name)

player.attack(enemy)
print("--------------------------------------------------------------------------------------------------")