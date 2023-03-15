def aantalBolletjes():
    while True:
        try:
            aantal = int(input("Hoeveel bolletjes wilt u? "))
            if aantal > 8:
                print("Sorry, zulke grote bakken hebben we niet ")
            else:
                return aantal
        except:
            print("Sorry dat snap ik niet...")

def bakjeOfHoorntje(aantal):
    keuzeBoolean = True
    if aantal >= 1 and aantal <= 3:
        while keuzeBoolean:
            keuze = input(f"Wil u deze {aantal} bolletje(s) in een hoorntje of een bakje? ").lower()
            if keuze in ("hoorntje", "bakje"):
                keuzeBoolean = False
            else:
                print("Sorry die ken ik niet...")
    elif aantal >= 4 and aantal <= 8:
        print(f"Dan krijgt u van mij een bakje met {aantal} bolletjes ")
        keuze = "bakje"

    print(f"Hier is uw {keuze} met {aantal} bolletje(s) ")
    return aantal, keuze

def smaakKiezen(aantal):
    keuzeBoolean = True
    smaakLst = [{'name': 'aardbei', 'aantal': 0, 'prijs': 1.10},
                 {'name': 'chocolade', 'aantal': 0, 'prijs': 1.10},
                 {'name': 'munt', 'aantal': 0, 'prijs': 1.10},
                 {'name': 'vanille', 'aantal': 0, 'prijs': 1.10}]
    
    for index in range(aantal):
        while keuzeBoolean:
            smaakKeuze = input(f"Welke smaak wilt u voor bolletje nummer {index+1}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?").lower()
            if smaakKeuze == "a":
                smaakLst[0]['aantal'] += 1
                keuzeBoolean = False
            elif smaakKeuze == "c":
                smaakLst[1]['aantal'] += 1
                keuzeBoolean = False
            elif smaakKeuze == "m":
                smaakLst[2]['aantal'] += 1 
                keuzeBoolean = False
            elif smaakKeuze == "v":
                smaakLst[3]['aantal'] += 1 
                keuzeBoolean = False
            else:
                print("Sorry dat snap ik niet...")
        keuzeBoolean = True
        
    return smaakLst

def meerBestellen(nogEen):
    while True:
        meer = input("Wilt u nog meer bestellen? ")
        if meer == "y":
            return nogEen
        elif meer == "n":
            nogEen = False
            return nogEen
        else:
            print("Sorry dat snap ik niet")

def berekening(aantal, keuze):
    lst = [{'name': 'bolletje', 'aantal': 0, 'prijs': 1.10},
            {'name': 'hoorntje', 'aantal': 0, 'prijs': 1.25},
            {'name': 'bakje', 'aantal': 0, 'prijs': 0.75}]

    lst[0]['aantal'] += aantal

    for item in lst:
        if keuze == item['name']:
            item['aantal'] += 1

    return lst

def bon(lst, smaakLst):
    totaalPrijs = 0
    lst.extend(smaakLst)

    print('--------["Papi Gelato"]--------')
    for index in lst:
        if index['aantal']:
            print(f"{index['name']} {index['aantal']} x € {'%.2f' % (index['prijs'])} = € {'%.2f' % (index['aantal'] * index['prijs'])}")
        totaalPrijs += index['aantal'] * index['prijs']
    print("-------------------------------")
    print(f"Totaal                 € {'%.2f' % totaalPrijs}\n")
    print("Bedankt en tot ziens! ")