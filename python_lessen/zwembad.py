# Grootte zwembad
lengte = int(input("Wat is de lengte van het zwembad? "))
breedte = int(input("Wat is de breedte van het zwembad? "))
diepte = int(input("Wat is de diepte van het zwembad? "))

# Kosten uitgraven grond
zwembadInhoud = lengte * breedte * diepte
kostenUitgraven = 25
uitgravenPrijs = zwembadInhoud * kostenUitgraven

# Kosten afvoer grond
kostenAfvoerenGrond = 32.50
afvoerGrondPrijs = zwembadInhoud * kostenAfvoerenGrond

# Voorrijkosten
voorrijkostenVastePrijs = 250
voorrijkostenPerKM = 2.05
afstand = 60
kostenPerKM = 60 * 2.05
voorrijkosten = kostenPerKM + voorrijkostenVastePrijs

# Vierkante meter zwembad
zwembadVierkanteMeter = lengte * breedte

# Afwerken kosten
if zwembadInhoud < 20:
    afwerkenPrijsPer = 250
    meerprijsRood = 25
    meerprijsKeuzeKleur = 100
elif zwembadInhoud >= 20:
    afwerkenPrijsPer = 200
    meerprijsRood = 20
    meerprijsKeuzeKleur = 125
else:
    print("Error")
    exit()

# Totaal kosten
totaalprijs = afvoerGrondPrijs + uitgravenPrijs + voorrijkosten



# Bon
print(f"""
Uitgraven:          {uitgravenPrijs}
Afvoeren grond:     {afvoerGrondPrijs}
Voorrijkosten       {voorrijkosten}

Totaal prijs:       {totaalprijs}
""")