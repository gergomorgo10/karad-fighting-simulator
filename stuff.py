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

    def Enemystat(self, lista, Etype):
        if Etype == 1:
            throwawaylist = []
            name = "Mugger"
            Hp = 80
            Spd = 20
            dmg = 75
            throwawaylist.append(name)
            throwawaylist.append(Hp)
            throwawaylist.append(Spd)
            throwawaylist.append(dmg)
            a = enemy.enemystat(throwawaylist[0], throwawaylist[1], throwawaylist[2], throwawaylist[3])
            return lista.append(a)
        elif Etype == 2:
            throwawaylist = []
            name = "Kindergarten kid"
            Hp = 50
            Spd = 50
            dmg = 40
            throwawaylist.append(name)
            throwawaylist.append(Hp)
            throwawaylist.append(Spd)
            throwawaylist.append(dmg)
            a = enemy.enemystat(throwawaylist[0], throwawaylist[1], throwawaylist[2], throwawaylist[3])
            return lista.append(a)
        elif Etype == 3:
            throwawaylist = []
            name = "kid gypsy"
            Hp = 65
            Spd = 50
            dmg = 45
            throwawaylist.append(name)
            throwawaylist.append(Hp)
            throwawaylist.append(Spd)
            throwawaylist.append(dmg)
            a = enemy.enemystat(throwawaylist[0], throwawaylist[1], throwawaylist[2], throwawaylist[3])
            return lista.append(a)
        elif Etype == 4:
            throwawaylist = []
            name = "adult gypsy"
            Hp = 120
            Spd = 15
            dmg = 50
            throwawaylist.append(name)
            throwawaylist.append(Hp)
            throwawaylist.append(Spd)
            throwawaylist.append(dmg)
            a = enemy.enemystat(throwawaylist[0], throwawaylist[1], throwawaylist[2], throwawaylist[3])
            return lista.append(a)
        elif Etype == 5:
            throwawaylist = []
            name = "destroyer of worlds (D2)"
            Hp = 66666
            Spd = 66666
            dmg = 66666
            throwawaylist.append(name)
            throwawaylist.append(Hp)
            throwawaylist.append(Spd)
            throwawaylist.append(dmg)
            a = enemy.enemystat(throwawaylist[0], throwawaylist[1], throwawaylist[2], throwawaylist[3])
            return lista.append(a)
        elif Etype == 6:
            throwawaylist = []
            name = "banklifter"
            Hp = 150
            Spd = 20
            dmg = 85
            throwawaylist.append(name)
            throwawaylist.append(Hp)
            throwawaylist.append(Spd)
            throwawaylist.append(dmg)
            a = enemy.enemystat(throwawaylist[0], throwawaylist[1], throwawaylist[2], throwawaylist[3])
            return lista.append(a)

