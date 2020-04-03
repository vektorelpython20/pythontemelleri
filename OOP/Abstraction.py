from abc import * 

class Hayvan(ABC):
    @abstractmethod
    def ses_cikar(self):
        pass

class Kedi(Hayvan):
    def ses_cikar(self):
        print("Miyav")


class Kopek(Hayvan):
    def ses_cikar(self):
        print("Hav")


nesne1 = Kedi()
nesne2 = Kopek()