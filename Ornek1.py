# class DeadPool:
#     def __init__(self,adi,guc,saglik):
#         self.adi = adi
#         self.guc = guc
#         self.saglik = saglik

#     def Vurus(self):
#         return self.guc
    
#     def Darbe(self,darbe):
#         self.saglik -= darbe

# class IronMan:
#     def __init__(self,adi,guc,saglik):
#         self.adi = adi
#         self.guc = guc
#         self.saglik = saglik

#     def Vurus(self):
#         return self.guc
    
#     def Darbe(self,darbe):
#         self.saglik -= darbe

# P1 = DeadPool("Deadpool",200,1000)
# P2 = IronMan("IronMan",150,2000)

from random import choice as ch
class MarvelHero:
    def __init__(self,adi,guc,saglik):
        self.adi = adi
        self.guc = guc
        self.saglik = saglik
        self.__gizli = 5
        self.__gizliBirikme = 0

    def Vurus(self):
        return self.guc
    
    def Vurus2(self):
        return self.guc//2

    def Vurus3(self):
        return self.guc//3
    
    def Darbe(self,darbe):
        self.saglik -= darbe

    def Savunma(self,darbe):
        self.saglik -= darbe//3
    
    def OfansSec(self,param=0):
        liste = [self.Vurus,self.Vurus2,self.Vurus3]
        self.__gizliBirikme += 1
        if param:
            return self.HareketSecim(liste)()
        return ch(liste)()

    def DefansSec(self,darbe,param=0):
        liste = [self.Darbe,self.Savunma]
        if self.__gizliBirikme == self.__gizli:
            self.__gizliBirikme = 0
            liste.append(self.Yetenek)
        if param:
            return self.HareketSecim(liste)(darbe)
        return ch(liste)(darbe)

    def HareketSecim(self,liste):
        for item in liste:
            print(item.__name__)
        return liste[int(input("Hareketi Seç"))-1]

    def Yetenek(self,darbe=0):
        pass


class Deadpool(MarvelHero):
    def __init__(self):
        super().__init__("Deadpool",200,1500)
        self.__gizli = 10
    
    def Yetenek(self,darbe=0):
        self.saglik = 1500
    
class IronMan(MarvelHero):
    def __init__(self):
        super().__init__("IronMan",200,2000)

class Thanos(MarvelHero):
    def __init__(self):
        super().__init__("Thanos",300,2500)

class Thor(MarvelHero):
    def __init__(self):
        super().__init__("Thor",400,1700)
    
    def Darbe2(self,darbe):
        self.saglik += darbe//4
    
    def Yetenek(self,darbe):
        self.Darbe2(darbe)

class SpiderMan(MarvelHero):
    def __init__(self):
        super().__init__("SpiderMan",300,2000)

class Hulk(MarvelHero):
    def __init__(self):
        super().__init__("Hulk",250,2000)

def PCvsPC():
    Karlist = [Deadpool,IronMan,Thanos,Thor,SpiderMan,Hulk]
    P1 = ch(Karlist)()
    P2 = ch(Karlist)()
    print(f"P1:{P1.adi} vs P2:{P2.adi}")
    import time
    while P1.saglik > 0 and P2.saglik > 0:
        P2.DefansSec(P1.OfansSec())
        time.sleep(1)
        P1.DefansSec(P2.OfansSec())
        print(f"P1:{P1.adi} Sağlık:{P1.saglik} vs P2:{P2.adi} Sağlık:{P2.saglik}")
    else:
        if P1.saglik > P2.saglik:
            print(P1.adi,"kazandı")
        elif P1.saglik < P2.saglik:
            print(P2.adi,"kazandi")
        else:
            print("Berabere")

def USERvsPC():
    menu = """
    1-Deadpool
    2-IronMan
    3-Thanos
    4-Thor
    5-SpiderMan
    6-Hulk
    Karakteri Seçiniz :
    """
    secim = int(input(menu))
    Karlist = [Deadpool,IronMan,Thanos,Thor,SpiderMan,Hulk]
    P1 = Karlist[secim-1]()
    P2 = ch(Karlist)()
    print(f"P1:{P1.adi} vs P2:{P2.adi}")
    import time
    while P1.saglik > 0 and P2.saglik > 0:
        P2.DefansSec(P1.OfansSec(1))
        time.sleep(1)
        P1.DefansSec(P2.OfansSec(),1)
        print(f"P1:{P1.adi} Sağlık:{P1.saglik} vs P2:{P2.adi} Sağlık:{P2.saglik}")
    else:
        if P1.saglik > P2.saglik:
            print(P1.adi,"kazandı")
        elif P1.saglik < P2.saglik:
            print(P2.adi,"kazandi")
        else:
            print("Berabere")    

def USERvsUSER():
    menu = """
    1-Deadpool
    2-IronMan
    3-Thanos
    4-Thor
    5-SpiderMan
    6-Hulk
    Karakteri Seçiniz :
    """
    Karlist = [Deadpool,IronMan,Thanos,Thor,SpiderMan,Hulk]
    P1 = Karlist[int(input(menu+"Kullanıcı 1"))-1]()
    P2 = Karlist[int(input(menu+"Kullanıcı 2"))-1]()
    print(f"P1:{P1.adi} vs P2:{P2.adi}")
    import time
    while P1.saglik > 0 and P2.saglik > 0:
        P2.DefansSec(P1.OfansSec(1),1)
        time.sleep(1)
        P1.DefansSec(P2.OfansSec(1),1)
        print(f"P1:{P1.adi} Sağlık:{P1.saglik} vs P2:{P2.adi} Sağlık:{P2.saglik}")
    else:
        if P1.saglik > P2.saglik:
            print(P1.adi,"kazandı")
        elif P1.saglik < P2.saglik:
            print(P2.adi,"kazandi")
        else:
            print("Berabere")    

