birds = [{'name':'mus','key':'m','count':0},
          {'name':'duif','key':'d','count':0},
          {'name':'koolmees','key':'k','count':0},
          {'name':'kraai','key':'i','count':0},
          ]

print('Bird counter until dot \n')

# 1
for bird in birds:
    print(f"{bird['key']}: {bird['name']}")

# 2
def getBirdByKey (birds: list, key: str) -> str:
    for bird in birds:
        if key == bird['key']:
            return bird

# 3
key = ''
while key != ".":
    key = input("Vogel naam ")
    bird = getBirdByKey(birds, key)
    if bird in birds:
        bird['count'] += 1
        print(f"{bird['name']} count: {bird['count']}")

# 4
for bird in birds:
    print(f"{bird['count']}x {bird['name']}")

# 5
totalCount = 0

for bird in birds:
    totalCount += bird['count']

if totalCount > 0:
    percentage = 100 / totalCount

    for bird in birds:
        if bird['count']:
            print(f"{bird['name']}: percentage: {round(bird['count'] * percentage, 2)}% count: {bird['count']}")
else:
    print('No birds')

print(f"Total birds: {totalCount}")

# TO DO:

# 1) print all birds with key and name

# 2) define function get_bird_by_key(birds: list, key:str) returns bird or None

# 3) repeat until given '.'
#       input key of bird 
#    find bird with get_bird_by_key
#    if bird found: 
#       increment bird count
#       show bird name and count

# 4) print all birds with name and count

# 5) print per bird also the percentage of the total count