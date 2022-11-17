import random

kleuren = ("rood", "blauw", "groen", "geel", "bruin")

aantal = int(input("Hoeveel M&M's in de zak? "))

zak = []

for x in range(aantal):
    zak.append(random.choice(kleuren))

aantalRood = zak.count("rood")
aantalBlauw = zak.count("blauw")
aantalGroen = zak.count("groen")
aantalGeel = zak.count("geel")
aantalBruin = zak.count("bruin")

zak2 = {
    "rood": 0,
    "blauw": 0,
    "groen": 0,
    "geel": 0,
    "bruin": 0
}

zak2["rood"] = aantalRood
zak2["blauw"] = aantalBlauw
zak2["groen"] = aantalGroen
zak2["geel"] = aantalGeel
zak2["bruin"] = aantalBruin

print(zak2)