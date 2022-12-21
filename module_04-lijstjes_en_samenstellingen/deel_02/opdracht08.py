from fruitmand import fruitmand

watermeloen = {
    'name' : 'watermelon',
    'weight' : 900,
    'color' : 'green',
    'round' : True
    }

fruitmand.append(watermeloen)

alleGewichten = []

for x in range(len(fruitmand)):
    alleGewichten.append(fruitmand[x]['weight'])

totaalGewicht = sum(alleGewichten)

print(totaalGewicht)