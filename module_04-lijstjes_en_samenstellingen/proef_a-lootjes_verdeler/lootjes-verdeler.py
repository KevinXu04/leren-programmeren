import random

lijstNamen = []



while True:
    vraagNamen = input("Geef een naam op. \n")
    lijstNamen.append(vraagNamen)
    if len(lijstNamen) >= 3:
        meer = input("Wil je meer namen toevoegen? \n")
        if meer == "nee":
            break
lijstLoten = lijstNamen.copy()

dictLijstLoten = []

while lijstNamen:
    if lijstNamen[0] != lijstLoten[0]:
        dictLijstLoten.append({lijstNamen[0]: lijstLoten[0]})
        del lijstLoten[0]
        del lijstNamen[0]
    else:
        random.shuffle(lijstLoten)

print(dictLijstLoten)