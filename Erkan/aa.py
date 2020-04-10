import sqlite3 as sql
try:    
    db=sql.connect("DB/IK.sqlite")
    cur=db.cursor()
    adi=input("adınızı giriniz:")
    soyadi=input("soyadinizi giriniz:")
    telefon=input("telefon numaranızı giriniz:")

    sorgu=f"""
    insert into telefonlar (adi,soyadi,tel_no) values 
    ('{adi}','{soyadi}','{telefon}')"""
    cur.execute(sorgu)
except Exception as hata:
    print("hata oluştu:",hata)
finally:
    cur.close()
    db.commit()
    db.close()