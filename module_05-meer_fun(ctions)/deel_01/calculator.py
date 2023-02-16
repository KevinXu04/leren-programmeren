def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

firstRound = True
nr1 = False
nr2 = False

while True:

    if firstRound == True:
        choice = input("Wat wilt u doen?\n A) getallen optellen\n B) getallen aftrekken\n C) getallen vermenigvuldigen\n D) getallen delen\n E) getal ophogen\n F) getal verlagen\n G) getal verdubbelen\n H) getal halveren? \n").lower()
    else:
        choice = input(f"Wat wilt u doen? met {antwoord}\n A) getallen optellen\n B) getallen aftrekken\n C) getallen vermenigvuldigen\n D) getallen delen\n E) getal ophogen\n F) getal verlagen\n G) getal verdubbelen\n H) getal halveren? \n I) niets \n").lower()
        n1 = antwoord
        nr2 = False

    if choice in ("a", "b"):
        if nr1 == False:
            n1 = float(input("Welk getal? \n"))
        if nr2 == False:
            n2 = float(input(f"Welk getal? \n"))

    if choice in ("c", "d"):
        if nr1 == False:
                n1 = float(input("Welk getal? \n"))
        if nr2 == False:
            while True:
                n2 = float(input(f"Welk getal? \n"))
                if n2 == 0:
                    print("Kan niet delen met 0. \n")
                else:
                    break

    if choice in ("e", "f", "g", "h"):
        n2 = 1
        if nr1 == False:
            nr1 = True
            n1 = float(input("Welk getal? \n"))
        if choice in ("g", "h"):
            n2 = 2

    if choice in("a", "b", "c", "d"):
        if choice == "a":
            antwoord = addition(n1, n2)
            print(f"{n1} + {n2} = {antwoord}")
            print("-------------------------")
        elif choice == "b":
            antwoord = subtraction(n1, n2)
            print(f"{n1} - {n2} = {antwoord}")
            print("-------------------------")
        elif choice == "c":
            antwoord = multiplication(n1, n2)
            print(f"{n1} x {n2} = {antwoord}")
            print("-------------------------")
        elif choice == "d":
            antwoord = division(n1, n2)
            print(f"{n1} : {n2} = {antwoord}")
            print("-------------------------")

    elif choice in("e", "f"):
        if choice == "e":
            antwoord = addition(n1, n2) 
            print(f"{n1} + {n2} = {antwoord}")
            print("-------------------------")
        elif choice == "f":
            antwoord = subtraction(n1, n2) 
            print(f"{n1} - {n2} = {antwoord}")
            print("-------------------------")
    
    elif choice in("g", "h"):
        if choice == "g":
            antwoord = multiplication(n1, n2) 
            print(f"{n1} x {n2} = {antwoord}")
            print("-------------------------")
        elif choice == "h":
            antwoord = division(n1, n2) 
            print(f"{n1} : {n2} = {antwoord}")
            print("-------------------------")

    elif choice == "i" and firstRound == False:
        print("Einde berekening. \n")
        break
    else:
        print("Dat is geen geldig antwoord! \n")
    
    firstRound = False
    nr1, nr2 = True, True