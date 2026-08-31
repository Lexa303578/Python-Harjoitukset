tuuma = 2.54
while tuuma <= 2.54:
        määrä=int(input("anna tummamäärä niin kauan kunnes annetaan negatiivisen tuumamäärän"))
        if määrä >=0:
                print("tuumat senttimetreinä "+str(tuuma * määrä)+"")
        else:
            print("negatiivinen luku pysäytää ohjelman")
            break