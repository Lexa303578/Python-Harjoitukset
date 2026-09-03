import random
def heita_noppaa(tahkot):
    return random.randint(1, tahkot)
tahkot = int(input("anna nopan tahkojen määrä:"))
while True:
    silmaluku= heita_noppaa(tahkot)
    print(silmaluku)
    if silmaluku == tahkot:
        break