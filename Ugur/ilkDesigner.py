import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5 import uic

class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Ediz\PyQt5\ilkarayuz.ui",self)
        self.Goster()
    
    def Goster(self):
        self.btGonder.clicked.connect(self.Tiklandi)
        self.hakkinda.triggered.connect(self.Hakkinda)
        self.show()

    def Tiklandi(self):
        self.txtPass.setText(self.txtUser.text())

    def Hakkinda(self):
        QMessageBox.information(self,"Bilgi","İbrahim EDİZ")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())