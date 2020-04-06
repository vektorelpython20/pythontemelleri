from os import sep,path
class DosyaTool:
    def __init__(self,adres=r"OrnekProje",dosyaadi="defter",uzanti=".csv",
    ayrac=";",alanlar=["Adı","Soyadı","Telefon"]):
        self.adres = adres
        self.dosyaadi = "defter"
        self.uzanti = uzanti 
        self.dosyaAdresi = self.adres + sep + self.dosyaadi + self.uzanti
        self.ayrac = ayrac
        self.alanlar = alanlar
        self.dosya = None
        self.DosyaAc()
        self.kayitlar = self.dosya.readlines()


    def DosyaAc(self):
        if path.exists(self.dosyaAdresi):
            self.dosya = open(self.dosyaAdresi,"r+")
        else:
            self.dosya = open(self.dosyaAdresi,"w+")
    
    def __del__(self):
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writelines(self.kayitlar)
        self.dosya.close()

    def DosyaKaydet(self):
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writelines(self.kayitlar)
        self.dosya.flush()

    def Listele(self):
        for i in range(len(self.kayitlar)):
            print(f"{i+1}-{self.kayitlar[i].replace(self.ayrac,'  ')}")
    

    def GirisAl(self):
        kayit = ""
        for item in self.alanlar:
            kayit += input(item + " Giriniz :") + self.ayrac
        else:
            #ali;veli;123123; ilk hali
            kayit =  kayit.rstrip(";") + "\n"
            #ali;veli;123123\n son hali
        return kayit
    
    def Ekleme(self):
        self.kayitlar.append(self.GirisAl())
    
    def Guncelleme(self):
        self.Listele()
        self.kayitlar[int(input("Düzenlemek istediğin kaydı seç"))-1] = self.GirisAl()

    def Silme(self):
        self.Listele()
        del self.kayitlar[int(input("Sil istediğin kaydı seç"))-1]
    
    def EXIT(self):
        return input("Çıkmak istediğinden emin misin?(E/H):").lower()

    def Menu(self):
        menu = """
        1-Listele
        2-Ekleme
        3-Güncelleme
        4-Silme
        5-Çıkış
        İşlem Seçiniz:
        """
        FonkListe = [self.Listele,self.Ekleme,self.Guncelleme,self.Silme,self.EXIT]
        islem = 1
        while 0<islem<6:
            islem = int(input(menu))
            if islem != 5:
                FonkListe[islem-1]()
            else:
                if self.EXIT() == "e":
                    break
                else:
                    continue

if __name__ == "__main__":
    deneme = DosyaTool()
    deneme.Menu()