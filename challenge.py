iphone = int(input("Hoe duur is de iPhone 13? "))
samsung = int(input("Hoe duur is de Samsung Galaxy S22? "))
asus = int(input("Hoe duur is de Asus Zenfone 9?"))

if (iphone < samsung and asus < samsung and asus > iphone):
    print(f"""De Samsung Galaxy S22 is het duurst, de telefoon kost: {samsung} euro.
De iPhone 13 is het goedkoopst, de telefoon kost: {iphone} euro.
De Asus Zenfone 9 zit er tussenin met: {asus} euro.
""")
elif (iphone > samsung and asus > samsung and asus < iphone):
    print(f"""De iPhone 13 is het duurst, de telefoon kost: {iphone} euro.
De Samsung Galaxy S22 is het goedkoopst, de telefoon kost: {samsung} euro.
De Asus Zenfone 9 zit er tussenin met: {asus} euro.
""")
elif (asus > samsung and iphone > samsung and iphone < asus):
    print(f"""De Asus Zenfone 9 is het duurst, de telefoon kost: {asus} euro.
De Samsung Galaxy S22 is het goedkoopst, de telefoon kost: {samsung} euro.
De iPhone 13 zit er tussenin met: {iphone} euro.
""")
elif (asus < samsung and iphone > asus and iphone < samsung):
    print(f"""De Samsung Galaxy S22 is het duurst, de telefoon kost: {samsung} euro.
De Asus Zenfone 9 is het goedkoopst, de telefoon kost: {asus} euro.
De iPhone 13 zit er tussenin met: {iphone} euro.
""")
elif (asus > iphone and samsung > iphone and samsung < asus):
    print(f"""De Asus Zenfone 9 is het duurst, de telefoon kost: {asus} euro.
De iPhone 13 is het goedkoopst, de telefoon kost: {iphone} euro.
De Samsung Galaxy S22 zit er tussenin met: {samsung} euro.
""")
elif (asus < iphone and samsung > asus and samsung < iphone):
    print(f"""De iPhone 13 is het duurst, de telefoon kost: {iphone} euro.
De Asus Zenfone 9 is het goedkoopst, de telefoon kost: {asus} euro.
De Samsung Galaxy S22 zit er tussenin met: {samsung} euro.
""")