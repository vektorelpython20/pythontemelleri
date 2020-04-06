class Personel:
    isim = ""
    yas = 0
    def __init__(self, personelIsim,personelYas):
        self.isim = personelIsim
        self.yas = personelYas

    def __repr__(self):
        return "{isim:"+self.isim+",yas:"+str(self.yas)+"}"
    
    def __str__(self):
        return "Personel(isim="+self.isim+", yas="+str(self.yas)+")"

P1 = Personel("Ali",25)
P2 = Personel("Veli",35)
