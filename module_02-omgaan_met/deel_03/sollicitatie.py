print("Vacature: Circusdirecteur voor Circus HotelDeBotel")
naam = input("Wat is uw naam?")
while True: 
    geslacht = input("Bent u een man of een vrouw?")
    if geslacht == "man":
        ervaringMan = input("Met welke van deze drie heeft u ervaring mee: dieren-dressuur, jongleren of acrobatiek")
        if ervaringMan == "dieren-dressuur":
            jaar = int(input("Hoeveel jaar praktijkervaring heeft u?"))
            if jaar > 4:
                diploma = input("Bent u in bezit van een MBO-4 diploma?")
                if diploma == "ja":
                    rijbewijs = input("Bent u in bezit van een vrachtwagen rijbewijs?")
                    if rijbewijs == "ja":
                        hogehoed = input("Bent u in bezit van een hoge hoed?")
                        if hogehoed == "ja":
                            snor = int(input("Hoelang is uw snor"))
                            if snor > 10:
                                lengte = int(input("Hoelang bent u? (in cm)"))
                                if lengte > 150:
                                    gewicht = int(input("Hoe zwaar bent u? (in kg)"))
                                    if gewicht > 90:
                                        cert = input("Heeft u de certificaat 'Overleven met gevaarlijk personeel'?")
                                        if cert == "ja":
                                            print("Proficiat! U komt in aanmerking voor een sollicitatiegesprek.")
                                        elif cert == "nee":
                                            print("Helaas voldoet u niet aan onze strenge eisen.")
                                    elif gewicht < 90:
                                        cert = input("Heeft u de certificaat 'Overleven met gevaarlijk personeel'?")
                                        if cert == "ja":
                                            print("Helaas voldoet u niet aan onze strenge eisen.")
                                        elif cert == "nee":
                                            print("Helaas voldoet u niet aan onze strenge eisen.")
                                elif lengte < 150:
                                    gewicht = int(input("Hoe zwaar bent u? (in kg)"))
                                    if gewicht > 90:
                                        cert = input("Heeft u de certificaat 'Overleven met gevaarlijk personeel'?")
                                        if cert == "ja":
                                            print("Helaas voldoet u niet aan onze strenge eisen.")
                                        elif cert == "nee":
                                            print("Helaas voldoet u niet aan onze strenge eisen.")
                                    elif gewicht < 90:
                                        cert = input("Heeft u de certificaat 'Overleven met gevaarlijk personeel'?")
                                        if cert == "ja":
                                            print("Helaas voldoet u niet aan onze strenge eisen.")
                                        elif cert == "nee":
                                            print("Helaas voldoet u niet aan onze strenge eisen.")
                            elif snor < 10:
                                lengte = int(input("Hoelang bent u? (in cm)"))
                                if lengte > 150:
                                    gewicht = int(input("Hoe zwaar bent u? (in kg)"))
                                    if gewicht > 90:
                                        cert = input("Heeft u de certificaat 'Overleven met gevaarlijk personeel'?")
                                        if cert == "ja":
                                            print("Proficiat! U komt in aanmerking voor een sollicitatiegesprek.")
                                        elif cert == "nee":
                                            print("Helaas voldoet u niet aan onze strenge eisen.")
                                    elif gewicht < 90:
                                        cert = input("Heeft u de certificaat 'Overleven met gevaarlijk personeel'?")
                                        if cert == "ja":
                                            print("Helaas voldoet u niet aan onze strenge eisen.")
                                        elif cert == "nee":
                                            print("Helaas voldoet u niet aan onze strenge eisen.")
                                elif lengte < 150:
                                    gewicht = int(input("Hoe zwaar bent u? (in kg)"))
                                    if gewicht > 90:
                                        cert = input("Helaas voldoet u niet aan onze strenge eisen.")
                                        if cert == "ja":
                                            print("Helaas voldoet u niet aan onze strenge eisen.")
                                        elif cert == "nee":
                                            print("Helaas voldoet u niet aan onze strenge eisen.")
                                    elif gewicht < 90:
                                        cert = input("Heeft u de certificaat 'Overleven met gevaarlijk personeel'?")
                                        if cert == "ja":
                                            print("Helaas voldoet u niet aan onze strenge eisen.")
                                        elif cert == "nee":
                                            print("Helaas voldoet u niet aan onze strenge eisen.")

