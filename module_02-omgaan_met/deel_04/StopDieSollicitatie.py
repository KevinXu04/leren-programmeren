print("Vacature: Circusdirecteur voor Circus HotelDeBotel")
score = 0
name = input("Wat is uw naam? ")
if name in("arda","Arda"):
    raise NameError("Sorry we nemen geen buitenlanders aan.")
geslacht = input("Wat is uw geslacht? (Man/Vrouw) ")
if geslacht in("non-binary"):
    raise NameError("Sorry dat is geen geslacht")

ervaring = input("Met welke van de drie heeft u praktijkervaring? Kies uit dieren-dressuur, jongleren of acrobatiek. ")

if ervaring in ("dieren-dressuur","dieren dressuur"):
    dierUur = int(input("Hoeveel jaar praktijkervaring heeft uw met dieren-dressuur? "))
    diploma = input("Bent u in bezit van een MBO-4 diploma?")
    if (dierUur > 4 and diploma in ("ja","Ja")) :
        score = score + 1
elif ervaring in ("jongleren"):
    jongUur = int(input("Hoeveel jaar praktijkervaring heeft uw met jongleren? "))
    diploma = input("Bent u in bezit van een MBO-4 diploma?")
    if (jongUur > 5 and diploma in ("ja","Ja")):
        score = score + 1   
elif ervaring in ("acrobatiek"):
    acroUur = int(input("Hoeveel jaar praktijkervaring heeft uw met acrobatiek? "))
    diploma = input("Bent u in bezit van een MBO-4 diploma?")
    if (acroUur > 3 and diploma in ("ja","Ja")):
        score = score + 1

rijbewijs = input("Bent u in bezit van een vrachtwagen rijbewijs? ")
if rijbewijs in ("ja","Ja"):
    score = score + 1

try:
    if geslacht in ("man","Man"):
        snor = int(input("Hoe lang is uw snor? "))
        if snor >= 10:
            score = score + 1
        if snor < 10:
            raise NameError("Laat hem wat groeien.")
except:
    print("Beetje laten door groeien")

if geslacht in ("vrouw","Vrouw"):
    haar = int(input("Hoe lang is uw krulhaar? "))
    if haar >= 20:
        score = score + 1

lengte = int(input("Hoe lang bent u? "))
gewicht = int(input("Hoe zwaar bent u? "))
if (lengte > 150 and gewicht > 90):
    score = score + 1

cert = input("Heeft u de certificaat 'Overleven met gevaarlijk personeel'? ")

if score >= 4:
    print("Proficiat! U komt in aanmerking voor een sollicitatiegesprek.")
elif score < 4:
    print("Helaas voldoet u niet aan onze strenge eisen.")