import datetime as dt
import os
zaman = dt.datetime.now()
liste=[zaman.year,zaman.month,zaman.day,zaman.hour,zaman.minute]
# [2020,4,15,20,9]
print(*map(str,liste))
#['2020','4','15','20','9']
os.chdir(r"C:\PythonDeneme")
try:
    #'2020\4\15\20\9'
    os.makedirs(os.sep.join(map(str,liste)))
    mesaj = "Klasör Oluşturdum"
except Exception as hata:
    mesaj = hata
liste.insert(0,r"C:\PythonDeneme")
#["C:\PythonDeneme",2020,4,15,20,9]
# 'C:\PythonDeneme\2020\4\15\20\9\log.csv'
dosya = open(os.sep.join(map(str,liste))+os.sep+"log.csv","a+")
print(zaman,mesaj,file=dosya)
dosya.close()

