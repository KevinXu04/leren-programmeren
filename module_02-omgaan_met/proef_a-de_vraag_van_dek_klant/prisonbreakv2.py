import time
import sys

def delay_print1 (s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.001)

delay_print1("Wat is je naam? ")
name = input().strip()
delay_print1(f"""Welkom bij Prison Break! {name}!
Je had een bank beroofd op 1 mei 2019 met 50 miljoen euro aan goud. 2 weken later werd je opgepakt door de politie, omdat je niet goed had verstopt.
Nu zit je in een van de meest beveiligde gevangenis van de wereld genaamd "ADX Florence" een van de meest beruchte gevangenis. Je kreeg 25 jaar straf in de gevangenis.
6 maanden later heb je een eigen bende gevormd genaamd {name}'s Gang en ben je van plan om te ontsnappen.
Nu op 15 november heb je je hele bende bij elkaar en nu moet je een keuze maken van hoe je moet ontsnappen.
""") # Intro

time.sleep(1) # 2 seconden delay

delay_print1("""
Please wait...
""")

time.sleep(2)

delay_print1("""
Je bende heeft in totaal 5 mensen inclusief jij. Ze heten Vincent, Farhan, Oscar en Jez
""") # de gang zelf

delay_print1("""
Kies een van de manieren van ontsnappen: 
    1. Tunnel graven
    2. Prison shootout
Type een van de nummers in.
""") # Escape keuzes

escape = input().strip()

if escape == "1": # Als je tunnel graven koos
    delay_print1(f"""
Op 16 november 2019 zijn alle bendeleden verzameld om te ontsnappen.
{name}: 'Hey Farhan komen de bewakers?'
Farhan: 'Nee man, maar ze zijn nu te alert om te ontsnappen en er lopen teveel rond.'

FLASHBACK 1 MAAND GELEDEN

*ALARM LOCKDOWN* *SIRENE GELUID*

Random Prisoner: 'HEY *Random Prisoner 2* HEB JE ZE?'
Random Prisoner 2: 'NEE MAN ZE ZIJN MET TEVEEL!'

*SHOTS FIRED*

Snap back to reality!

Vincent: 'De gevangene die wouden ontsnappen zijn door de bewakers allemaal dood geschoten.'
Oscar: 'We hebben een keuze om te wachten totdat ze wat minder alert zijn of we gaan nu!'""")
    delay_print1("""
Kies nu de optie om te wachten of niet.
    1. Doorgaan
    2. Wachten
Type een van de nummers in.
""")

    keuze1 = input().strip()
    if keuze1 == "1": # doodgaan
        delay_print1(f"""
Je hebt gekozen om door te gaan.
Je hebt de tunnel eindelijk gegraven, maar toen je bijna bij het einde was was de tunnel ingestort. 
Door de ingestorte tunnel gingen {name}, Farhan en Jez levend begraven. De rest werden snel opgepakt door de bewakers
Helaas heb je de verkeerde keuze genomen en ben je doodgegaan. Probeer het opnieuw!""")
        exit()

    if keuze1 == "2": # wachten
        delay_print1(f"""
Je hebt gekozen om te wachten
Het is nu 23 januari 2020
{name}: 'Het is nu eindelijk tijd om te ontsnappen!'
{name}: 'Vincent en Farhan staan op uitkijk en leidt ze af als de bewakers komen! De rest komen mee om de tunnel verder te graven.'
Na 1 uur graven ben je eindelijk klaar met de tunnel, maar nu is de vraag ga jij Vincent en Farhan achterlaten om zelf met de andere te ontsnappen?
Of wacht je tot morgen dat je met z'n allen gaat maar er is risico dat de tunnel ontdekt wordt...""")

        delay_print1("""
Ga je tot morgen wachten of laat je ze in de steek?
    1. Wachten
    2. In de steek laten
Type een van de nummers in.
""")
        keuze2 = input().strip()
    
    if keuze2 == "1": # wachten 
        delay_print1("Je hebt gekozen om te wachten tot morgen. *+10 risico*")
        delay_print1("Terwijl je aan het slapen bent hoor je opeens geluiden buiten je cell...")
        delay_print1("ZE CHECKEN ELKE CELL! NU HEB JE DE KEUZE OM BETRAPT TE WORDEN OF NU ONTSNAPPEN ZONDER JE BENDE!")

        delay_print1("""
Laat je je cell check door de bewakers of ontsnap je nu door de tunnel?
    1. Ontsnap
    2. Wacht
Type een van de nummers in.
""")
        prisoncheck = input().strip()

    if prisoncheck == "1":
        delay_print1("""Terwijl je door de tunnel was aan het ontsnappen waren de bewakers al bij je cell. Ze waren sneller dan dat je dacht
        Toen je uit de tunnel was waren ze al op alert dat je weg was. De snipers zagen je en schoten je dood...""")
        time.sleep(10)
        delay_print1("Helaas heb je de verkeerde keuze genomen en ben je doodgegaan. Probeer het opnieuw!")
    if prisoncheck == "2":
        delay_print1("Je hebt gekozen om te wachten...")
        time.sleep(3)
        delay_print1("Jij bent nu aan de beurt...")
        time.sleep(5)
        delay_print1("Ze jouw cell aan het doorzoeken...")
        time.sleep(1)
        delay_print1("...")
        time.sleep(7)
        delay_print1("Helaas hebben ze de tunnel gevonden... Probeer het opnieuw!")
    if keuze2 == "2":
        delay_print1("Je hebt gekozen om je kameraden in de steek te laten")
        time.sleep(1)
        delay_print1("...")
        time.sleep(4)
        delay_print1("Toen jullie eindelijk vrij waren hadden Oscar en Jez achtergebleven om te wachten voor Vincent en Farhan.")
        time.sleep(4)
        keuze3 = input("""Nu heb je de keuze om te wachten of alleen verder te gaan. Type het getal in.
        1. Wachten
        2. Verder gaan
        """)
        if keuze3 == "1":
            delay_print1("Je hebt gekozen om te wachten.")
            time.sleep(3)
            delay_print1("Helaas was dat de foute keuze geweest. Na een tijdje hadden de bewakers je gespot.")
            time.sleep(3)
            delay_print1("Jullie probeerden om weg te rennen, maar het lukte niet. Uiteindelijk waren jullie alle drie doodgeschoten.")
            time.sleep(4)
            delay_print1("Helaas heb je de verkeerde keuze genomen en ben je doodgegaan. Probeer het opnieuw!")
        if keuze3 == "2":
            delay_print1("Je hebt gekozen om alleen verder te gaan")
            time.sleep(2)
            delay_print1("...")
            time.sleep(4)
            delay_print1("Gefeliciteerd je bent ontsnapt!")
            time.sleep(3)
            delay_print1("Helaas waren de rest van je bende opgepakt.")
            time.sleep(3)
            delay_print1("""THE END
            """)

if escape == "2": # gekozen voor prison shootout
    delay_print1("Je hebt gekozen om de harde manier te nemen.")
    time.sleep(3)
    delay_print1(f"""{name}: 'Hey Oscar heb je de wapens uitgedeeld?'""")
    time.sleep(3)
    delay_print1("Oscar: 'Ja man bijna iedereen heeft nu een wapen.'")
    time.sleep(3)
    keuze4 = input("""Nu heb je de keuze om nu te rellen of om te wachten. Type het nummer in.
    1. Verder gaan
    2. Wachten
    """)
    if keuze4 == "1":
        delay_print1("Je hebt gekozen om verder te gaan.")
        time.sleep(3)
        delay_print1(f"""{name}: 'Oke mannen de tijd is aangebroken!' """)
        time.sleep(3)
        wapen = input("""Jij als de leider van de rebellen kan kiezen welke uitrusting je kiest. Type het nummer in.
        NOTE: Het uitrusting dat jij kiest kan ervoor zorgen voor latere complicaties!
        1. AK-47 en RPG
        2. M4A1 en C4
        """)
        delay_print1("Nadat je je uitrusting had uitgekozen ging jij als eerste een bewaker neerschieten.")
        time.sleep(4)
        delay_print1(f"""{name}: 'KOM OP MANNEN HET IS TIJD OM ONZE VRIJHEID TERUG TE NEMEN!'""")
        time.sleep(5)
        delay_print1("De uitgangen werden als snel gesloten door de bewakers.")
        time.sleep(3)
        delay_print1("Farhan: 'Het is tijd!'")
        time.sleep(2)
        delay_print1("Farhan drukte op een knop en op meerdere plekken gingen bommen af ook de afgesloten uitgangen gingen kapot.")
        time.sleep(4)
        delay_print1("")

    if keuze4 == "2":
        delay_print1("Je hebt gekozen om te wachten...")
        time.sleep(3)
        delay_print1("Misschien was dat niet zo'n slimme keuze geweest.")
        time.sleep(4)
        delay_print1("Een van de mensen hadden jou uitverkocht aan de bewakers.")
        time.sleep(4)
        delay_print1("Nu checken ze elke cell voor wapens...")
        time.sleep(4)
        delay_print1("Helaas ben je betrapt door de bewakers. Probeer het opnieuw!")
