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
    return keuze

def smaakEnTopping(aantal, lst, tekst):
    keuzeBoolean = True
    
    for index in range(aantal):
        while keuzeBoolean:
            keuze = input(tekst).lower()
            if keuze == 'a':
                keuze = lst[0]['name']
                keuzeBoolean = False
            elif keuze == 'b':
                keuze = lst[1]['name']
                keuzeBoolean = False
            elif keuze == 'c':
                keuze = lst[2]['name']
                keuzeBoolean = False
            elif keuze == 'd':
                keuze = lst[3]['name']
                keuzeBoolean = False
            else:
                print("Sorry dat snap ik niet...")

            for item in lst:
                if keuze == item['name']:
                    item['aantal'] += 1
            
        keuzeBoolean = True
    return lst
        

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

def bolletjesEnKeuzeBerekening(aantal, keuze, lst):
    lst[0]['aantal'] += aantal

    for item in lst:
        if keuze == item['name']:
            item['aantal'] += 1

    return lst

def bon(lst, smaakLst, toppings):
    totaalPrijs = 0
    totaalPrijsToppings = 0
    lst.extend(smaakLst)

    print('--------["Papi Gelato"]--------')
    for index in lst:
        if index['aantal']:
            print(f"{index['name']} {index['aantal']} x € {'%.2f' % (index['prijs'])} = € {'%.2f' % (index['aantal'] * index['prijs'])}")
        totaalPrijs += index['aantal'] * index['prijs']

    # if lst[1]['aantal'] > 0:
    #     toppings[3]['prijs'] = 0.6
    #     lst[1]['aantal'] = 0
    #     totaalPrijsToppings += toppings[3]['prijs'] * toppings[3]['aantal']
    # if lst[2]['aantal'] > 0:
    #     toppings[3]['prijs'] = 0.9
    #     lst[2]['aantal'] = 0
    #     totaalPrijsToppings += toppings[3]['prijs'] * toppings[3]['aantal']


    if lst[2]['aantal'] > 0:
        toppings[3]['prijs'] = 0.9
    elif lst[3]['aantal'] > 0:
        toppings[3]['prijs'] = 0.6

    
    for item in toppings:   
        if item['aantal']: 
            totaalPrijsToppings =+ item['aantal'] * item['prijs']

    totaalPrijs += totaalPrijsToppings
    
    if totaalPrijsToppings:
        print(f"topping               € {'%.2f' % totaalPrijsToppings}\n")
    print("-------------------------------")
    print(f"totaal                 € {'%.2f' % totaalPrijs}\n")
    print("Bedankt en tot ziens! ")