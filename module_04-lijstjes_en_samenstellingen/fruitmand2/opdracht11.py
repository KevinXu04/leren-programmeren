from fruitmand import fruitmand

kleuren = [item['color'] for item in fruitmand if item['round'] == False]

print("yellow, green, orange, red, brown\n")
vraagKleur = ''
while vraagKleur not in kleuren:
    vraagKleur = input("Kies een kleur uit. ")
    if vraagKleur not in kleuren:
        print(f"De kleur {vraagKleur} zit er niet in de fruitmand.")

rond, nietRond = 0, 0
for fruit in fruitmand:
    kleuren = fruit['color']
    if kleuren == vraagKleur:
        if fruit['round']:
            rond += 1
        else:
            nietRond += 1

if rond > nietRond:
    print(f"Er zijn {rond-nietRond} meer ronde vruchten dan niet ronde vruchten in de kleur {vraagKleur}")
elif rond < nietRond:
    print(f"Er zijn {nietRond-rond} minder ronde vruchten dan niet ronde vruchten in de kleur {vraagKleur}")
else:
    print(f"Er zijn {rond} ronde vruchten en {nietRond} niet ronde vruchten in de kleur {vraagKleur}")