class Inventaario:
    def __init__(self, tavarat=[]):
        self.tavarat= tavarat

        self.tavarat = tavarat

    def lisaa_tavara(self):
        uusi=input("Kirjoita uuden esineen nimi:")
        self.tavarat.append(uusi)

    def tulosta(self):
        for t in self.tavarat:



            varasto = Inventaario()
