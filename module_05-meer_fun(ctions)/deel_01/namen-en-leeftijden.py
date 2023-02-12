def dictionary():
    name = input("Vul een naam in. \n")
    age = int(input("Vul de leeftijd in. \n"))
    return {"name": name, "age": age}

info = []

while True:
    dictInfo = dictionary()
    info.append(dictInfo)
    doorgaan = input("Toets enter om door te gaan of stop om te printen: \n")
    if doorgaan == "stop":
        break

for x in info:
    print(f"{x['name']} is {x['age']} jaar oud.")