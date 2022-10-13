# Grootte zwembad
lengte = 8
breedte = 3
diepte = 1.5

# Kosten uitgraven grond
zwembadInhoud = lengte * breedte * diepte
kostenUitgraven = 25
uitgravenPrijs = zwembadInhoud * kostenUitgraven

# Kosten afvoer grond
kostenAfvoerenGrond = 32.50
afvoerGrondPrijs = zwembadInhoud * kostenAfvoerenGrond

# Totaal kosten
totaalprijs = afvoerGrondPrijs + uitgravenPrijs



# Bon
print(f"""
Uitgraven:          {uitgravenPrijs}
Afvoeren grond:     {afvoerGrondPrijs}

Totaal prijs:       {totaalprijs}
""")