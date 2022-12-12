import random

p = 0
groepA = {}

while p != 3:
    land = input("Welke land? ")
    groepA[land] = 0
    p += 1

for key, value in groepA:
    print(key, ":", value)

score = random.randint(0,7)