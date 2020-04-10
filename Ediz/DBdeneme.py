import sqlite3 as sql
try:
    db = sql.connect("DB/IK.sqlite")
    cur = db.cursor()
    adi = input("Adınızı Giriniz:")
    soyadi = input("Soyadınızı Giriniz:")
    telefon = input("Telefon Numaranızı Giriniz:")
    sorgu = f"""
    INSERT INTO telefonlar (adi,soyadi,tel_no)
    VALUES 
    ('{adi}','{soyadi}','{telefon}')
    """
    cur.execute(sorgu)
except Exception as hata:
    print("Hata oluştu:",hata)
finally:
    cur.close()
    db.commit()
    db.close()
# insert #
# delete #
# update #