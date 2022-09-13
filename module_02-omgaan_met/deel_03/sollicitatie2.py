print("Vacature: Circusdirecteur voor Circus HotelDeBotel")
naam = input("Wat is uw naam?")

# Geslacht
geslacht = input("Wat is uw geslacht? (man/vrouw)")
if geslacht == "man":
    ervaringMan = input("Met welke van de drie heeft u praktijkervaring? dieren-dressuur, jongleren of acrobatiek.")
elif geslacht == "vrouw":
    ervaringVrouw = input("Met welke van de drie heeft u praktijkervaring? dieren-dressuur, jongleren of acrobatiek.")

# Dieren-dressuur
if ervaringMan == "dieren-dressuur":
    dierMan = int(input("Hoeveel jaar praktijkervaring heeft u?"))
    if dierMan > 4:
        diploma = input("Bent u in bezit van een MBO-4 diploma?")
    elif dierMan < 4:
        diploma2 = input("Bent u in bezit van een MBO-4 diploma?")

# Jongleren
if ervaringMan == "jongleren":
    jongMan = int(input("Hoeveel jaar praktijkervaring heeft u?"))
    if jongMan > 5:
        diploma = input("Bent u in bezit van een MBO-4 diploma?")
    elif jongMan < 5:
        diploma2 = input("Bent u in bezit van een MBO-4 diploma?")

# Acrobatiek
if ervaringMan == "jongleren":
    acroMan = int(input("Hoeveel jaar praktijkervaring heeft u?"))
    if acroMan > 3:
        diploma = input("Bent u in bezit van een MBO-4 diploma?")
    elif jongMan < 3:
        diploma2 = input("Bent u in bezit van een MBO-4 diploma?")

# Diploma = ja, rijbewijs & hogehoed
if diploma == "ja":
    rijbewijs = input("Bent u in bezit van een vrachtwagen rijbewijs?")
    if rijbewijs == "ja":
        hogeHoedGoed = input("Bent u in bezit van een hoge hoed?")
    elif rijbewijs == "nee":
        hogeHoedFout = input("Bent u in bezit van een hoge hoed?")

# Diploma = nee, rijbewijs & hogehoed
if diploma2 == "nee":
    rijbewijs = input("Bent u in bezit van een vrachtwagen rijbewijs?")
    if rijbewijs == "ja":
        hogeHoedFout = input("Bent u in bezit van een hoge hoed?")
    elif rijbewijs == "nee":
        hogeHoedFout = input("Bent u in bezit van een hoge hoed?")

# HogeHoed = ja, 
