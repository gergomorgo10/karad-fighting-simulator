import random
class enemystat:
    def __init__(self, name, hp, speed, damage):
        self.Name = name
        self.Hp = hp
        self.Spd = speed
        self.Dmg = damage

    def Enemykiir(self):
        print(f"enemy name is {self.Name}\nStats: dmg = {self.Dmg},\thp = {self.Hp},\tspeed = {self.Spd}")