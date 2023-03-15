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

def bon(aantal, keuze, nogEen):
    totaalPrijs = 0
    lst = [{'name': 'bolletje', 'aantal': 0, 'prijs': 1.10},
            {'name': 'hoorntje', 'aantal': 0, 'prijs': 1.25},
            {'name': 'bakje', 'aantal': 0, 'prijs': 0.75}]

    lst[0]['aantal'] += aantal

    for item in lst:
        if keuze == item['name']:
            item['aantal'] += 1

    if nogEen == False:
        print('--------["Papi Gelato"]--------')
        for index in lst:
            if index['aantal']:
                print(f"{index['name']} {index['aantal']} x € {'%.2f' % (index['prijs'])} = € {'%.2f' % (index['aantal'] * index['prijs'])}")
            totaalPrijs += index['aantal'] * index['prijs']
        print("-------------------------------")
        print(f"Totaal                 {'%.2f' % totaalPrijs}\n")
        print("Bedankt en tot ziens! ")



    
