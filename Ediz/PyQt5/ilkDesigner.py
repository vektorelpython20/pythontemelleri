import sys
from PyQt5.QtWidgets import QApplication,QMainWindow

class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Goster()
    
    def Goster(self):
        self.show()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())