boodschappen = {}

while True:
    item = input("Wat wil je toevoegen? ").lower()
    aantal = int(input("Hoeveel wil je er hebben? "))
    
    if item in boodschappen.keys():
        boodschappen[item] += aantal
    else:
        boodschappen.update({item : aantal})

    vraag = input("Wil je nog iets toevoegen? ").lower()
    if vraag in("n", "no", "nee", "ne"):
        break

print("-[ BOODSCHAPPENLIJST ]-")
for key, value in boodschappen.items():
    print(value, "x", key )
print("-----------------------")