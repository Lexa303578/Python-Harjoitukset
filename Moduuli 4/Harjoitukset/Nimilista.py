nimet = set()
while True:
    nimi = input("anna nimi:")
    if nimi =="":
        break
    if nimi in nimet:
        print("Nimi on jo listalla")
    else:
        print("Uusi nimi")
        nimet.add(nimi)
        for nimi in nimet:
            print(nimi)