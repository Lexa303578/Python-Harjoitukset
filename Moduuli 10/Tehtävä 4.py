import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        uusi_nopeus = self.nykyinen_nopeus + nopeuden_muutos

        if uusi_nopeus > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nykyinen_nopeus = 0
        else:
            self.nykyinen_nopeus = uusi_nopeus

    def kulje(self, tuntimäärä):
        self.kuljettu_matka += self.nykyinen_nopeus * tuntimäärä


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("\n", self.nimi)
        print("-" * 65)
        print(f"{'Rekisteritunnus':<18}{'Nopeus (km/h)':<18}{'Matka (km)':<15}")
        print("-" * 65)

        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<18}"
                  f"{auto.nykyinen_nopeus:<18}"
                  f"{auto.kuljettu_matka:<15.1f}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False



autot = []

for i in range(10):
    auto = Auto("ABC-" + str(i + 1), random.randint(100, 200))
    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1

    if tunnit % 10 == 0 and not kilpailu.kilpailu_ohi():
        kilpailu.tulosta_tilanne()

print("\nKILPAILU ON PÄÄTTYNYT!")
print("Kilpailuun kului", tunnit, "tuntia.")

kilpailu.tulosta_tilanne()
