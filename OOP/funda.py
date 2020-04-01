class Öğrenci :
    Ogretmen="Funda Tamdoğan"
    Sınıf="Güzelkent sabah grubu"
    def __init__(self,adi,yasi):
        self.adi=adi
        self.yasi=yasi
         
    def Ogrendi(self):
        print(self.adi,self.yasi,"A1 düzey ingilizce öğrendi")
        
    def __del__(self):
        print(self.adi,"Ders kaydını sildirdi")
        
Ögrenci1=Öğrenci("Kadir Taha ",11)
Ögrenci2=Öğrenci("Ecem Nur ",10)

Ögrenci1.Ogrendi()
del Ögrenci2