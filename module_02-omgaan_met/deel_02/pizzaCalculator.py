# Kevin Xiu
# Opdracht: Pizza calculator


afmeting = input('Kies de grootte: small, medium, large')   # Vraagt welke grootte pizza 

if afmeting == "small": # Als het hij small kiest voert hij deze code
    aantal1 = int(input("Hoeveel pizza's wilt u?")) # Hier vraagt hij hoeveel pizza's de persoon wilt
    prijs1 = 6.99
    totaalprijs1 = prijs1 * aantal1 # Hier berekent hij hoeveel het kost met het aantal pizza's en de prijs
    print(f""""
    BON
    -------------------------------------
    {aantal1} Small pizza's       5x {prijs1},- €
    
    -------------------------------------
    Totaal prijs:           {totaalprijs1},- €
    """)    # Hier print hij de bon uit met wat hij bestelt heeft en de totaal prijs

if afmeting == "medium": # Als het hij medium kiest voert hij deze code uit
    aantal2 = int(input("Hoeveel pizza's wilt u?"))
    prijs2 = 8.99
    totaalprijs2 = prijs2 * aantal2
    print(f""""
    BON
    -------------------------------------
    {aantal2} Medium pizza's       5x {prijs2},- €
    
    -------------------------------------
    Totaal prijs:            {totaalprijs2},- €
    """)
    
if afmeting == "large": # Als het hij large kiest voert hij deze code uit
    aantal3 = int(input("Hoeveel pizza's wilt u?"))
    prijs3 = 10.99
    totaalprijs3 = prijs3 * aantal3
    print(f""""
    BON
    -------------------------------------
    {aantal3} Large pizza's       5x {prijs3},- €
    
    -------------------------------------
    Totaal prijs:            {totaalprijs3},- €
    """)

else:
    print("U heeft niet de juiste grootte gekozen. Probeer het opnieuw.")