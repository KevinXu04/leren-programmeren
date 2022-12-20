from fruitmand import fruitmand

langsteNaam = (sorted(fruitmand,  key=lambda i: i['name'], reverse=True))
print(f' De "{langsteNaam[0]["name"]}" ({len(langsteNaam[0]["name"])}) letters heeft een {langsteNaam[0]["color"]} kleur en een gewicht van {langsteNaam[0]["weight"]/1000} kg')
