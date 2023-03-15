from functions import *

nogEen = True

print("Welkom bij Papi Gelato.")

lst = [{'name': 'bolletje', 'aantal': 0, 'prijs': 1.10},
        {'name': 'hoorntje', 'aantal': 0, 'prijs': 1.25},
        {'name': 'bakje', 'aantal': 0, 'prijs': 0.75}]

smaakLst = [{'name': 'aardbei', 'aantal': 0, 'prijs': 1.10},
             {'name': 'chocolade', 'aantal': 0, 'prijs': 1.10},
             {'name': 'munt', 'aantal': 0, 'prijs': 1.10},
             {'name': 'vanille', 'aantal': 0, 'prijs': 1.10}]

while nogEen:
    aantal, keuze = bakjeOfHoorntje(aantalBolletjes())

    smaak = smaakKiezen(aantal)

    nogEen = meerBestellen(nogEen)

    tempLst = berekening(aantal, keuze)

    for item in tempLst:
        for i, d in enumerate(lst):
            if d['name'] == item['name']:
                lst[i]['aantal'] += item['aantal']

    for item in smaak:
        for i, d in enumerate(smaakLst):
            if d['name'] == item['name']:
                smaakLst[i]['aantal'] += item['aantal']

bon(lst, smaakLst)