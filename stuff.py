class Game:
    def __init__(self, name, hp, speed, dmg):
        self.Name = name
        self.Hp = int(hp)
        self.Speed = int(speed)
        self.Dmg = int(dmg)

    def Kiir(self):
        print(f"your name is {self.Name}\nStats: dmg = {self.Dmg},\thp = {self.Hp},\tspeed = {self.Speed}")
