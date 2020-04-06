from DosyaTool import DosyaTool as DT
# class TelefonDefteri(DT):
#     def __init__(self):
#         super().__init__(adres="OrnekProje",dosyaadi="telefondefteri",
#         uzanti=".csv",ayrac=";",
#         alanlar=["Adı","Soyadı","Sabit Telefon","Cep Telefon","Eposta"])
    
#     def __del__(self):
#         print("Telefon Defteri Kapanıyor")
#         super().__del__()

# TelDef = TelefonDefteri()
# TelDef.Menu()

# from DosyaTool import DosyaTool as DT
# class KasaDefteri(DT):
#     def __init__(self):
#         super().__init__(adres="OrnekProje",dosyaadi="kasadefteri",
#         uzanti=".csv",ayrac=";",
#         alanlar=["Cari Ünvan:","Vergi Kimlik No:","Borç:","Alacak:"])

#     def __del__(self):
#         print("Kasa Defteri Kapanıyor")
#         super().__del__()
    
#     def Listele(self):
#         for i in range(len(self.kayitlar)):
#             fark = int(self.kayitlar[i].split(";")[3])-int(self.kayitlar[i].split(";")[2])
#             print(f"{i+1}-{self.kayitlar[i].replace(self.ayrac,'  ')}-{fark}")


# KasDef = KasaDefteri()
# KasDef.Menu()

# csv comma seperated value virgülle ayrılmış veri

# from DosyaTool import DosyaTool as DT
# class VeresiyeDefteri(DT):
#     def __init__(self):
#         super().__init__(adres="OrnekProje",dosyaadi="VeresiyeDefteri",uzanti=".csv",ayrac=";",
#         alanlar=["Adı","Soyadı","Borç Miktarı:","Cep Telefonu:"])

#     def __del__(self):
#         print("Veresiye defteri kapanıyor.")
#         super().__del__()

# VerDef=VeresiyeDefteri()
# VerDef.Menu()


from DosyaTool import DosyaTool as DT
class Icindekiler(DT):
    def __init__(self):
        super().__init__(adres="OrnekProje",dosyaadi="İçindekiler",uzanti=".csv",ayrac=";",
        alanlar = ["Başlık","Sayfa"])

    def __del__(self):
        print("içindekiler")
        super().__del__() 
icinde = Icindekiler()
icinde.Menu()