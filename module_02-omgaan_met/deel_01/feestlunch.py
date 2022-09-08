croissant = 0.39
stokbrood = 2.78
kortingsbon = 0.50

aantalcroissant = 17
aantalstokbrood = 2
aantalkortingsbon = 3

aantalcroissant = int(aantalcroissant)
aantalstokbrood = int(aantalstokbrood)
aantalkortingsbon = int(aantalkortingsbon)

croissant = float(croissant)
stokbrood = float(stokbrood)
kortingsbon = float(kortingsbon)

betalen = (aantalcroissant * croissant + aantalstokbrood * stokbrood) - (aantalkortingsbon * kortingsbon)

print('Te betalen:', betalen)   