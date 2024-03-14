import random
class enemystat:
    def __init__(self, name, hp, speed, damage):
        self.Name = name
        self.Hp = hp
        self.Spd = speed
        self.Dmg = damage

    def Enemykiir(self):
        print(f"enemy name is {self.Name}\nStats: dmg = {self.Dmg},\thp = {self.Hp},\tspeed = {self.Spd}")

    def Efight(self, damage):
        a = self.Hp
        a = a - damage
        print(f"it took {damage} damage.\n its hp is {a}")
        if a <= 0:
            print("you win")
            return 0