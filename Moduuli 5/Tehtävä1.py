import random

maara = int(input("anna arpakuutioiden määrä:"))
summa = 0

for i in range(maara):
    silmaluku = random.randint(1,6)
summa +=silmaluku
print("silmälukujen summa on:", summa)