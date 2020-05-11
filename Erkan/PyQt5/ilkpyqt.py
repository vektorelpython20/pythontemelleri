import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QCheckBox,QLineEdit

class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        self.baslik="Örnek 1"
        self.sol=100
        self.ust=100
        self.width=640
        self.height=480
        self.Goster()
    
    def Goster(self):
        self.setWindowTitle(self.baslik)
        self.setGeometry(self.sol,self.ust,self.width,self.height)

        dugme=QPushButton("Tıkla",self)
        dugme.move(100,70)
        dugme.clicked.connect(self.Tiklandi)
        self.textBox=QLineEdit(self)
        self.textBox.move(30,30)
        self.textBox.resize(240,40)
        self.secim=QCheckBox("Güzel",self)
        self.secim.move(120,100)
        
#####################################################
        self.show()

    def Tiklandi(self):
        if self.secim.checkState:
            print(self.textBox.text())
        else:
            print("İşaretli değil")



if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=Uygulama()
    sys.exit(app.exec_())
