class Auto:
    def __init__(self,rekisteritunnus,huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self,tuntimäärä):
        self.kuljettu_matka += self.nopeus * tuntimäärä

auto = Auto("ABC-123", 142)

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

print("Auton nopeus:", auto.nopeus, "km/h")

auto.kiihdytä(-200)
print("Nopeusjarrutuksen jälkeen:", auto.nopeus, "km/h")

auto.nopeus = 60
auto.kuljettu_matka = 2000
auto.kulje(1.5)

print("Kuljettu matka:",auto.kuljettu_matka, "km")