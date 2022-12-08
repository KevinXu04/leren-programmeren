import random

kleuren = ('2','3','4','5','6','7','8','9','10','Boer','Vrouw','Heer','Aas', 'Timmerman')
kaarten = ('Harten', 'Klaver', 'Schoppen', 'Ruiten', 'Cirkel')
deck = [f'{x} {y}' for x in kaarten for y in kleuren]
deck.append("Joker1")
deck.append("Joker2")
random.shuffle(deck)

deckAantal = len(deck) - 7

p = 0
o = 0
for x in range(7):
    p += 1
    print(f"Kaart {p}:", deck[o])
    del deck[o]
    o += 1    
random.shuffle(deck)
print(f"Deck ({deckAantal} kaarten):", deck)
# Kaarten uit de deck halen en het aantal kaarten dat overblijft optellen