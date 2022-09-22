iphone = int(input("Hoe duur is de iPhone 13? "))
samsung = int(input("Hoe duur is de Samsung Galaxy S22? "))

max1 = samsung - iphone
max2 = iphone - samsung

if (iphone > 900 and samsung > 900 and iphone > samsung):
    print(f"""De iPhone is het duurst, de telefoon kost: {iphone} euro.
De Samsung is het goedkoopst, de telefoon kost: {samsung} euro
Het advies is dus geen telefoon te kopen, ze zijn te duur
""")
    exit()
elif (iphone > 900 and samsung > 900 and iphone < samsung):
    print(f"""De Samsung is het duurst, de telefoon kost: {samsung} euro.
De iPhone is het goedkoopst, de telefoon kost: {iphone} euro
Het advies is dus geen telefoon te kopen, ze zijn te duur
""")
    exit()


if iphone < samsung:
    print(f"""De Samsung is het duurst, de telefoon kost: {samsung} euro.
De iPhone is het goedkoopst, de telefoon kost: {iphone} euro.
Het advies is dus de iPhone te kopen. Deze is namelijk {max1} euro goedkoper dan de Samsung
""")
    exit()
if max2 > 50:
    print(f"""De iPhone is het duurst, de telefoon kost: {iphone} euro.
De Samsung is het goedkoopst, de telefoon kost: {samsung} euro.
Het advies is dus de Samsung te kopen. Deze is namelijk {max2} euro goedkoper dan de iPhone
""")
elif max2 <= 50:
    print(f"""De iPhone is het duurst, de telefoon kost: {iphone} euro.
De Samsung is het goedkoopst, de telefoon kost: {samsung} euro.
Het advies is dus de iPhone te kopen. Deze is namelijk {max2} euro duurder dan de Samsung
""")
