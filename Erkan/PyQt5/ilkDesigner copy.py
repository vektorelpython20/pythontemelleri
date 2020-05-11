import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QLineEdit
from PyQt5 import uic

class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        #2.
        uic.loadUi(r"Erkan\PyQt5\ilkarayuz.ui",self)
        #3.
        # self.win = uic.loadUi(r"Ediz\PyQt5\ilkarayuz.ui")
        # self.win.btGonder
        self.Goster()
    
    def Goster(self):
        self.btGonder.clicked.connect(self.Tiklandi)
        self.hakkinda.triggered.connect(self.Hakkinda)
        self.txtUser.textChanged.connect(self.GirisKontrol)
        self.txtGiris.textChanged.connect(self.GirisKontrol)
        self.show()



    def GirisKontrol(self):
        gelen = self.sender()
        adi = gelen.objectName()
        yazi = gelen.text()
        sonuc = ""
        if adi == "txtGiris":
            for item in yazi:
                if item.isdigit():
                    self.statusBar().showMessage(" Sadece Harf Girilir")
                else:
                    sonuc += item.upper()
                
        elif adi == "txtUser":
            for item in yazi:
                if item.isdigit():
                    sonuc += item
                    self.statusBar().showMessage("")
                else:
                    self.statusBar().showMessage("Harf Girilmez")
        gelen.setText(sonuc)


    def Tiklandi(self):
        self.txtPass.setText(self.txtUser.text())

    def Hakkinda(self):
        QMessageBox.information(self,"Bilgi","İbrahim EDİZ")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())