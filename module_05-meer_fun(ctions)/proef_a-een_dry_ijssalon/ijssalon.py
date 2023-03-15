from functions import *

nogEen = True

print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")

while nogEen:

    aantal, keuze = bakjeOfHoorntje(aantalBolletjes())

    nogEen = meerBestellen(nogEen)

    bon(aantal, keuze, nogEen)


