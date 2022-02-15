from pygame import init


class Character:
    def __init__(self, name, health, attack, armour):
        self.name = name
        self.health = health
        self.attack = attack
        self.armour = armour

    
    
    def __str__(self) -> str:
        return_string = f"Name: {self.name}\nHealth: {self.health}\nAttack: {self.attack}\nArmour: {self.armour}"
        