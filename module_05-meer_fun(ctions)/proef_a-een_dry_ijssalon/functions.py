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
            keuze = input(f"Wil u deze {aantal} bolletje(s) in een hoorntje of een bakje? ")
            if keuze in ("hoorntje", "bakje"):
                keuzeBoolean = False
            else:
                print("Sorry die ken ik niet...")
    elif aantal >= 4 and aantal <= 8:
        print(f"Dan krijgt u van mij een bakje met {aantal} bolletjes ")
        keuze = "bakje"

    print(f"Hier is uw {keuze} met {aantal} bolletje(s) ")
    return aantal

def meerBestellen(nogEen):
    while True:
        meer = input("Wilt u nog meer bestellen? ")
        if meer == "y":
            return nogEen
        elif meer == "n":
            print("Bedankt en tot ziens! ")
            nogEen = False
            return nogEen
        else:
            print("Sorry dat snap ik niet")

