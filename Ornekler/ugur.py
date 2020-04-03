class Balik:
    tur = "moli"
    familya = "Balon Moli"

    def __init__(self,adi,yas):
        self.adi = adi
        self.yas = yas  
 
    def Swim(self):
        print(self.adi,"bıcı_bıcı")

    def Costu(self):
        print(self.adi,"Costu")
    
    def __del__(self):
        print(self.adi,"boguldu")

balik1 = Balik("Sarı","Erkek")
balik1.Swim()
del balik1