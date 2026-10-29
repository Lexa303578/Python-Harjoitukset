yritykset = 0
while yritykset < 5:
    tunnus=input("käyttäjätunnus:")
    salasana=input("salasana:")
    if tunnus =="python" and salasana =="rules":
        print("Tervetuloa")
        break
    yritykset += 1

if yritykset == 5:
    print("Pääsy evätty")
