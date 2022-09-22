import time
import sys

def delay_print1 (s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

delay_print1("Wat is je naam?")
name = input().strip()
print(f"""Welkom bij Prison Break! {name}
Je had een bank beroofd op 1 mei 2019 met 50 miljoen euro aan goud. 2 weken later werd je opgepakt door de politie, omdat je niet goed had verstopt.
Nu zit je in een van de meest beveiligde gevangenis van de wereld genaamd "ADX Florence" een van de meest beruchte gevangenis. Je kreeg 25 jaar straf in de gevangenis.
6 maanden later heb je een eigen bende gevormd genaamd {name}'s Gang en ben je van plan om te ontsnappen.
Nu op 15 november heb je je hele bende bij elkaar en nu moet je een keuze maken van hoe je moet ontsnappen.
""") # Intro

time.sleep(2) # 2 seconden delay

print("""Please wait...
""")

time.sleep(1)

print("Je bende heeft in totaal 5 mensen inclusief jij. Ze heten Vincent, Farhan, Oscar en Jez") # de gang zelf

escape = input("""Kies een van de manieren van ontsnappen: 
1. Tunnel graven
2. Prison shootout
Type een van de nummers in.
""") # Escape keuzes

if escape == "1": # Als je tunnel graven koos
    print("Op 16 november 2019 zijn alle bendeleden verzameld om te ontsnappen.")
    time.sleep(4) 
    print(f"{name}: 'Hey Farhan komen de bewakers?'")
    time.sleep(4)
    print("Farhan: 'Nee man, maar ze zijn nu te alert om te ontsnappen en er lopen teveel rond.'")
    time.sleep(5)
    print("""FLASHBACK 1 MAAND GELEDEN
    """)
    time.sleep(2)
    print("""*ALARM LOCKDOWN* *SIRENE GELUID*
    """)
    time.sleep(2)
    print("Random Prisoner: 'HEY *Random Prisoner 2* HEB JE ZE?'")
    time.sleep(3)
    print("Random Prisoner 2: 'NEE MAN ZE ZIJN MET TEVEEL'")
    time.sleep(3)
    print("*SHOTS FIRED*")
    time.sleep(2)
    print("Snap back to reality!")
    time.sleep(4)
    print("Vincent: 'De gevangene die wouden ontsnappen zijn door de bewakers allemaal dood geschoten.'")
    time.sleep(4)
    print("Oscar: 'We hebben een keuze om te wachten totdat ze wat minder alert zijn of we gaan nu!'")
    time.sleep(3)
    keuze1 = input("""Kies nu de optie om te wachten of niet. Type de nummer in
    1. Doorgaan
    2. Wachten
    """)
    if keuze1 == "1": # doodgaan
        print("Je hebt gekozen om door te gaan")
        time.sleep(3)
        print(f"""Je hebt de tunnel eindelijk gegraven, maar toen je bijna bij het einde was was de tunnel ingestort. Door de ingestorte tunnel gingen 
        {name}, Farhan en Jez levend begraven. De rest werden snel opgepakt door de bewakers""")
        time.sleep(7)
        print("Helaas heb je de verkeerde keuze genomen en ben je doodgegaan. Probeer het opnieuw!")
    if keuze1 == "2": # wachten
        print("Je hebt gekozen om te wachten")
        time.sleep(3)
        print("Het is nu 23 januari 2020")
        time.sleep(3)
        print(f"{name}: 'Het is nu eindelijk tijd om te ontsnappen!'")
        time.sleep(3)
        print(f"{name}: 'Vincent en Farhan staan op uitkijk en leidt ze af als de bewakers komen! De rest komen mee om de tunnel verder te graven.'")
        time.sleep(5)
        print("""Na 1 uur graven ben je eindelijk klaar met de tunnel, maar nu is de vraag ga jij Vincent en Farhan achterlaten om zelf met de andere te ontsnappen?
        Of wacht je tot morgen dat je met z'n allen gaat maar er is risico dat de tunnel ontdekt wordt...""")
        time.sleep(8)
        keuze2 = input("""Ga je tot morgen wachten of laat je ze in de steek? Type de nummer in
        1. Wachten
        2. In de steek laten
        """)
    if keuze2 == "1": # wachten 
        print("Je hebt gekozen om te wachten tot morgen. *+10 risico*")
        time.sleep(3)
        print("Terwijl je aan het slapen bent hoor je opeens geluiden buiten je cell...")
        time.sleep(5)
        print("ZE CHECKEN ELKE CELL! NU HEB JE DE KEUZE OM BETRAPT TE WORDEN OF NU ONTSNAPPEN ZONDER JE BENDE!")
        time.sleep(7)
        prisoncheck = input("""Laat je je cell check door de bewakers of ontsnap je nu door de tunnel? Type de nummer in.
        1. Ontsnap
        2. Wacht
        """)
    if prisoncheck == "1":
        print("""Terwijl je door de tunnel was aan het ontsnappen waren de bewakers al bij je cell. Ze waren sneller dan dat je dacht
        Toen je uit de tunnel was waren ze al op alert dat je weg was. De snipers zagen je en schoten je dood...""")
        time.sleep(10)
        print("Helaas heb je de verkeerde keuze genomen en ben je doodgegaan. Probeer het opnieuw!")
    if prisoncheck == "2":
        print("Je hebt gekozen om te wachten...")
        time.sleep(3)
        print("Jij bent nu aan de beurt...")
        time.sleep(5)
        print("Ze jouw cell aan het doorzoeken...")
        time.sleep(1)
        print("...")
        time.sleep(7)
        print("Helaas hebben ze de tunnel gevonden... Probeer het opnieuw!")
    if keuze2 == "2":
        print("Je hebt gekozen om je kameraden in de steek te laten")
        time.sleep(1)
        print("...")
        time.sleep(4)
        print("Toen jullie eindelijk vrij waren hadden Oscar en Jez achtergebleven om te wachten voor Vincent en Farhan.")
        time.sleep(4)
        keuze3 = input("""Nu heb je de keuze om te wachten of alleen verder te gaan. Type het getal in.
        1. Wachten
        2. Verder gaan
        """)
        if keuze3 == "1":
            print("Je hebt gekozen om te wachten.")
            time.sleep(3)
            print("Helaas was dat de foute keuze geweest. Na een tijdje hadden de bewakers je gespot.")
            time.sleep(3)
            print("Jullie probeerden om weg te rennen, maar het lukte niet. Uiteindelijk waren jullie alle drie doodgeschoten.")
            time.sleep(4)
            print("Helaas heb je de verkeerde keuze genomen en ben je doodgegaan. Probeer het opnieuw!")
        if keuze3 == "2":
            print("Je hebt gekozen om alleen verder te gaan")
            time.sleep(2)
            print("...")
            time.sleep(4)
            print("Gefeliciteerd je bent ontsnapt!")
            time.sleep(3)
            print("Helaas waren de rest van je bende opgepakt.")
            time.sleep(3)
            print("""THE END
            """)

if escape == "2": # gekozen voor prison shootout
    print("Je hebt gekozen om de harde manier te nemen.")
    time.sleep(3)
    print(f"""{name}: 'Hey Oscar heb je de wapens uitgedeeld?'""")
    time.sleep(3)
    print("Oscar: 'Ja man bijna iedereen heeft nu een wapen.'")
    time.sleep(3)
    keuze4 = input("""Nu heb je de keuze om nu te rellen of om te wachten. Type het nummer in.
    1. Verder gaan
    2. Wachten
    """)
    if keuze4 == "1":
        print("Je hebt gekozen om verder te gaan.")
        time.sleep(3)
        print(f"""{name}: 'Oke mannen de tijd is aangebroken!' """)
        time.sleep(3)
        wapen = input("""Jij als de leider van de rebellen kan kiezen welke uitrusting je kiest. Type het nummer in.
        NOTE: Het uitrusting dat jij kiest kan ervoor zorgen voor latere complicaties!
        1. AK-47 en RPG
        2. M4A1 en C4
        """)
        print("Nadat je je uitrusting had uitgekozen ging jij als eerste een bewaker neerschieten.")
        time.sleep(4)
        print(f"""{name}: 'KOM OP MANNEN HET IS TIJD OM ONZE VRIJHEID TERUG TE NEMEN!'""")
        time.sleep(5)
        print("De uitgangen werden als snel gesloten door de bewakers.")
        time.sleep(3)
        print("Farhan: 'Het is tijd!'")
        time.sleep(2)
        print("Farhan drukte op een knop en op meerdere plekken gingen bommen af ook de afgesloten uitgangen gingen kapot.")
        time.sleep(4)
        print("")

    if keuze4 == "2":
        print("Je hebt gekozen om te wachten...")
        time.sleep(3)
        print("Misschien was dat niet zo'n slimme keuze geweest.")
        time.sleep(4)
        print("Een van de mensen hadden jou uitverkocht aan de bewakers.")
        time.sleep(4)
        print("Nu checken ze elke cell voor wapens...")
        time.sleep(4)
        print("Helaas ben je betrapt door de bewakers. Probeer het opnieuw!")
