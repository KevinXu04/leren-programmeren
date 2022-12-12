from fruitmand import fruitmand


for x in range(len(fruitmand)):
    print(fruitmand[x]['color'])
vraag = input("Kies een kleur uit. ")

if vraag in fruitmand['color']:
    print("Hij is rond")