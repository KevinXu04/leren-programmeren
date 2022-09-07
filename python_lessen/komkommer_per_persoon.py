
# Ingrediënten voor Tzatziki
# 1 Komkommer voor 3 personen

print('Bereken van de ingrediënten')
aantalpersonen = input('Hoeveel personen: ')
aantalpersonen = int(aantalpersonen)

PersonenPerKomkommer = 1/3
aantalkomkommer = PersonenPerKomkommer * aantalpersonen

ZeeZoutPuntjesPerPersoon = 1/3
zeezoutpuntjes = ZeeZoutPuntjesPerPersoon * aantalpersonen

TenenKnoflookPerPersoon = 2/3
tenenknoflook = TenenKnoflookPerPersoon * aantalpersonen

VerseDillePerPersoon = 15/3
versedille = VerseDillePerPersoon * aantalpersonen

GriekseYoghurtPerPersoon = 500/3
griekseyoghurt = GriekseYoghurtPerPersoon * aantalpersonen

WitteAzijnPerPersoon = 1/3
witteazijn = WitteAzijnPerPersoon * aantalpersonen

ExtraViergeOlijfOlie = 1
extraviergeolijfolie = ExtraViergeOlijfOlie * aantalpersonen



print('Aantal komkommers:', aantalkomkommer)
print('Mespuntjes zeezout:', zeezoutpuntjes)
print('Tenen knoflook:', tenenknoflook)
print('Aantal gram dille:', versedille)
print('Aantal ml Griekse Yoghurt 10%:', griekseyoghurt)
print('Aantal eetlepels Witte Azijn:', witteazijn)
print('Aantal eetlepels extra vierge olijfolie:', extraviergeolijfolie)