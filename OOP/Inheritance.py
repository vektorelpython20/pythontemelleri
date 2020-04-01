# class A:
#     def __init__(self):
#         self.a = "a"

#     def Func(self):
#         print("A dan Çalıştı")
    
# class B:
#     def __init__(self):
#         self.a = "a"
#         self.b = "b"
        
#     def Func(self):
#         print("A dan Çalıştı")

# class C:
#     def __init__(self):
#         self.a = "a"
#         self.b = "b"
#         self.c = "c"
        
#     def Func(self):
#         print("A dan Çalıştı")

class A:
    def __init__(self):
        self.a = "a"

    def Func(self):
        print("A dan Çalıştı")

class B(A):
    def __init__(self):
        super().__init__()
        self.b = "b"
    
class C(B):
    def __init__(self):
        super().__init__()
        self.c = "c"


class D():
    def __init__(self):
        self.d = "d"

class E(A,D):
    def __init__(self):
        A.__init__(self)
        D.__init__(self)
        self.e = "e"

class F(E):
    def __init__(self):
        super().__init__()

class G(F):
    def __init__(self):
        super().__init__()

# F,G 
# F sınıfı E den miras alsın 
# G sınıfı F den miras alsın
#her ikisi için nesne üret
#her ikisinden a değişkenini yazdır.

nesne1 = A()
nesne2 = B()
nesne3 = C()
print(nesne1.a)
print(nesne2.b)
print(nesne3.c)
nesne5 = F()
nesne6 = G()
print(nesne5.a)
print(nesne6.a)