luku = int(input("anna kokonaisluku:"))
if luku < 2:
    print("luku ei ole kokonaisluku")
else:
    alkuluku= True
    for jakaja in range(2,luku):
        if luku % jakaja == 0:
            alkuluku =False
            break
        if alkuluku:
            print("Luku on alkuluku")
        else:
            print("luku ei ole alkuluku")