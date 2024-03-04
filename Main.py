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