from abc import *

class Suclu(ABC):
    @abstractmethod
    def isledigiSuc(self):
        pass

class Kırmızı(ABC):
    def isledigiSuc(self):
        print("Adam Bıcaklama")

nesne1 = Kırmızı()

from abc import *

class GeometricSekil(ABC):
    def Area (self):
        pass
    
class Square(GeometricSekil):
    def Area(self):
        print("karenin alanı")
        
        
class Triangle(GeometricSekil):
    def Area(self):
        print("Üçgenin alanı")
        
        
nesne1=Square()
nesne2=Triangle()