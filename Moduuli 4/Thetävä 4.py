import random
randomi_luku=random.randint(1,10)

while True:
    luku = int(input("anna luku:"))
    if luku < randomi_luku:
        print("luku on liian pieni")
    elif luku > randomi_luku:
        print("luku on liian suuri")
    else:
        print("oikein")
        break


    

