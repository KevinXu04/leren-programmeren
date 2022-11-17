import random

kleuren = ("oranje", "blauw", "groen", "bruin")

aantal = int(input("Hoeveel M&M's in de zak? "))

zak = []

for x in range(aantal):
    zak.append(random.choice(kleuren))

print(zak)