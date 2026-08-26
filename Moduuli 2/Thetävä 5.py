leiviskä = float(input("anna leiviskä:"))
naula = float(input("anna naulat:"))
luoti = float(input("anna luodit:"))

luoti = 0.0133
naula = luoti * 32
leiviskä = naula * 20

luotien_paino = luoti * luoti
naulojen_paino = naula * naula
leiviskä_paino = leiviskä * leiviskä

massa1 = luotien_paino + naulojen_paino + leiviskä_paino
massa2 = int(massa1 * 1000)
k = int(massa2 // 1000)
g = massa2 % 1000
print("Massa nykymittojen mukaan:",k,"kiloa ja",g,"Grammaa.")

