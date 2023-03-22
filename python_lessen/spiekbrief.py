# commentaar
# start met een hekje
########################################################
# datatypes
# string = woord of zin
########################################################
woord = 'Hallo' # mag ook met dubbele komma's
woord = "Hallo"
# met drie quotes krijg je een multiline string
lange_zin = """dit is een erg lange zin,
die verdeeld is over meerdere regels.""""

# int = geheel getal
x = 6
# float = kommagetal (let op punt ipv komma)
y = 6.5

########################################################
# built in functies bif's (ongeveer 70 in python)
########################################################
# input = stel een vraag en sla het antwoord op. Geef altijd een string terug.
antwoord = input('Hoe heet je?')

# print = stuurt een string naar de commandline
print('hallo', antwoord) # of
print('hallo' + antwoord) # of
print(f'hallo {antwoord}, leuk om kennis te maken!')

# int() zet om naar int
getal = int('6')
