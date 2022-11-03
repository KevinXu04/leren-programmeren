import random

naam = input("Wat is je naam? ")
aantal = int(input("Hoeveel complimenten wil je? "))
vorig_compliment = "" 

list = [f"Je bent geweldig {naam}", f"{naam} jouw lach is adembenemend.", f"{naam} jouw glimlach doet mijn hart smelten.", f"{naam} jouw rust doet mij goed."]

for x in range(aantal):
    compliment = random.choice(list)
    while vorig_compliment == compliment:
        compliment = random.choice(list)
    print(compliment)
    vorig_compliment = compliment