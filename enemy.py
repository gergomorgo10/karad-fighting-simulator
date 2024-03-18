import random
class enemystat:
    def __init__(self, name, hp, speed, damage):
        self.Name = name
        self.Hp = hp
        self.Spd = speed
        self.Dmg = damage

    def Enemykiir(self):
        print(f"enemy name is {self.Name}\nStats: dmg = {self.Dmg},\thp = {self.Hp},\tspeed = {self.Spd}\n")

    def Efight(self, damage, hp):
        a = hp
        b = self.Hp
        a = a - damage
        if a <= 0:
            print(f"it took {damage} damage\n")
            print("you win")
            return 0
        elif damage >= b:
            print(f"you obliterated the enemy with the damage of {damage}\n")
            print("you win")
            return 0
        else:
            print(f"it took {damage} damage.\n its hp is {a}\n")
            return a

