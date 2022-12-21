from fruitmand import fruitmand

for item in fruitmand.copy():
    if item.get('name') == 'druif':
        fruitmand.remove(item)

kleuren = []

for x in range(len(fruitmand)):
    kleuren.append(fruitmand[x]['color'])

verschillendeKleuren = [*set(kleuren)]

print(verschillendeKleuren)