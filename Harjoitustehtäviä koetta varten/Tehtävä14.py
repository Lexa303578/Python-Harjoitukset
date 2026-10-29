import math

def yksikköhinta(halkaisija,hinta):
    säde= halkaisija/2
    pinta_ala = math.pi*säde**2
    pinta_ala_m2= pinta_ala / 10000
    return hinta / pinta_ala_m2
halkaisija1 = float(input("anna ensimmäisen pizzan halkaisija (cm):"))
hinta1= float(input("anna ensimmäisen pizzan hinta(€):"))
halkaisija2 = float(input("anna toisen pizzan halkaisjan pituus (cm):"))
hinta2=float(input("anna toisen pizzan halkaisjna pituus (cm):"))

yksikkohinta1=yksikköhinta(halkaisija1,hinta1)
yksikkohinta2=yksikköhinta(halkaisija2,hinta2)
print("ensimmäisen pizzan yksikköhinta:",yksikkohinta1,"€/m2")
print("toisen pizzan ykiskköhinta:",yksikkohinta2,"€/m2")

if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif yksikkohinta2 < yksikkohinta1:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Pizzat ovat yhtö edullisia")
