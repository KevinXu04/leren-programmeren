vraagBolletjes = True
keuzeBoolean = True
nogEen = True

while nogEen:
    while vraagBolletjes:
        aantalBolletjes = int(input("Hoeveel bolletjes wilt u? "))

        if aantalBolletjes >= 1 and aantalBolletjes <= 3:
            while keuzeBoolean:
                keuze = input(f"Wil u deze {aantalBolletjes} in een hoorntje of een bakje? ")
                if keuze in ("hoorntje", "bakje"):
                    keuzeBoolean = False
                    vraagBolletjes = False
                else:
                    print("Sorry die ken ik niet...")
        elif aantalBolletjes >= 4 and aantalBolletjes <= 8:
            print(f"Dan krijgt u van mij een bakje met {aantalBolletjes} bolletjes ")
            keuze = "bakje"
            vraagBolletjes = False
        elif aantalBolletjes > 8:
            print("Sorry, zulke grote bakken hebben we niet ")

    print(f"Hier is uw {keuze} met {aantalBolletjes} bolletje(s) ")

    meer = input("Wilt u nog meer bestellen? ")
    if meer == "y":
        vraagBolletjes = True
        continue
    elif meer == "n":
        print("Bedankt en tot ziens! ")
        nogEen = False
    else:
        print("Sorry dat snap ik niet")