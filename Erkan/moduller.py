import os
print(os.name)
print(os.getcwd())
os.chdir(r"C:\PythonDeneme") #mevcut çalışan klasörü değiştirme kodu
print(os.getcwd())
#os.mkdir("Erkan")    #Erkan adında klasör oluşturur.
demet=("Ali","Veli")
print(os.sep.join(demet))    #Ali\Veli
os.makedirs(os.sep.join(demet))
