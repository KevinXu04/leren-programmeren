from fruitmand import fruitmand

kleuren = []

kleuren = [item['color'] for item in fruitmand]

print("yellow, green, orange, red, brown\n")
while True:
    vraagKleur = input("Kies een kleur uit. ")
    if vraagKleur in kleuren:
        break
    else:
        print(f"De kleur {vraagKleur} zit er niet in de fruitmand.")
        continue

rond, nietRond = 0, 0
for i in range(len(fruitmand)):
    kleuren = fruitmand[i].get('color')
    if kleuren == vraagKleur:
        if fruitmand[i].get('round'):
            rond += 1
        else:
            nietRond += 1

if rond > nietRond:
    print(f"Er zijn {rond} meer ronde vruchten dan niet ronde vruchten in de kleur {vraagKleur}")
elif rond < nietRond:
    print(f"Er zijn {rond} minder ronde vruchten dan niet ronde vruchten in de kleur {vraagKleur}")
else:
    print(f"Er zijn {rond} ronde vruchten en {nietRond} niet ronde vruchten in de kleur {vraagKleur}")