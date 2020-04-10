import sqlite3 as sql
class TelefonDefter:
    def __init__(self):
        self.db = sql.connect("DB/IK.sqlite")
        self.cur = self.db.cursor()
    
    def Ekleme(self):
        try:
            adi = input("Adınızı Giriniz: ")
            soyadi = input("Soyadınızı Giriniz: ")
            telefon = input("Telefon numaranızı giriniz: ")
            sorgu = f"""
            INSERT INTO telefonlar (adi,soyadi,tel_no)
            VALUES
            ('{adi}','{soyadi}','{telefon}')
            """
            self.cur.execute(sorgu)
            return 1
        except Exception as hata: 
            print("Hata oluştu.",hata)
            return hata
        finally:
            self.db.commit()

    def Guncelleme(self,id):
        try:
            adi = input("Adınızı Giriniz: ")
            soyadi = input("Soyadınızı Giriniz: ")
            telefon = input("Telefon numaranızı giriniz: ")
            sorgu = f"""
            UPDATE telefonlar SET adi = '{adi}',soyadi='{soyadi}',tel_no='{telefon}'
            WHERE tel_id = {id}
            """
        except Exception as hata: 
            print("Hata oluştu.",hata)
            return hata
        finally:
            self.db.commit()

    def Silme(self,id):
        try:
            sorgu = f"""DELETE FROM telefonlar WHERE tel_id = {id}"""
            self.cur.execute(sorgu)
            return 1
        except Exception as hata: 
            print("Hata oluştu.",hata)
            return hata
        finally:
            self.db.commit()

    def Listeleme(self):
        try:
            sorgu =f"""SELECT * FROM telefonlar"""
            self.cur.execute(sorgu)
            liste = self.cur.fetchall()
            for tel_id,adi,soyadi,tel_no in liste:
                print(f"{tel_id}-{adi} {soyadi} {tel_no}")
        except Exception as hata: 
            print("Hata oluştu.",hata)
            return hata

    def Menu(self):
        menu = """
        1-Ekleme
        2-Silme
        3-Güncelleme
        4-Listeleme
        5-Çıkış
        """
        islem = 0
        while islem < 6:
            islem = int(input(menu))
            if islem != 5:
                if islem ==1:
                    self.Ekleme()
                elif islem == 2:
                    self.Listeleme()
                    secid = int(input("Silmek istediğiniz kaydın numarasını giriniz"))
                    self.Silme(secid)
                elif islem == 3:
                    self.Listeleme()
                    secid = int(input("Güncellemek istediğiniz kaydın numarasını giriniz"))
                    self.Silme(secid)
                elif islem == 4:
                    self.Listeleme()
            else:
                islem = 6
        else:
            print("İyi Günler Dİleriz")
                

    def __del__(self):
        self.cur.close()
        self.db.commit()
        self.db.close()
        
telDefter = TelefonDefter()
telDefter.Menu()