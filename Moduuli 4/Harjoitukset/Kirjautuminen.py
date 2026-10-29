yritykset = 0
while yritykset < 5:
    tunnus =input("anna käyttäjätunnus:")
    salasana =input("anna salasana:")
    if tunnus == "Python" and salasana == "jules":
        print("Tervetuloa")
        break
    yritykset += 1

if yritykset == 5:
    print("Pääsy evätty")


