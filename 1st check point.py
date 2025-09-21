import random


while True:
    print("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!")


    Counter_blin = 0
    Input_blin = input()


    if Input_blin == "ПОКА!":
        Counter_blin = Counter_blin + 1
        if Counter_blin == 3:
            print("ДО СВИДАНИЯ, МИЛЫЙ!")
            break
        else:
            Year_blin = random.randint(1930, 1950)
            print("НЕТ, НИ РАЗУ С " + str(Year_blin) + " ГОДА!")
    else:
        Counter_blin = 0
        if Input_blin.isupper():
            Year_blin = random.randint(1930, 1950)
            print("НЕТ, НИ РАЗУ С " + str(Year_blin) + " ГОДА!")
        else:
            print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")