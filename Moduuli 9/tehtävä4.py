import random

class Auto:
    def __init__(self,rekisteritunnus,huippunopeus):
        self.rekisteritunnus= rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntimäärä):
        self.kuljettu_matka += self.nopeus * tuntimäärä

autot = []

for i in range(1,11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)


    kilpailu_jatkuu = True

    while kilpailu_jatkuu:
        for auto in autot:
            nopeuden_muutos= random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)

        for auto in autot:
            if auto.kuljettu_matka >= 10000:
                kilpailu_jatkuu = False
                break


        print(f"{'rekisteritunnus':<18}{'huippunopeus':<18}"
              f"{'nopeus':<15}{'kuljettumatka':<18}")
        print("-" * 69)

        for auto in autot:
            print(f"{auto.rekisteritunnus:<18}"
                  f"{auto.huippunopeus:<18}"
                  f"{auto.nopeus:<15}"
                  f"{auto.kuljettu_matka:<18.1f}")