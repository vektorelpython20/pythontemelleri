# Encapsulation Kapsülleme
class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.__c =3 #private
        self._d = 1 #semi private

    @property
    def c(self):  # getter
        return self.__c
    
    @c.setter  # setter
    def c(self,c):
        if isinstance(c,str):
            if c.isnumeric():
                c = int(c)
                if 10<c<20: 
                    self.__c = c
                    print("c yi değiştirdim")
        else:
            print("C yanlış değer")
    
    @c.deleter # deleter
    def c(self):
        self.silinen_c = self.__c
        del self.__c

    
    def FuncA(self):
        return self.a
    

nesne1 = A("A","B")

print(nesne1.c)
nesne1.FuncA()
nesne1.c = "5"



"""
Pythonda yok
Access Modifier
private
public
static
"""

"""
__gizli gizli
__gizli_ gizli
__gizli__ gizli değil
"""