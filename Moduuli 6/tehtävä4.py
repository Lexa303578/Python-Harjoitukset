def laske_summa(luvut):
    summa =0
    for luku in luvut:
        summa += luku
        return summa
    luvut= [2,5,7,3,8]
    tulos = laske_summa(luvut)
    print("Lukujen summa on:", tulos)