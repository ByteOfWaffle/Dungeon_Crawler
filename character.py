class Character:
    def __init__(self, name, health, damage):
        self.name = name 
        self.health = health
        self.damage = damage
    def attack(self, target):
        target_e_health = target.e_health
        new_helth = target_e_health - self.damage
        target.e_health = new_helth
        print(f"{self.name} attacked {target.e_name}")
        print(f"{target.e_name} now has {target.e_health} health")