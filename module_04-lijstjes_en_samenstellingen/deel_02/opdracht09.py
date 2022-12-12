from fruitmand import fruitmand

fruitmand.remove({
    'name' : 'druif',
    'weight' : 5,
    'color' : 'red',
    'round' : True
})
for x in range(len(fruitmand)):
    print(fruitmand[x]['color'])