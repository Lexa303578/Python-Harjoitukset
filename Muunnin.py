grammamäärä = float(input("anna grammamäärä"))

gramma = grammamäärä % 1000
kilo = grammamäärä // 100

print(f"{kilo}kg ja {gramma}g")

