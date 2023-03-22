import random

a = random.randint(1,10000)
b = random.randint(1,10000)

c = a + b

vraag = int(input(f"Wat is {a} + {b}? "))

if vraag == c:
    print("Goed")
else:
    print("dead")
    exit()