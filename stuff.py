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
            print(f"you lose\n")
            return 0
        else:
            print(f"you took {damage} damage.\n your hp is {a}\n")
            return a

    def Score(self, type):
        if type == 1:
            return 30
        elif type == 2:
            return 5
        elif type == 3:
            return 10
        elif type == 4:
            return 20
        elif type == 5:
            return 66666
        else:
            return 40

    def Punishment(self, type):
        if type == 1:
            return 40
        elif type == 2:
            return 20
        elif type == 3:
            return 30
        elif type == 4:
            return 35
        elif type == 5:
            return 666666
        else:
            return 50

    def gaining(self, type):
        if type == 3:
            print(f"you gained 15 hp, 5 dmg\n")
            self.Hp += 15
            self.Dmg += 5
        elif type == 4:
            print(f"you gained 20 hp, 10 dmg\n")
            self.Hp += 20
            self.Dmg += 10
        elif type == 5:
            print(f"you have gained its divine power\n")
            self.Hp = 66666666
            self.Dmg = 6666666666
        elif type == 6:
            print(f"you gained 35 hp, 25 dmg\n")
            self.Hp += 35
            self.Dmg += 25

