# Çokbiçimlilik
# overload
# override
# built in polymorphic functions
metin = "Python"
liste = [1,2,3,4]
print(len(metin))
print(len(liste))
# user defined polymorphic functions
def Fonk(a,b,c=4):
    return a+b+c
print(Fonk(1,2))
print(Fonk(1,2,3))
# Polymorphism with class methods
class A:
    def foo():
        print("A Fooo")
    def tii():
        print("A tiii")

class B:
    def foo():
        print("B Fooo")
    def tii():
        print("B tiii")

def Fonk(nesne):
    nesne.foo()
    nesne.tii()

for item in (A,B):
    Fonk(item)

#Polymorphism with Inheritance

class A:
    def __init__(self):
        self.a = "a"

    def Func(self):
        print("A dan Çalıştı")

class B(A):
    def __init__(self):
        super().__init__()
        self.b = "b"
    
    def Func(self):
        print("B den Çalıştı")
class C(A):
    def __init__(self):
        super().__init__()
        self.c = "c"

nesne1 = A()
nesne2 = B()
nesne3 = C()
nesne1.Func()
nesne2.Func()
nesne3.Func()
