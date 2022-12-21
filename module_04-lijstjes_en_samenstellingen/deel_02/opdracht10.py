from fruitmand import fruitmand

zwaarsteFruit = (sorted(fruitmand,  key=lambda i: i['weight'], reverse=True))

for x in range(len(zwaarsteFruit)):
    print(zwaarsteFruit[x]['name'], zwaarsteFruit[x]['weight'], 'gram')