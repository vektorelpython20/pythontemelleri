import sqlite3 as sql
db = sql.connect("DB/IK.sqlite")
cur = db.cursor()
adi = input("Adınızı Giriniz:")
soyadi =input("Soyadınızı Giriniz:")
telefon = input("Telefon numaranızı Giriniz:")
sorgu = f""""
INSERT INTO telefonlar (adi,soyadi,tel_no)
VALUES
('{adi}','{soyadi}','{telefon}')
"""
cur.execute(sorgu)
except Exception as hata:
    print("hata oluştu",hata)
finally:
    cur.close()
    db.commit()
    db.close()
# insert #
# delete #
# update #
