class A:
    sinif_ozellik = "Deneme"
    def __init__(self):
        self.ornek_ozellik
    def ornekMetod(self):
        return self.ornek_ozellik

    @classmethod
    def sinif_method(cls):
        return cls.sinif_ozellik

    @staticmethod
    def statik():
        return 22//7
import time
import math

def hesapZaman(fonk):
    def icFonk(*args,**kwargs):
        begin = time.time()
        fonk(*args,**kwargs)
        end = time.time()
        print("Bu işlem yapılırken geçen zaman:",fonk.__name__,end-begin)

    return icFonk
    
@hesapZaman
def Faktoriyel(param):
    time.sleep(2)
    print(math.factorial(param))

Faktoriyel(10)