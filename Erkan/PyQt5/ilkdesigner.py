import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QCheckBox,QLineEdit
from PyQt5 import uic
class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Erkan\ilkarayuz.ui",self)
        self.Goster()
        
    def Goster(self):
        self.btGonder.clicked.connect(self.tiklandi)
        self.show()

    def tiklandi(self):
        self.txtPass.setText(self.txtUser.text())

if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=Uygulama()
    sys.exit(app.exec_())
