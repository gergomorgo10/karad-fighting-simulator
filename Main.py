import random
import stuff

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
    hp = 200
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


