import random

score = 0
geraden = 0
ronde = 0

getal = random.randint(1, 1000)

while True:
    if ronde == 20:
        print("Eindescoer = ", score)
        break
    
    while True:
        raad = int(input("Raad het getal\n"))
        y = getal - raad

        if raad == getal:
            print("Goed geraden!")
            score += 1
            ronde += 1
            geraden = 0
            print("Score = ", score)
        
        elif raad < 0:
            print("Lager!")

        elif raad > getal:
            print("Lager!")
            geraden += 1
            if y < 20:
                print("Je bent heel warm!")
            elif y < 50:
                print("Je bent warm!")
        elif raad < getal:
            print("Hoger!")
            geraden += 1
            if y < 20:
                print("Je bent heel  warm!")
            elif y < 50:
                print("Je bent warm!")
        
        if geraden == 10:
            print("Score = ", score)
            getal = random.randint(1, 1000)
            ronde += 1
            vraag = input("Nog een getal raden? Y/N ").lower()
            if vraag == "n":
                exit()
            else:
                geraden = 0
                continue