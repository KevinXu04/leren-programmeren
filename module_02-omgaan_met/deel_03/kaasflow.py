kaas = input("Is de kaas geel?")
if kaas == "ja":
    gaten = input("Zitten er gaten in?")
    if gaten == "ja":
        duur = input("Is de kaas belachelijk duur?")
        if duur == "ja":
            print("Emmenthaler")
        else :
            print("Leerdammer")
    else :
        hard = input("Is de kaas hard als steen?")
        if hard == "ja":
            print("Parmigiano Reggiano")
        else :
            print("Goudse Kaas")
else :
    blauw = input("Heeft de kaas een blauwe schimmel?")
    if blauw == "ja":
        korst = input("Heeft de kaas een korst?")
        if korst == "ja":
            print("Blue de Rochbaron")
        else :
            print("Foume d'Ambert")
    else :
        korst = input("Heeft de kaas een korst?")
        if korst == "ja":
            print("Camembert")
        else :
            print("Mozzarella")