aantalpersonen = int(input('Hoeveel personen?'))

ticket = 7.45

gameseat = 0.37
aantalminuten = 5
keerminuten = 9

hoelang = aantalminuten * keerminuten
betalen = (aantalpersonen * ticket) + (keerminuten * gameseat)

print("Dit geweldige dagje-uit met", aantalpersonen, "mensen in de Speelhal met", hoelang, "minuten VR kost je maar", betalen, "euro")