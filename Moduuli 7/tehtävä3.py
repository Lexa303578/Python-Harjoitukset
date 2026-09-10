lentoasemat ={}
while True:
    print("valitse toiminto:")
    print("1-syötä uusi lentoasema")
    print("2-Hae lentoaseman tiedot")
    print("3-Lopeta")

    valinta = input("valinta:")
    if valinta == "1":
        icao = input("Anna lentoasmean ICAO-koodi:")
        nimi = input("Anna lentoaseman nimi:")
        lentoasemat[icao]= nimi

    elif valinta == "2":
        icao = input("Anna Lentoasmean ICAO-koodi")
        if icao in lentoasemat:
            print(lentoasemat[icao])
        else:
            print("Lentoasemaa ei löytynyt")

    elif valinta == "3":
        break
    else:
        print("Virheellinen valinta.")