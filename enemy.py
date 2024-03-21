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
        if damage == 9999999 and a <= 0:
            print(" ")
            return 0
        elif damage >= b and a <= 0:
            print(f"you obliterated the enemy with the damage of {damage}\n")
            print(f"you win\n")
            return 0
        elif a <= 0:
            print(f"it took {damage} damage\n")
            print(f"you win\n")
            return 0
        else:
            print(f"it took {damage} damage.\n its hp is {a}\n")
            return a

