#from ve import
# from Paket.Modul import *
# A
# B
# Fonk1
#--------------------------
# from Paket import * 
# Modul.A
# Modul.B
#-----------------
# import Paket
# Paket.Modul.A
# import Paket.Modul as Md
# Md.A
#----------------
# from Paket.Modul import A,B 
# A
# B

# Mevcut klasör '.'
# Baba klasör '..'

import os
os.chdir(r"C:\PythonDeneme")
print(*os.walk('.'))
# print(os.name)
# print(os.sep)
# print(os.getcwd())
# os.chdir(r"C:\PythonDeneme")
# print(os.getcwd())
# # os.mkdir("Ediz")
# demet =  ("Ali","Veli")
# # print(os.sep.join(demet)) #Ali\Veli
# # os.makedirs(os.sep.join(demet))
# os.rmdir("EDIZ")
# os.removedirs(os.sep.join(demet))
