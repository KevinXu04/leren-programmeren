import random

kleuren = ["rood", "blauw", "groen", "geel", "bruin", "zwart"]

aantal = int(input("Hoeveel M&M's in de zak? "))

zak = []

for x in range(aantal):
    zak.append(random.choice(kleuren))

zak2 = {}

for zak in zak:
    if zak in zak2:
        zak2[zak] += 1
    else:
        zak2[zak] = 1

for key, value in zak2.items():
    if value > 0:
        print(key, ":", value)

# Kleuren zonder aantal niet in zak zien en als er een kleur toevoegd dat hij wel in de zak komt.