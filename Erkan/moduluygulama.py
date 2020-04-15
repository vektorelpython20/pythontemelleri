import datetime as dt
import os
zaman=dt.datetime.now()
liste=[zaman.year,zaman.month,zaman.day,zaman.hour,zaman.minute]
print(*map(str,liste))
os.chdir(r"C:\PythonDeneme")

try:
    os.makedirs(os.sep.join(map(str,liste)))
    mesaj="Klasör oluşturdum."
except Exception as hata:
    mesaj=hata
liste.insert(0,r"C:\PythonDeneme")
dosya=open(os.sep.join(map(str,liste))+os.sep+"log.csv","a+")
print(zaman,mesaj,file=dosya)
dosya.close()
