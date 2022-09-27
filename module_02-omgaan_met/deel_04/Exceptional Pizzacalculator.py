# Kevin Xiu
# Opdracht: Pizza calculator

afmeting = input('Kies de grootte: small, medium, large ')   # Vraagt welke grootte pizza 

while True:
    try:
        aantal = int(input("Hoeveel pizza's wilt u? ")) # Hier vraagt hij hoeveel pizza's de persoon wilt
        break
    except:
        print("Nee dat is niet juist. Voer een nummer in!")

if afmeting in("s","small","Small","S"):
    prijs = 6.99
if afmeting in("m","medium","Medium","M"):
    prijs = 8.99
if afmeting in("l","large","Large","L"):
    prijs = 10.99

totaalprijs = aantal * prijs

print(f"""
    BON
    -------------------------------------
    {aantal} {afmeting} pizza's       {aantal}x {prijs},- €
    
    -------------------------------------
    Totaal prijs:           {totaalprijs},- €
    """)    # Hier print hij de bon uit met wat hij bestelt heeft en de totaal prijs
