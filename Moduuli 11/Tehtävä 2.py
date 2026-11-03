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

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus,bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sähköauto.kiihdytä(120)
polttomoottoriauto.kiihdytä(100)

sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

print("Sähköauton matkamittari:",sähköauto.kuljettu_matka, "km")
print("Polttomoottoriauton matkamittari", polttomoottoriauto.kuljettu_matka, "km")