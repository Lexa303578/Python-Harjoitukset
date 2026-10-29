sukupuoli=input("anna sukupuoli(mies/nainen):")
hemoglobiiniarvo=int(input("anna hemoglobiiniarvo(g/l):"))
if sukupuoli== "mies":
    if hemoglobiiniarvo < 134:
        print("hemoglobiiniarvo on alhainen")
    elif hemoglobiiniarvo <=195:
        print("hemoglobiiniarvo on normaali")
    else:
        print("hemoglobiniarvo on liian korkea")

if sukupuoli =="nainen":
    if hemoglobiiniarvo < 117:
        print("hemoglobiiniarvo on alhainen")
    elif hemoglobiiniarvo <=175:
        print("hemoglobiiniarvo on normaali")
    else:
        print("hemoglobiiniarvo on liian korkea")