from fruitmand import fruitmand

maxLengte = 0
for item in range (0,len(fruitmand)):
    langsteNaam = len(fruitmand[item]['name'])
    if langsteNaam > maxLengte:
        maxLengte = langsteNaam
        naam = (fruitmand[item].get('name'))
        gewicht = (fruitmand[item].get('weight'))
        kleur = (fruitmand[item].get('color'))

nieuweKleuren = {
    'yellow' : 'geel',
    'green' : 'groen',
    'purple' : 'paars',
    'pink' : 'roze',
    'black' : 'zwart',
    'orange' : 'oranje',
    'brown' : 'bruin'
}

print(f'De "{naam}" ({maxLengte} letters) heeft een {nieuweKleuren[kleur]} kleur en weegt {gewicht/1000} kg.')