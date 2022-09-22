iphone = int(input("Hoe duur is de iPhone 13? "))
samsung = int(input("Hoe duur is de Samsung Galaxy S22? "))
asus = int(input("Hoe duur is de Asus Zenfone 9? "))

max1 = samsung - asus
max2 = iphone - asus
max3 = samsung - iphone
max4 = iphone - samsung
max5 = asus - samsung

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
De Asus Zenfone 9 is het goedkoopst, de telefoon kost: {iphone} euro.
De Samsung Galaxy S22 zit er tussenin met: {samsung} euro.
""")

if (max1 >= 100 and max2 >= 100 and iphone > samsung):
    print(f"""Het advies is dus de Asus Zenfone 9 te kopen. 
Deze is namelijk {max1} euro goedkoper dan de Samsung Galaxy S22 en {max2} euro goedkoper dan iPhone 13.""")
elif (max1 >= 100 and max2 >= 100 and iphone < samsung):
    print(f"""Het advies is dus de Asus Zenfone 9 te kopen. 
Deze is namelijk {max2} euro goedkoper dan de iPhone 13 en {max1} euro goedkoper dan Samsung Galaxy S22.""")
elif (iphone > samsung and max4 <= 50 and asus < samsung):
    print(f"""Het advies is dus de iPhone 13 te kopen. 
Deze is namelijk {max4} euro goedkoper dan de Samsung Galaxy S22 en {max2} euro goedkoper dan Asus Zenfone 9.""")
elif (iphone > samsung and max4 > 50 and asus > samsung):
    print(f"""Het advies is dus de Samsung Galaxy S22 te kopen. 
Deze is namelijk {max4} euro goedkoper dan de iPhone 13 en {max5} euro goedkoper dan Asus Zenfone 9.""")
elif (iphone < samsung and asus < samsung):
    print(f"""Het advies is dus de iPhone 13 te kopen. 
Deze is namelijk {max4} euro goedkoper dan de iPhone 13 en {max5} euro goedkoper dan Asus Zenfone 9.""")