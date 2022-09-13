print("Vacature: Circusdirecteur voor Circus HotelDeBotel")
score = 0
name = input("Wat is uw naam?")
geslacht = input("Wat is uw geslacht? (Man/Vrouw)")

ervaring = input("Met welke van de drie heeft u praktijkervaring? Kies uit dieren-dressuur, jongleren of acrobatiek.")

if ervaring in ("dieren-dressuur","dieren dressuur"):
    dierUur = int(input("Hoeveel jaar prijktijkervaring heeft uw met dieren-dressuur?"))
    if dierUur > 4:
        score = score + 1
elif ervaring in ("jongleren"):
    jongUur = int(input("Hoeveel jaar prijktijkervaring heeft uw met jongleren?"))
    if jongUur > 5:
        score = score + 1
elif ervaring in ("acrobatiek"):
    acroUur = int(input("Hoeveel jaar prijktijkervaring heeft uw met acrobatiek?"))
    if acroUur > 3:
        score = score + 1

diploma = input("Bent u in bezit van een MBO-4 diploma?")
if diploma in ("ja","Ja"):
    score = score + 1

rijbewijs = input("Bent u in bezit van een vrachtwagen rijbewijs?")
if rijbewijs in ("ja","Ja"):
    score = score + 1

if geslacht in ("man","Man"):
    snor = int(input("Hoe lang is uw snor?"))
    if snor > 10:
        score = score + 1
    elif snor == 10:
        score = score + 1

if geslacht in ("vrouw","Vrouw"):
    haar = int(input("Hoe lang is uw krulhaar?"))
    if haar > 20:
        score = score + 1
    elif haar == 20:
        score = score + 1

lengte = int(input("Hoe lang bent u?"))
if lengte > 150:
    score = score + 1

gewicht = int(input("Hoe zwaar bent u?"))
if gewicht > 90:
    score = score + 1

cert = input("Heeft u de certificaat 'Overleven met gevaarlijk personeel'?")

if score > 6:
    print("Proficiat! U komt in aanmerking voor een sollicitatiegesprek.")
elif score == 6:
    print("Proficiat! U komt in aanmerking voor een sollicitatiegesprek.")
elif score < 6:
    print("Helaas voldoet u niet aan onze strenge eisen.")