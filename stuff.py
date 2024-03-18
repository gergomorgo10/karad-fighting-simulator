import random
import enemy
class Game:
    def __init__(self, name, hp, speed, dmg):
        self.Name = name
        self.Hp = int(hp)
        self.Speed = int(speed)
        self.Dmg = int(dmg)

    def Kiir(self):
        print(f"your name is {self.Name}\nStats: dmg = {self.Dmg},\thp = {self.Hp},\tspeed = {self.Speed}")

    def Enemygenerator(self):
        ranszam = random.randint(1, 100000)
        if ranszam >= 1 and ranszam < 5000:
            print(f"mugger has appeared\n")
            return 1
        elif ranszam >= 5000 and ranszam < 10000:
            print(f"kindergarten kid has appeared\n")
            return 2
        elif ranszam >= 10000 and ranszam < 30000:
            print(f"kid gypsy has appeared\n")
            return 3
        elif ranszam >= 30000 and ranszam < 66666:
            print(f"adult gypsy has appeared\n")
            return 4
        elif ranszam == 66666:
            print(f"D2 crawls into this reality\n")
            return 5
        elif ranszam > 66666 and ranszam <= 100000:
            print(f"banklifter has appeared\n")
            return 6

    def Fight(self, damage, hp):
        a = hp
        b = self.Hp
        a = a - damage
        if a <= 0:
            print(f"you took {damage} damage\n")
            print("you lose")
            return 0
        elif damage >= b:
            print(f"it obliterated you with the damage of {damage}\n")
            print("you lose")
            return 0
        else:
            print(f"you took {damage} damage.\n your hp is {a}\n")
            return a
