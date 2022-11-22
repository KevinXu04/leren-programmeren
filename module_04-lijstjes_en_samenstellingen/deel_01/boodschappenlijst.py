boodschappen = []

while True:
    item = input("Voeg uw boodschap toe. Type n om te stoppen. ")
    if item == "n":
        break
    aantal = int(input("Hoeveel wil je ervan hebben? "))
    boodschap = [item, aantal]
    boodschappen.append(boodschap)
    

print("-[ BOODSCHAPPENNLIJST ]- ")
b = 0
for x in boodschappen:
    aantal = int(boodschappen[b][1])
    item = boodschappen[b][0]
    print(f'{aantal} x  {item} ')
    b += 1
print('------------------------')