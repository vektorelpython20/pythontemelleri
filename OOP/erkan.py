class kurt:
    tur="memeli"
    familya="Canidae"

    def __init__(self,adi,dogum_yili):
        self.adi=adi
        self.dogum_yili=dogum_yili

    def avlandi(self): 
        print(self.adi,"avlandı.")

    def uludu(self):
        print(self.adi,"uludu.")

    def suru_lideri(self):
        print(self.adi,"alfa kurt oldu.")

    def __del__(self):
        print(self.adi,"==>Kurtlar yalnız ölür. :( ")

kurt1=kurt("Yalnız kurt",2010)
kurt1.avlandi()
kurt1.uludu()
kurt1.suru_lideri()

del kurt1