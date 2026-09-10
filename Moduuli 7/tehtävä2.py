nimet = set()

while True:
    nimi = input("anna nimi:")
    if nimi == "":
        break
    if nimi in nimet:
        print("aiemmin syötetty nimi")
    else:
        print("uusi nimi")
        nimet.add(nimi)
        print("syötetyt nimet:")
        for nimi in nimet:
            print(nimi)
