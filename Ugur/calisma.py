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



    def __del__(self):
        self.cur.close()
        self.db.commit()
        self.db.close()