def aantalBolletjes(aantal, keuzeBoolean):
    if aantal >= 1 and aantal <= 3:
        while keuzeBoolean:
            keuze = input(f"Wil u deze {aantal} in een hoorntje of een bakje? ")
            if keuze in ("hoorntje", "bakje"):
                keuzeBoolean = False
            else:
                print("Sorry die ken ik niet...")
    elif aantal >= 4 and aantal <= 8:
        print(f"Dan krijgt u van mij een bakje met {aantal} bolletjes ")
        keuze = "bakje"

    elif aantal > 8:
        print("Sorry, zulke grote bakken hebben we niet ")

    
    print(f"Hier is uw {keuze} met {aantal} bolletje(s) ")

    return aantal, keuzeBoolean

def meerBestellen(nogEen, eersteKeer, keuzeBoolean):
    while True:
        meer = input("Wilt u nog meer bestellen? ")
        if meer == "y":
            eersteKeer = False
            keuzeBoolean = True
            return nogEen, eersteKeer, keuzeBoolean
        elif meer == "n":
            print("Bedankt en tot ziens! ")
            nogEen = False
            return nogEen, eersteKeer, keuzeBoolean
        else:
            print("Sorry dat snap ik niet")

