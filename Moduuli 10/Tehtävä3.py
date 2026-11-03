class Hissi:
    def __init__(self,alin_kerros,ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def kerros_ylös(self):
            if self.kerros < self.ylin_kerros:
                self.kerros += 1
                print("Hissi on kerroksessa", self.kerros)

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
            print("Hissi on kerroksessa", self.kerros)
    
    def siirry_kerrokseen(self,kohde):
        while self.kerros < kohde:
            self.kerros_ylös()

        while self.kerros > kohde:
            self.kerros_alas()

class Talo:
    def __init__ (self,alin_kerros,ylin_kerros, hissien_lukumäärä):
        self.hissit = []

        for i in range(hissien_lukumäärä):
            hissi = Hissi(alin_kerros,ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissiä(self,hissin_numero, kohdekerros):
        self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(hissi.alin_kerros)

talo = Talo(1, 7, 3)

talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 3)
talo.aja_hissiä(2, 7)

print("PALOHÄLYTYS!")
talo.palohälytys()