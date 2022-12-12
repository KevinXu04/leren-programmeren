from fruitmand import fruitmand

watermeloen = {
    'name' : 'watermelon',
    'weight' : 900,
    'color' : 'green',
    'round' : True
    }

fruitmand.append(watermeloen)

for x in range(len(fruitmand)):
    print(fruitmand[x]['weight'])