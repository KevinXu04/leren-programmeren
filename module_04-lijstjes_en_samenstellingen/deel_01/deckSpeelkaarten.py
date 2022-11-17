import random
values = ['2','3','4','5','6','7','8','9','10','Boer','Vrouw','Heer','Aas']
suites = ['Harten', 'Klaver', 'Schoppen', 'Ruiten']
joker = ['Joker']
joker2 = ['Joker']
deck = [[s, v] for s in suites for v in values]
deck.append(joker and joker2)
random.shuffle(deck)
z = 0
for x in range(7):
    z += 1
    print(f"Kaart {z}:", random.choice(deck))

print("Deck (47 kaarten):", deck)