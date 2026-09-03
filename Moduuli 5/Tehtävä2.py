luvut = []

while True:
    syote = input("anna luku:" )
    if syote == "":
        break
    luvut.append(int(syote))
    luvut.sort(reverse=True)
    print("viisi suurinta lukua")
    for luku in luvut[:5]:
        print(luku)