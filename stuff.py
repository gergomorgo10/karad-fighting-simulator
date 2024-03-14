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
            print("mugger has appeared")
            return 1
        elif ranszam >= 5000 and ranszam < 10000:
            print("kindergarten kid has appeared")
            return 2
        elif ranszam >= 10000 and ranszam < 30000:
            print("kid gypsy has appeared")
            return 3
        elif ranszam >= 30000 and ranszam < 66666:
            print("adult gypsy has appeared")
            return 4
        elif ranszam == 66666:
            print("D2 crawls into this reality")
            return 5
        elif ranszam > 66666 and ranszam <= 100000:
            print("banklifter has appeared")
            return 6