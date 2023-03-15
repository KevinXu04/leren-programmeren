from functions import *

nogEen = True
keuzeBoolean = True

print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")

while nogEen:

    bakjeOfHoorntje(aantalBolletjes(), keuzeBoolean)

    nogEen, keuzeBoolean = meerBestellen(nogEen, keuzeBoolean)


