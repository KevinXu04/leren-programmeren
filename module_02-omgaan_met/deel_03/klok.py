time = float(input("Hoe laat is het?"))

h = float(input("Welke uur is het?"))
m = float(input("Welke minuut is het?"))

endH = 23.00
endM = 60

h2 = endH - h
m2 = endM - m

print(f"""Het duurt nog {h2} uur en {m2} minuten voordat de dag voorbij is.
""")