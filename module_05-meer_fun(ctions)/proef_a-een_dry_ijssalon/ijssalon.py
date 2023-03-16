from functions import *

nogEen = True

print("Welkom bij Papi Gelato.")

lst = [{'name': 'bolletje', 'aantal': 0, 'prijs': 1.10},
        {'name': 'hoorntje', 'aantal': 0, 'prijs': 1.25},
        {'name': 'bakje', 'aantal': 0, 'prijs': 0.75}]

smaakLst = [{'name': 'aardbei', 'aantal': 0, 'prijs': 1.10, 'key': 'a'},
             {'name': 'chocolade', 'aantal': 0, 'prijs': 1.10, 'key': 'c'},
             {'name': 'munt', 'aantal': 0, 'prijs': 1.10, 'key': 'm'},
             {'name': 'vanille', 'aantal': 0, 'prijs': 1.10, 'key': 'a'}]

toppingLst = [{'name': 'geen', 'aantal': 0, 'prijs': 0, 'key': 'a'},
             {'name': 'slagroom', 'aantal': 0, 'prijs': 0.50, 'key': 'b'},
             {'name': 'sprinkels', 'aantal': 0, 'prijs': 0.30, 'key': 'c'},
             {'name': 'caramel saus', 'aantal': 0, 'prijs': 0, 'key': 'd'}]

smaakTekst = f"Welke smaak wilt u voor bolletje? A) Aardbei, B) Chocolade, C) Munt of D) Vanille?\n "
toppingTekst = "Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?\n "

while nogEen:
    aantal = aantalBolletjes()

    keuze = bakjeOfHoorntje(aantal)

    smaakEnTopping(aantal, smaakLst, smaakTekst)

    smaakEnTopping(aantal, toppingLst, toppingTekst)

    nogEen = meerBestellen()  

    tempLst = bolletjesEnKeuzeBerekening(aantal, keuze, lst)

bon(lst, smaakLst, toppingLst)