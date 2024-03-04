import random

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