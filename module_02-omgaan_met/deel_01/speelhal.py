# speelhal

aantalpersonen = 3

ticket = 7.45
ticket = float(ticket)

gameseat = 0.37
gameseat = float(gameseat)
aantalminuten = 5
keerminuten = 9

hoelang = aantalminuten * keerminuten
betalen = (aantalpersonen * ticket) + (keerminuten * gameseat)

print("Dit geweldige dagje-uit met", aantalpersonen, "mensen in de Speelhal met", hoelang, "minuten VR kost je maar", betalen, "euro")