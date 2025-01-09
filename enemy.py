class Enemy:
    def __init__(self, e_name, e_health, e_attack, e_damage):
        self.e_name = e_name
        self.e_health = e_health
        self.e_attack = e_attack
        self.e_damage = e_damage

    def attack(self, target):
        target.health - self.e_attack
        print(f"{self.e_name} attacked {target.name}")
        print(f"{target.name} now has {target.health} health")    