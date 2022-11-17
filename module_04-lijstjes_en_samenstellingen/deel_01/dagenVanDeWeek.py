alleDagen = ("Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag")
print("Alle dagen in de week zijn:", alleDagen)
print("De werkdagen zijn:", alleDagen[0:5])
print("De weekenddagen zijn:", alleDagen[5:7])

x = reversed(alleDagen)
x = tuple(x)

print("Alle dagen van de week in omgekeerde volgorde zijn:", x)
print("De werkdagen in omgekeerde volgorde zijn:", x[2:7])
print("De weekenddagen in omgekeerde volgorde zijn:", x[0:2])
