from fruitmand import fruitmand
import random

aantal = int(input("Aantal? "))

for x in range(aantal):
    fruit = random.choice(fruitmand)
    print(fruit['name'])