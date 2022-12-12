from fruitmand import fruitmand

test = (sorted(fruitmand,  key=lambda i: i['weight'], reverse=True))

for x in range(len(test)):
    print(test[x]['name'])
    print(test[x]['weight'])

