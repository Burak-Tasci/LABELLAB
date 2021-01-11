from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from LABELLAB_python import Ui_MainPage
import subprocess

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainPage()
        self.ui.setupUi(self)
        self.setFixedSize(815,756)
        self.ui.App.setCurrentIndex(1)
        self.ui.Sayfalar.setCurrentIndex(0)

    def AnaSayfaGit(self):
        self.ui.Sayfalar.setCurrentIndex(0)
    def AlinanIlanlarGit(self):
        self.ui.Sayfalar.setCurrentIndex(1)
    def ProfilGit(self):
        self.ui.Sayfalar.setCurrentIndex(2)
    def IlanVerGit(self):
        self.ui.Sayfalar.setCurrentIndex(3)
    def IlanlarGit(self):
        self.ui.Sayfalar.setCurrentIndex(4)
    def VerisetiEtiketGit(self):
        self.ui.Sayfalar.setCurrentIndex(5)
    def VerilenIlanlarGit(self):
        self.ui.Sayfalar.setCurrentIndex(6)
    def KayitOlGit(self):
        self.ui.App.setCurrentIndex(2)
    def GiriseGit(self):
        self.ui.App.setCurrentIndex(1)
    def Giris_clicked(self):
        self.ui.App.setCurrentIndex(0)
        self.AnaSayfaGit()
    def Labelimg(self):
        subprocess.Popen("python labelimg.py")
    def Cikis(self):
        self.ui.App.setCurrentIndex(1)
    def Fonksiyon(self):
        print("Burak")



app = QApplication([])
window = Window()
window.show()
app.exec()

