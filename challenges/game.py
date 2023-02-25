# Een spelletje kost in de winkel 24,95, maar gamewinkels krijgen 40% korting bij inkoop. 
# Het versturen vanuit de leverancier kost 1,00 voor het eerste spel, en 25 cent voor ieder volgende game. 
# Bereken hoeveel de gamewinkel betaalt voor 60 spelletje.

PRIJSSPEL = 24.95
KORTING = 0.4

def berekening(aantal):
    prijs = (PRIJSSPEL - PRIJSSPEL * KORTING) * aantal
    verzendKosten = (aantal - 1) * 0.25 + 1
    return prijs + verzendKosten

print(berekening(60))