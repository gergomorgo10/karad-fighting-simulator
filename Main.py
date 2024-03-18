import random
import stuff
import enemy

print("Welcom to karád simulator")

name = input("what is your username? : ")

decision = int(input("are you sure? (1 yes , 2 no)  :"))

while decision <= 0 or decision > 2:
    print("nope")
    decision = int(input("are you sure? (1 yes , 2 no)  :"))

while decision != 1:
    if decision == 2:
        name = input("what is your username? : ")
        decision = int(input("are you sure? (1 yes , 2 no)  :"))
        while decision <= 0 or decision > 2:
            print("nope")
            decision = int(input("are you sure? (1 yes , 2 no)  :"))


gameclass = int(input("which class do you want? (1. heavy {has higher damage and health}, 2. speedster  {has higher speed and health}, 3. glass cannon  {has higher damage and speed} )    : "))

while gameclass < 1 or gameclass > 3:
    print("there are only 3 classes")
    gameclass = int(input("which class do you want? (1. heavy {has higher damage and health}, 2. speedster  {has higher speed and health}, 3. glass cannon  {has higher damage and speed} )    : "))

decision2 = int(input("are you sure? (1 yes , 2 no)  :"))

while decision2 <= 0 or decision > 2:
    print("nope")
    decision2 = int(input("are you sure? (1 yes , 2 no)  :"))

while decision2 != 1:
    if decision2 == 2:
        gameclass = int(input("which class do you want? (1. heavy {has higher damage and health}, 2. speedster  {has higher speed and health}, 3. glass cannon  {has higher damage and speed} )    : "))
        while gameclass < 1 or gameclass > 3:
            print("there are only 3 classes")
            gameclass = int(input("which class do you want? (1. heavy {has higher damage and health}, 2. speedster  {has higher speed and health}, 3. glass cannon  {has higher damage and speed} )    : "))
        decision2 = int(input("are you sure? (1 yes , 2 no)  :"))
        while decision2 <= 0 or decision2 > 2:
            print("nope")
            decision2 = int(input("are you sure? (1 yes , 2 no)  :"))

characterstat = []

throwawaylist = []

if gameclass == 1:
    speed = 10
    hp = 300
    damage = 65
    throwawaylist.append(name)
    throwawaylist.append(hp)
    throwawaylist.append(speed)
    throwawaylist.append(damage)
    a = stuff.Game(throwawaylist[0], throwawaylist[1], throwawaylist[2], throwawaylist[3])
    characterstat.append(a)

if gameclass == 2:
    speed = 30
    hp = 100
    damage = 50
    throwawaylist.append(name)
    throwawaylist.append(hp)
    throwawaylist.append(speed)
    throwawaylist.append(damage)
    a = stuff.Game(throwawaylist[0], throwawaylist[1], throwawaylist[2], throwawaylist[3])
    characterstat.append(a)

if gameclass == 3:
    speed = 20
    hp = 60
    damage = 80
    throwawaylist.append(name)
    throwawaylist.append(hp)
    throwawaylist.append(speed)
    throwawaylist.append(damage)
    a = stuff.Game(throwawaylist[0], throwawaylist[1], throwawaylist[2], throwawaylist[3])
    characterstat.append(a)

characterstat[0].Kiir()

Enemy = int(characterstat[0].Enemygenerator())

enemystatok = []

if Enemy == 1:
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
    enemystatok.append(a)
elif Enemy == 2:
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
    enemystatok.append(a)
elif Enemy == 3:
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
    enemystatok.append(a)
elif Enemy == 4:
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
    enemystatok.append(a)
elif Enemy == 5:
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
    enemystatok.append(a)
elif Enemy == 6:
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
    enemystatok.append(a)
print(enemystatok[0].Enemykiir())

enemyhp = enemystatok[0].Hp

playerhp = characterstat[0].Hp

ehp = enemyhp

while enemyhp > 0 and playerhp > 0:
    if enemystatok[0].Spd > characterstat[0].Speed:
        print(f"enemy attacks\n")
        eattack = random.randint(enemystatok[0].Dmg - 10, enemystatok[0].Dmg + 10)
        playerhp = characterstat[0].Fight(eattack, playerhp)
        if playerhp <= 0:
            print(" ")
        elif playerhp > 0:
            print(f"your turn\n")
            options = int(input("what do you want to do? [1  run,   2 attack] : "))
            while options < 1 or options > 2:
                print("you can only choose between 1 and 2")
                options = int(input("what do you want to do? [1  run,   2 attack] : "))
            if options == 1:
                chance = random.randint(1, 100)
                if chance > 20 and chance < 60:
                    print(f"sikeresen elszöktél\n")
                    enemyhp = enemystatok[0].Efight(9999999, enemyhp)
                else:
                    print(f"you failed to escape\n")
            elif options == 2:
                pattack = random.randint(characterstat[0].Dmg - 10, characterstat[0].Dmg + 10)
                enemyhp = enemystatok[0].Efight(pattack, enemyhp)



