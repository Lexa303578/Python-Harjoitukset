luvut = []

while True:
    syöte=input("anna luku:")
    if syöte == "":
        break
    luvut.append(int(syöte))
    luvut.sort(reverse=True)
    print("viisi suurinta lukua")
    for luku in luvut[:5]:
        print (luku)

    