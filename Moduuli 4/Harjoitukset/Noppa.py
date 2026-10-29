import random
def heitä_noppa():
    return random.randint(1,6)
while True:
    silmäluku= heitä_noppa()
    print(silmäluku)
    if silmäluku ==6:
        break