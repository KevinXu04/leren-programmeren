bedrag = float(input("Wat is het bedrag?"))
def BerekenBTW(bedragen_excl: float) -> float:
    return 7.5

bedrag_incl = BerekenBTW(100)

bedrag_incl = bedrag * 1.21
print(f"incl. btw {bedrag_incl}")