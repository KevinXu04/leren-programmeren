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
    if choice in("a", "b", "c", "d"):
        firstRound = False
        if choice == "a":
            print("Getallen optellen. \n")
            if nr1 == False:
                nr1 = True
                n1 = float(input("Welk getal? \n"))
            if nr2 == False:
                nr2 = True
                n2 = float(input(f"Welk getal optellen bij {n1}? \n"))
            antwoord = addition(n1, n2)
            print(f"{n1} + {n2} = {antwoord}")
            print("-------------------------")
        elif choice == "b":
            print("Getallen aftrekken. \n")
            if nr1 == False:
                nr1 = True
                n1 = float(input("Welk getal? \n"))
            if nr2 == False:
                nr2 = True
                n2 = float(input(f"Welk getal aftrekken bij {n1}? \n"))
            antwoord = subtraction(n1, n2)
            print(f"{n1} - {n2} = {antwoord}")
            print("-------------------------")
        elif choice == "c":
            print("Getallen vermenigvuldigen. \n")
            if nr1 == False:
                nr1 = True
                n1 = float(input("Welk getal? \n"))
            if nr2 == False:
                nr2 = True
                n2 = float(input(f"{n1} door welk getal vermenigvuldigen? \n"))
            antwoord = multiplication(n1, n2)
            print(f"{n1} x {n2} = {antwoord}")
            print("-------------------------")
        elif choice == "d":
            print("Getallen delen. \n")
            if nr1 == False:
                nr1 = True
                n1 = float(input("Welk getal? \n"))
            if nr2 == False:
                nr2 = True
                while True:
                    n2 = float(input(f"{n1} door welk getal delen? \n"))
                    if n2 == 0:
                        print("Kan niet delen met 0. \n")
                    else:
                        break
            antwoord = division(n1, n2)
            print(f"{n1} : {n2} = {antwoord}")
            print("-------------------------")
            print(n1)
    elif choice in("e", "f"):
        firstRound = False
        n2 = 1
        if choice == "e":
            print("Getallen ophogen. \n")
            if nr1 == False:
                nr1 = True
                n1 = float(input("Welk getal? \n"))
            antwoord = addition(n1, n2) 
            print(f"{n1} + {n2} = {antwoord}")
            print("-------------------------")
        elif choice == "f":
            print("Getallen verlagen. \n")
            if nr1 == False:
                nr1 = True
                n1 = float(input("Welk getal? \n"))
            antwoord = subtraction(n1, n2) 
            print(f"{n1} - {n2} = {antwoord}")
            print("-------------------------")
    elif choice in("g", "h"):
        firstRound = False
        n2 = 2
        if choice == "g":
            print("Getallen verdubbelen. \n")
            if nr1 == False:
                nr1 = True
                n1 = float(input("Welk getal? \n"))
            antwoord = multiplication(n1, n2) 
            print(f"{n1} x {n2} = {antwoord}")
            print("-------------------------")
        elif choice == "h":
            print("Getallen halveren. \n")
            if nr1 == False:
                nr1 = True
                n1 = float(input("Welk getal? \n"))
            antwoord = division(n1, n2) 
            print(f"{n1} : {n2} = {antwoord}")
            print("-------------------------")
    elif choice == "i" and firstRound == False:
        print("Einde berekening. \n")
        break
    else:
        print("Dat is geen geldig antwoord! \n")
