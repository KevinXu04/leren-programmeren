getal = int(input("Van welk getal wilt u de tafel zien? \n"))

def tafel(cijfer):
    for x in range(1, 11):
        print(f"{x} x {cijfer} = {x*cijfer}")

tafel(getal)