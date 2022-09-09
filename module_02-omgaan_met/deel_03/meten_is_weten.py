a = int(input("Kies een getal"))
b = int(input("Kies een getal"))

if a > b:
    max = a
    min = b
    print("a is het grootste getal:", max)
    print("Het minimum is:", b)
    print("Het maximum is:", a)
elif a < b:
    min = a
    max = b
    print("a is het kleinste getal:", min)
    print("Het minimum is:", a)
    print("Het maximum is:", b)
else :
    print("a is gelijk aan b")