class Lentokone:
    def _init_(self, nimi,max_bensa,nykyinen_määrä):
        self.nimi = nimi
        self.max_bensa = max_bensa
        self.määrä = nykyinen_määrä

            def tiedot(self):
            print(f"Kone{self.nimi}")
            print(f"bensan max määrä{self.max_bensa}")
            print(f"bensan nykyinen määrä{self.määrä}")

kone = Lentokone("finnair",100,30)
kone.tiedot()

class Lentokenttä:
    def _init_(self,nimi):
        self.nimi = nimi
        self.koneet=[]


