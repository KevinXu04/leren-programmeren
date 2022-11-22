import random
values = ['2','3','4','5','6','7','8','9','10','Boer','Vrouw','Heer','Aas']
suites = ['Harten', 'Klaver', 'Schoppen', 'Ruiten']
rood = ('Rode', 'Joker')
zwart = ('Zwarte', 'Joker')
deck = [[s, v] for s in suites for v in values]
deck.append(rood and zwart)
random.shuffle(deck)
y= 0
z = 0
for x in range(7):
    z += 1
    print(f"Kaart {z}:", deck[y])
    y += 1

print("Deck (47 kaarten):", deck[7:54])