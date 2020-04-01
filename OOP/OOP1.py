class Kedi:  # class 
    tur = "Memeli" # class attribute - sınıf özelliği
    familya = "Felis"  # class attribute - sınıf özelliği

    def __init__(self,adi,yas): # constructor _  yapıcı
        self.adi = adi # instance attribute - örnek özellik
        self.yas = yas

    def Miyavla(self):   # instance method - örnek metod
        print(self.adi,"Miyavladi")
    
    def Beslendi(self):
        print(self.adi,"Beslendi")

    def __del__(self): # destructor  _ yıkıcı 
        print(self.adi,"Rest in peace")


kedi1 = Kedi("Melek",5)
kedi1.Miyavla()
kedi1.Beslendi()
del kedi1