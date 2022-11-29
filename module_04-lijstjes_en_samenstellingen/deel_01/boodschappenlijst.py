boodschappen = {}

while True:
    item = input("Wat wil je toevoegen? ")
    aantal = int(input("Hoeveel wil je er hebben? "))
    
    if item in boodschappen.keys():
        boodschappen[item] += aantal
    else:
        boodschappen.update({item : aantal})

    vraag = input("Wil je nog iets toevoegen? ")
    if vraag in("n", "no"):
        break

print("-[ BOODSCHAPPENLIJST ]-")
for key, value in boodschappen.items():
    print(value, "x", key )
print("-----------------------")