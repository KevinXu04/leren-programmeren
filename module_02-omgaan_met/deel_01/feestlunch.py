aantalcroissant = input('Hoeveel croissantjes?')
aantalcroissant = int(aantalcroissant)

aantalstokbrood = input('Hoeveel stokbroden?')
aantalstokbrood = int(aantalstokbrood)

croissant = 0.39
stokbrood = 2.78
kortingsbon = 0.50

aantalkortingsbon = 3

betalen = (aantalcroissant * croissant + aantalstokbrood * stokbrood) - (aantalkortingsbon * kortingsbon)
   
print("De feestlunch kost je bij elkaar", betalen, "euro voor de", aantalcroissant, "croissantjes en de", aantalstokbrood, "stokbroden als de", aantalkortingsbon, "kortingsbonnen nog geldig zijn!")