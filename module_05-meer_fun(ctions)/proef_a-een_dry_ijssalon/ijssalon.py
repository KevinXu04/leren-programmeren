from functions import *

nogEen = True
eersteKeer = True
keuzeBoolean = True

while nogEen:
    if eersteKeer:
        print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")

    while True:
        try:
            aantal = int(input("Hoeveel bolletjes wilt u? "))
            break
        except:
            print("Sorry dat snap ik niet...")

    aantalBolletjes(aantal, keuzeBoolean)

    nogEen, eersteKeer, keuzeBoolean = meerBestellen(nogEen, eersteKeer, keuzeBoolean)


