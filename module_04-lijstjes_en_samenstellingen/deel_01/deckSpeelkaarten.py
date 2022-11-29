import random

kleuren = ('2','3','4','5','6','7','8','9','10','Boer','Vrouw','Heer','Aas')
kaarten = ('Harten', 'Klaver', 'Schoppen', 'Ruiten')
deck = [f'{x} {y}' for x in kaarten for y in kleuren]
deck.append("Joker1")
deck.append("Joker2")
random.shuffle(deck)
p = 0
o = 0
for x in range(7):
    p += 1
    print(f"Kaart {p}:", deck[o])
    o += 1

print("Deck (47 kaarten):", deck[7:54])