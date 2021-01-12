# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/90531/Desktop/LABELLAB/LABELLAB.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainPage(object):
    def setupUi(self, MainPage):
        MainPage.setObjectName("MainPage")
        MainPage.resize(847, 769)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainPage.sizePolicy().hasHeightForWidth())
        MainPage.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        MainPage.setFont(font)
        MainPage.setStyleSheet("background-color:rgb(222, 255, 249);")
        self.centralwidget = QtWidgets.QWidget(MainPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.App = QtWidgets.QStackedWidget(self.centralwidget)
        self.App.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.App.sizePolicy().hasHeightForWidth())
        self.App.setSizePolicy(sizePolicy)
        self.App.setStyleSheet("background:url(:/images/images/bg.jpg)\n"
"")
        self.App.setObjectName("App")
        self.Uygulama = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Uygulama.sizePolicy().hasHeightForWidth())
        self.Uygulama.setSizePolicy(sizePolicy)
        self.Uygulama.setStyleSheet("background:url(:/images/images/bg.jpg)")
        self.Uygulama.setObjectName("Uygulama")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Uygulama)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 781, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AnaSayfa = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.AnaSayfa.setMinimumSize(QtCore.QSize(101, 50))
        self.AnaSayfa.setStyleSheet("#AnaSayfa\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#AnaSayfa:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.AnaSayfa.setObjectName("AnaSayfa")
        self.horizontalLayout.addWidget(self.AnaSayfa)
        self.Alinan_Ilanlar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Alinan_Ilanlar.sizePolicy().hasHeightForWidth())
        self.Alinan_Ilanlar.setSizePolicy(sizePolicy)
        self.Alinan_Ilanlar.setMinimumSize(QtCore.QSize(101, 50))
        self.Alinan_Ilanlar.setStyleSheet("#Alinan_Ilanlar\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#Alinan_Ilanlar:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.Alinan_Ilanlar.setObjectName("Alinan_Ilanlar")
        self.horizontalLayout.addWidget(self.Alinan_Ilanlar)
        self.Profil = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Profil.sizePolicy().hasHeightForWidth())
        self.Profil.setSizePolicy(sizePolicy)
        self.Profil.setMinimumSize(QtCore.QSize(101, 50))
        self.Profil.setStyleSheet("#Profil\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#Profil:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.Profil.setObjectName("Profil")
        self.horizontalLayout.addWidget(self.Profil)
        self.IlanVer = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IlanVer.sizePolicy().hasHeightForWidth())
        self.IlanVer.setSizePolicy(sizePolicy)
        self.IlanVer.setMinimumSize(QtCore.QSize(101, 50))
        self.IlanVer.setStyleSheet("#IlanVer\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#IlanVer:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.IlanVer.setObjectName("IlanVer")
        self.horizontalLayout.addWidget(self.IlanVer)
        self.Ilanlar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ilanlar.sizePolicy().hasHeightForWidth())
        self.Ilanlar.setSizePolicy(sizePolicy)
        self.Ilanlar.setMinimumSize(QtCore.QSize(101, 50))
        self.Ilanlar.setStyleSheet("#Ilanlar\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#Ilanlar:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.Ilanlar.setObjectName("Ilanlar")
        self.horizontalLayout.addWidget(self.Ilanlar)
        self.Veri_Etiket = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Veri_Etiket.sizePolicy().hasHeightForWidth())
        self.Veri_Etiket.setSizePolicy(sizePolicy)
        self.Veri_Etiket.setMinimumSize(QtCore.QSize(101, 50))
        self.Veri_Etiket.setStyleSheet("#Veri_Etiket\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#Veri_Etiket:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.Veri_Etiket.setObjectName("Veri_Etiket")
        self.horizontalLayout.addWidget(self.Veri_Etiket)
        self.Verilen_Ilanlar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Verilen_Ilanlar.sizePolicy().hasHeightForWidth())
        self.Verilen_Ilanlar.setSizePolicy(sizePolicy)
        self.Verilen_Ilanlar.setMinimumSize(QtCore.QSize(101, 50))
        self.Verilen_Ilanlar.setStyleSheet("#Verilen_Ilanlar\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#Verilen_Ilanlar:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.Verilen_Ilanlar.setObjectName("Verilen_Ilanlar")
        self.horizontalLayout.addWidget(self.Verilen_Ilanlar)
        self.Sayfalar = QtWidgets.QStackedWidget(self.Uygulama)
        self.Sayfalar.setGeometry(QtCore.QRect(10, 170, 761, 581))
        self.Sayfalar.setObjectName("Sayfalar")
        self.Ana_Sayfa = QtWidgets.QWidget()
        self.Ana_Sayfa.setObjectName("Ana_Sayfa")
        self.Cikis = QtWidgets.QPushButton(self.Ana_Sayfa)
        self.Cikis.setGeometry(QtCore.QRect(550, 520, 201, 41))
        self.Cikis.setStyleSheet("#Cikis\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#Cikis:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.Cikis.setObjectName("Cikis")
        self.Sayfalar.addWidget(self.Ana_Sayfa)
        self.AlinanIlanlar_Sayfa = QtWidgets.QWidget()
        self.AlinanIlanlar_Sayfa.setObjectName("AlinanIlanlar_Sayfa")
        self.label_4 = QtWidgets.QLabel(self.AlinanIlanlar_Sayfa)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 741, 71))
        self.label_4.setStyleSheet("font: 75 20pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: blue;\n"
"font: italic bold 25px;\n"
"min-width: 10em;\n"
"padding: 16px;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.AlinanIlanlar_Sayfa)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 130, 681, 196))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.A_I_Ara = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A_I_Ara.sizePolicy().hasHeightForWidth())
        self.A_I_Ara.setSizePolicy(sizePolicy)
        self.A_I_Ara.setStyleSheet("#A_I_Ara\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#A_I_Ara:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.A_I_Ara.setObjectName("A_I_Ara")
        self.horizontalLayout_3.addWidget(self.A_I_Ara)
        self.Upload = QtWidgets.QPushButton(self.AlinanIlanlar_Sayfa)
        self.Upload.setGeometry(QtCore.QRect(500, 520, 231, 41))
        self.Upload.setStyleSheet("#Upload\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#Upload:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.Upload.setObjectName("Upload")
        self.Sonuc_2 = QtWidgets.QTextEdit(self.AlinanIlanlar_Sayfa)
        self.Sonuc_2.setGeometry(QtCore.QRect(40, 340, 681, 151))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Sonuc_2.setFont(font)
        self.Sonuc_2.setStyleSheet("#Sonuc_2\n"
"{\n"
"\n"
"background:rgb(255, 255, 255)\n"
"\n"
"}")
        self.Sonuc_2.setReadOnly(True)
        self.Sonuc_2.setObjectName("Sonuc_2")
        self.Sayfalar.addWidget(self.AlinanIlanlar_Sayfa)
        self.Profil_Sayfa = QtWidgets.QWidget()
        self.Profil_Sayfa.setObjectName("Profil_Sayfa")
        self.PP = QtWidgets.QLabel(self.Profil_Sayfa)
        self.PP.setGeometry(QtCore.QRect(40, 110, 241, 231))
        self.PP.setStyleSheet("#PP\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 5px;\n"
"border-radius: 30px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"")
        self.PP.setText("")
        self.PP.setObjectName("PP")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.Profil_Sayfa)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(390, 110, 361, 79))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.ad_bilgi = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.ad_bilgi.setEnabled(False)
        self.ad_bilgi.setStyleSheet("#ad_bilgi\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"")
        self.ad_bilgi.setObjectName("ad_bilgi")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ad_bilgi)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.soyad_bilgi = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.soyad_bilgi.setEnabled(False)
        self.soyad_bilgi.setStyleSheet("#soyad_bilgi\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"")
        self.soyad_bilgi.setObjectName("soyad_bilgi")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.soyad_bilgi)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.Profil_Sayfa)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(390, 260, 361, 37))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.mail_bilgi = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.mail_bilgi.setEnabled(False)
        self.mail_bilgi.setStyleSheet("#mail_bilgi\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"")
        self.mail_bilgi.setObjectName("mail_bilgi")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.mail_bilgi)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Profil_Sayfa)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(390, 200, 361, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.Profil_Sayfa)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(40, 460, 711, 81))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Verilmis_Ilan_Gor = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.Verilmis_Ilan_Gor.setStyleSheet("#Verilmis_Ilan_Gor\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#Verilmis_Ilan_Gor:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.Verilmis_Ilan_Gor.setObjectName("Verilmis_Ilan_Gor")
        self.horizontalLayout_4.addWidget(self.Verilmis_Ilan_Gor)
        self.Alinmis_Ilan_Gor = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.Alinmis_Ilan_Gor.setStyleSheet("#Alinmis_Ilan_Gor\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#Alinmis_Ilan_Gor:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.Alinmis_Ilan_Gor.setObjectName("Alinmis_Ilan_Gor")
        self.horizontalLayout_4.addWidget(self.Alinmis_Ilan_Gor)
        self.label_11 = QtWidgets.QLabel(self.Profil_Sayfa)
        self.label_11.setGeometry(QtCore.QRect(20, 30, 741, 71))
        self.label_11.setStyleSheet("font: 75 20pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: blue;\n"
"font: italic bold 25px;\n"
"min-width: 10em;\n"
"padding: 16px;")
        self.label_11.setObjectName("label_11")
        self.Change_Profile = QtWidgets.QPushButton(self.Profil_Sayfa)
        self.Change_Profile.setGeometry(QtCore.QRect(70, 350, 181, 51))
        self.Change_Profile.setStyleSheet("#Change_Profile\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 4em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#Change_Profile:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.Change_Profile.setObjectName("Change_Profile")
        self.formLayoutWidget_9 = QtWidgets.QWidget(self.Profil_Sayfa)
        self.formLayoutWidget_9.setGeometry(QtCore.QRect(390, 310, 361, 147))
        self.formLayoutWidget_9.setObjectName("formLayoutWidget_9")
        self.formLayout_9 = QtWidgets.QFormLayout(self.formLayoutWidget_9)
        self.formLayout_9.setContentsMargins(0, 0, 0, 0)
        self.formLayout_9.setObjectName("formLayout_9")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.AboutMe = QtWidgets.QPushButton(self.formLayoutWidget_9)
        self.AboutMe.setStyleSheet("#AboutMe\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 4em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#AboutMe:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.AboutMe.setObjectName("AboutMe")
        self.formLayout_9.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.AboutMe)
        self.Hakkimda = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Hakkimda.sizePolicy().hasHeightForWidth())
        self.Hakkimda.setSizePolicy(sizePolicy)
        self.Hakkimda.setMinimumSize(QtCore.QSize(101, 100))
        self.Hakkimda.setStyleSheet("#Hakkimda\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"")
        self.Hakkimda.setObjectName("Hakkimda")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Hakkimda)
        self.Sayfalar.addWidget(self.Profil_Sayfa)
        self.IlanVer_Sayfa = QtWidgets.QWidget()
        self.IlanVer_Sayfa.setObjectName("IlanVer_Sayfa")
        self.label_12 = QtWidgets.QLabel(self.IlanVer_Sayfa)
        self.label_12.setGeometry(QtCore.QRect(20, 50, 741, 71))
        self.label_12.setStyleSheet("font: 75 20pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: blue;\n"
"font: italic bold 25px;\n"
"min-width: 10em;\n"
"padding: 16px;")
        self.label_12.setObjectName("label_12")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.IlanVer_Sayfa)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(30, 150, 451, 191))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.Ilan_bilgi = QtWidgets.QTextEdit(self.formLayoutWidget_4)
        self.Ilan_bilgi.setStyleSheet("#Ilan_bilgi\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"")
        self.Ilan_bilgi.setObjectName("Ilan_bilgi")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Ilan_bilgi)
        self.formLayoutWidget_5 = QtWidgets.QWidget(self.IlanVer_Sayfa)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(30, 360, 451, 41))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayout_6 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.RBU_bilgi = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        self.RBU_bilgi.setStyleSheet("#RBU_bilgi\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"")
        self.RBU_bilgi.setObjectName("RBU_bilgi")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.RBU_bilgi)
        self.formLayoutWidget_6 = QtWidgets.QWidget(self.IlanVer_Sayfa)
        self.formLayoutWidget_6.setGeometry(QtCore.QRect(30, 420, 451, 41))
        self.formLayoutWidget_6.setObjectName("formLayoutWidget_6")
        self.formLayout_7 = QtWidgets.QFormLayout(self.formLayoutWidget_6)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.formLayout_7.setObjectName("formLayout_7")
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.STT = QtWidgets.QDateEdit(self.formLayoutWidget_6)
        self.STT.setStyleSheet("#STT\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"")
        self.STT.setObjectName("STT")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.STT)
        self.formLayoutWidget_7 = QtWidgets.QWidget(self.IlanVer_Sayfa)
        self.formLayoutWidget_7.setGeometry(QtCore.QRect(30, 470, 451, 41))
        self.formLayoutWidget_7.setObjectName("formLayoutWidget_7")
        self.formLayout_8 = QtWidgets.QFormLayout(self.formLayoutWidget_7)
        self.formLayout_8.setContentsMargins(0, 0, 0, 0)
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.VeriSeti_bilgi = QtWidgets.QLineEdit(self.formLayoutWidget_7)
        self.VeriSeti_bilgi.setStyleSheet("#VeriSeti_bilgi\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"")
        self.VeriSeti_bilgi.setObjectName("VeriSeti_bilgi")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.VeriSeti_bilgi)
        self.Ilan_btn = QtWidgets.QPushButton(self.IlanVer_Sayfa)
        self.Ilan_btn.setGeometry(QtCore.QRect(530, 120, 211, 361))
        self.Ilan_btn.setStyleSheet("#Ilan_btn\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 4em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#Ilan_btn:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.Ilan_btn.setObjectName("Ilan_btn")
        self.Sayfalar.addWidget(self.IlanVer_Sayfa)
        self.Ilanlar_Sayfa = QtWidgets.QWidget()
        self.Ilanlar_Sayfa.setObjectName("Ilanlar_Sayfa")
        self.label_17 = QtWidgets.QLabel(self.Ilanlar_Sayfa)
        self.label_17.setGeometry(QtCore.QRect(20, 40, 741, 71))
        self.label_17.setStyleSheet("font: 75 20pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: blue;\n"
"font: italic bold 25px;\n"
"min-width: 10em;\n"
"padding: 16px;")
        self.label_17.setObjectName("label_17")
        self.Yenile = QtWidgets.QPushButton(self.Ilanlar_Sayfa)
        self.Yenile.setGeometry(QtCore.QRect(570, 120, 171, 41))
        self.Yenile.setStyleSheet("#Yenile\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#Yenile:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.Yenile.setObjectName("Yenile")
        self.formLayoutWidget_8 = QtWidgets.QWidget(self.Ilanlar_Sayfa)
        self.formLayoutWidget_8.setGeometry(QtCore.QRect(30, 170, 711, 481))
        self.formLayoutWidget_8.setObjectName("formLayoutWidget_8")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_8)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.Ilan_Al1 = QtWidgets.QPushButton(self.formLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ilan_Al1.sizePolicy().hasHeightForWidth())
        self.Ilan_Al1.setSizePolicy(sizePolicy)
        self.Ilan_Al1.setStyleSheet("#Ilan_Al1\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#Ilan_Al1:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.Ilan_Al1.setObjectName("Ilan_Al1")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Ilan_Al1)
        self.Ilan_Al2 = QtWidgets.QPushButton(self.formLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ilan_Al2.sizePolicy().hasHeightForWidth())
        self.Ilan_Al2.setSizePolicy(sizePolicy)
        self.Ilan_Al2.setStyleSheet("#Ilan_Al2\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#Ilan_Al2:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.Ilan_Al2.setObjectName("Ilan_Al2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Ilan_Al2)
        self.Ilan_Al3 = QtWidgets.QPushButton(self.formLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ilan_Al3.sizePolicy().hasHeightForWidth())
        self.Ilan_Al3.setSizePolicy(sizePolicy)
        self.Ilan_Al3.setStyleSheet("#Ilan_Al3\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#Ilan_Al3:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.Ilan_Al3.setObjectName("Ilan_Al3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Ilan_Al3)
        self.Ilan_Al4 = QtWidgets.QPushButton(self.formLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ilan_Al4.sizePolicy().hasHeightForWidth())
        self.Ilan_Al4.setSizePolicy(sizePolicy)
        self.Ilan_Al4.setStyleSheet("#Ilan_Al4\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#Ilan_Al4:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.Ilan_Al4.setObjectName("Ilan_Al4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Ilan_Al4)
        self.Ilan_Al5 = QtWidgets.QPushButton(self.formLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ilan_Al5.sizePolicy().hasHeightForWidth())
        self.Ilan_Al5.setSizePolicy(sizePolicy)
        self.Ilan_Al5.setStyleSheet("#Ilan_Al5\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#Ilan_Al5:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.Ilan_Al5.setObjectName("Ilan_Al5")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Ilan_Al5)
        self.Ilan_1 = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ilan_1.sizePolicy().hasHeightForWidth())
        self.Ilan_1.setSizePolicy(sizePolicy)
        self.Ilan_1.setMaximumSize(QtCore.QSize(16777215, 75))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Ilan_1.setFont(font)
        self.Ilan_1.setStyleSheet("background:rgb(255,255,255);")
        self.Ilan_1.setObjectName("Ilan_1")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Ilan_1)
        self.Ilan_2 = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ilan_2.sizePolicy().hasHeightForWidth())
        self.Ilan_2.setSizePolicy(sizePolicy)
        self.Ilan_2.setMaximumSize(QtCore.QSize(16777215, 75))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Ilan_2.setFont(font)
        self.Ilan_2.setStyleSheet("background:rgb(255,255,255);")
        self.Ilan_2.setObjectName("Ilan_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Ilan_2)
        self.Ilan_3 = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ilan_3.sizePolicy().hasHeightForWidth())
        self.Ilan_3.setSizePolicy(sizePolicy)
        self.Ilan_3.setMaximumSize(QtCore.QSize(16777215, 75))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Ilan_3.setFont(font)
        self.Ilan_3.setStyleSheet("background:rgb(255,255,255);")
        self.Ilan_3.setObjectName("Ilan_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Ilan_3)
        self.Ilan_4 = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ilan_4.sizePolicy().hasHeightForWidth())
        self.Ilan_4.setSizePolicy(sizePolicy)
        self.Ilan_4.setMaximumSize(QtCore.QSize(16777215, 75))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Ilan_4.setFont(font)
        self.Ilan_4.setStyleSheet("background:rgb(255,255,255);")
        self.Ilan_4.setObjectName("Ilan_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Ilan_4)
        self.Ilan_5 = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.Ilan_5.setMaximumSize(QtCore.QSize(16777215, 75))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Ilan_5.setFont(font)
        self.Ilan_5.setStyleSheet("background:rgb(255,255,255);")
        self.Ilan_5.setObjectName("Ilan_5")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Ilan_5)
        self.Sayfalar.addWidget(self.Ilanlar_Sayfa)
        self.VeriEtiket_Sayfa = QtWidgets.QWidget()
        self.VeriEtiket_Sayfa.setObjectName("VeriEtiket_Sayfa")
        self.label_18 = QtWidgets.QLabel(self.VeriEtiket_Sayfa)
        self.label_18.setGeometry(QtCore.QRect(20, 30, 741, 71))
        self.label_18.setStyleSheet("font: 75 20pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: blue;\n"
"font: italic bold 25px;\n"
"min-width: 10em;\n"
"padding: 16px;")
        self.label_18.setObjectName("label_18")
        self.label_20 = QtWidgets.QLabel(self.VeriEtiket_Sayfa)
        self.label_20.setGeometry(QtCore.QRect(20, 160, 741, 71))
        self.label_20.setStyleSheet("font: 75 20pt \"Times New Roman\";\n"
"\n"
"\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: white;\n"
"font: italic bold 25px;\n"
"min-width: 10em;\n"
"padding: 16px;")
        self.label_20.setObjectName("label_20")
        self.labelimg_btn = QtWidgets.QPushButton(self.VeriEtiket_Sayfa)
        self.labelimg_btn.setGeometry(QtCore.QRect(170, 250, 411, 81))
        self.labelimg_btn.setStyleSheet("#labelimg_btn\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 40px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#labelimg_btn:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.labelimg_btn.setObjectName("labelimg_btn")
        self.Sayfalar.addWidget(self.VeriEtiket_Sayfa)
        self.VerilenIlanlar_Sayfa = QtWidgets.QWidget()
        self.VerilenIlanlar_Sayfa.setObjectName("VerilenIlanlar_Sayfa")
        self.label_36 = QtWidgets.QLabel(self.VerilenIlanlar_Sayfa)
        self.label_36.setGeometry(QtCore.QRect(20, 30, 741, 71))
        self.label_36.setStyleSheet("font: 75 20pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: blue;\n"
"font: italic bold 25px;\n"
"min-width: 10em;\n"
"padding: 16px;")
        self.label_36.setObjectName("label_36")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.VerilenIlanlar_Sayfa)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(40, 130, 681, 196))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.VerIlCombobox = QtWidgets.QComboBox(self.horizontalLayoutWidget_7)
        self.VerIlCombobox.setObjectName("VerIlCombobox")
        self.horizontalLayout_7.addWidget(self.VerIlCombobox)
        self.V_I_Ara = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.V_I_Ara.sizePolicy().hasHeightForWidth())
        self.V_I_Ara.setSizePolicy(sizePolicy)
        self.V_I_Ara.setStyleSheet("#V_I_Ara\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#V_I_Ara:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.V_I_Ara.setObjectName("V_I_Ara")
        self.horizontalLayout_7.addWidget(self.V_I_Ara)
        self.Download = QtWidgets.QPushButton(self.VerilenIlanlar_Sayfa)
        self.Download.setGeometry(QtCore.QRect(500, 520, 231, 41))
        self.Download.setStyleSheet("#Download\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#Download:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}")
        self.Download.setObjectName("Download")
        self.Sonuc_3 = QtWidgets.QTextEdit(self.VerilenIlanlar_Sayfa)
        self.Sonuc_3.setGeometry(QtCore.QRect(40, 340, 681, 151))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Sonuc_3.setFont(font)
        self.Sonuc_3.setAutoFillBackground(True)
        self.Sonuc_3.setStyleSheet("#Sonuc_3\n"
"{\n"
"\n"
"background:rgb(255, 255, 255)\n"
"\n"
"}")
        self.Sonuc_3.setReadOnly(True)
        self.Sonuc_3.setObjectName("Sonuc_3")
        self.Sayfalar.addWidget(self.VerilenIlanlar_Sayfa)
        self.App.addWidget(self.Uygulama)
        self.Giris = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Giris.sizePolicy().hasHeightForWidth())
        self.Giris.setSizePolicy(sizePolicy)
        self.Giris.setStyleSheet("#Giris\n"
"{\n"
"    border-image:url(:/images/images/bg.jpg);\n"
"}")
        self.Giris.setObjectName("Giris")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Giris)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.Giris)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTabletTracking(False)
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setAcceptDrops(False)
        self.label.setStyleSheet("background:url(:/images/images/bg.jpg)")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(300, 100, 300, 500)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.mail_ledit = QtWidgets.QLineEdit(self.Giris)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mail_ledit.sizePolicy().hasHeightForWidth())
        self.mail_ledit.setSizePolicy(sizePolicy)
        self.mail_ledit.setStyleSheet("#mail_ledit\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"")
        self.mail_ledit.setObjectName("mail_ledit")
        self.gridLayout_4.addWidget(self.mail_ledit, 0, 2, 1, 2)
        self.sifre_ledit = QtWidgets.QLineEdit(self.Giris)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sifre_ledit.sizePolicy().hasHeightForWidth())
        self.sifre_ledit.setSizePolicy(sizePolicy)
        self.sifre_ledit.setStyleSheet("#sifre_ledit\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}")
        self.sifre_ledit.setObjectName("sifre_ledit")
        self.gridLayout_4.addWidget(self.sifre_ledit, 1, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.Giris)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:url(:/images/LABELLAB/images/bg.jpg);")
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 1, 1, 1)
        self.Giris_btn = QtWidgets.QPushButton(self.Giris)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Giris_btn.sizePolicy().hasHeightForWidth())
        self.Giris_btn.setSizePolicy(sizePolicy)
        self.Giris_btn.setMinimumSize(QtCore.QSize(101, 0))
        self.Giris_btn.setStyleSheet("#Giris_btn\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#Giris_btn:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}\n"
"\n"
"")
        self.Giris_btn.setObjectName("Giris_btn")
        self.gridLayout_4.addWidget(self.Giris_btn, 2, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.Giris)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background:url(:/images/LABELLAB/images/bg.jpg);")
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 1, 1, 1)
        self.KayitOl_btn = QtWidgets.QPushButton(self.Giris)
        self.KayitOl_btn.setStyleSheet("#KayitOl_btn\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#KayitOl_btn:pressed\n"
"{\n"
"    background-color:rgb(255,255,255);\n"
"}\n"
"\n"
"")
        self.KayitOl_btn.setObjectName("KayitOl_btn")
        self.gridLayout_4.addWidget(self.KayitOl_btn, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 3, 1, 1, 1)
        self.App.addWidget(self.Giris)
        self.KayitOlPage = QtWidgets.QWidget()
        self.KayitOlPage.setObjectName("KayitOlPage")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.KayitOlPage)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(250, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setTabletTracking(False)
        self.label_5.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_5.setAcceptDrops(False)
        self.label_5.setStyleSheet("background:url(:/images/images/bg.jpg)")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.formLayoutWidget = QtWidgets.QWidget(self.KayitOlPage)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 110, 781, 651))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.GeriDon_btn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.GeriDon_btn.setStyleSheet("#GeriDon_btn\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#GeriDon_btn:pressed\n"
"{\n"
"background:white;\n"
"}\n"
"")
        self.GeriDon_btn.setObjectName("GeriDon_btn")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.GeriDon_btn)
        self.ad_linedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ad_linedit.setStyleSheet("#ad_linedit\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"")
        self.ad_linedit.setObjectName("ad_linedit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ad_linedit)
        self.Ad = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Ad.setFont(font)
        self.Ad.setStyleSheet("background:url(:/images/images/bg.jpg)")
        self.Ad.setObjectName("Ad")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Ad)
        self.Soyad = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Soyad.setFont(font)
        self.Soyad.setStyleSheet("background:url(:/images/images/bg.jpg)")
        self.Soyad.setObjectName("Soyad")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Soyad)
        self.soyad_linedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.soyad_linedit.setStyleSheet("#soyad_linedit\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"")
        self.soyad_linedit.setObjectName("soyad_linedit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.soyad_linedit)
        self.Mail = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Mail.setFont(font)
        self.Mail.setStyleSheet("background:url(:/images/images/bg.jpg)")
        self.Mail.setObjectName("Mail")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Mail)
        self.mail_linedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.mail_linedit.setStyleSheet("#mail_linedit\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"")
        self.mail_linedit.setObjectName("mail_linedit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.mail_linedit)
        self.Sifre = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Sifre.setFont(font)
        self.Sifre.setStyleSheet("background:url(:/images/images/bg.jpg)")
        self.Sifre.setObjectName("Sifre")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Sifre)
        self.sifre_linedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.sifre_linedit.setStyleSheet("#sifre_linedit\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"")
        self.sifre_linedit.setObjectName("sifre_linedit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sifre_linedit)
        self.sifreonay_linedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.sifreonay_linedit.setStyleSheet("#sifreonay_linedit\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"")
        self.sifreonay_linedit.setObjectName("sifreonay_linedit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sifreonay_linedit)
        self.SifreConfirm = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.SifreConfirm.setFont(font)
        self.SifreConfirm.setStyleSheet("background:url(:/images/images/bg.jpg)")
        self.SifreConfirm.setObjectName("SifreConfirm")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.SifreConfirm)
        self.Onay = QtWidgets.QPushButton(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Onay.sizePolicy().hasHeightForWidth())
        self.Onay.setSizePolicy(sizePolicy)
        self.Onay.setStyleSheet("#Onay\n"
"{\n"
"font: 75 14pt \"Times New Roman\";\n"
"\n"
"background: beige;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: blue;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"\n"
"}\n"
"#Onay:pressed\n"
"{\n"
"background:white;\n"
"}\n"
"")
        self.Onay.setObjectName("Onay")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Onay)
        self.App.addWidget(self.KayitOlPage)
        self.gridLayout.addWidget(self.App, 0, 0, 1, 1)
        MainPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainPage)
        self.App.setCurrentIndex(0)
        self.Sayfalar.setCurrentIndex(1)
        self.AnaSayfa.clicked.connect(MainPage.AnaSayfaGit)
        self.Alinan_Ilanlar.clicked.connect(MainPage.AlinanIlanlarGit)
        self.Profil.clicked.connect(MainPage.ProfilGit)
        self.IlanVer.clicked.connect(MainPage.IlanVerGit)
        self.Ilanlar.clicked.connect(MainPage.IlanlarGit)
        self.Veri_Etiket.clicked.connect(MainPage.VerisetiEtiketGit)
        self.Verilen_Ilanlar.clicked.connect(MainPage.VerilenIlanlarGit)
        self.KayitOl_btn.clicked.connect(MainPage.KayitOlGit)
        self.GeriDon_btn.clicked.connect(MainPage.GiriseGit)
        self.Giris_btn.clicked.connect(MainPage.Giris_clicked)
        self.labelimg_btn.clicked.connect(MainPage.Labelimg)
        self.Cikis.clicked.connect(MainPage.Cikis)
        self.Onay.clicked.connect(MainPage.kayit_ol)
        self.AboutMe.clicked.connect(MainPage.hakkimda_gir)
        self.Ilan_btn.clicked.connect(MainPage.ilan_ver)
        self.Ilan_Al1.clicked.connect(MainPage.Ilan_Al1)
        self.Ilan_Al2.clicked.connect(MainPage.Ilan_Al2)
        self.Ilan_Al3.clicked.connect(MainPage.Ilan_Al3)
        self.Ilan_Al4.clicked.connect(MainPage.Ilan_Al4)
        self.Ilan_Al5.clicked.connect(MainPage.Ilan_Al5)
        self.A_I_Ara.clicked.connect(MainPage.ilan_sec)
        self.V_I_Ara.clicked.connect(MainPage.ilan_sec2)
        self.Download.clicked.connect(MainPage.ilan_tamamlandi)
        self.Upload.clicked.connect(MainPage.ilan_tamamlandi)
        QtCore.QMetaObject.connectSlotsByName(MainPage)

    def retranslateUi(self, MainPage):
        _translate = QtCore.QCoreApplication.translate
        MainPage.setWindowTitle(_translate("MainPage", "LABELLAB"))
        self.AnaSayfa.setText(_translate("MainPage", "AnaSayfa"))
        self.Alinan_Ilanlar.setText(_translate("MainPage", "Alınan İlanlar"))
        self.Profil.setText(_translate("MainPage", "Profil"))
        self.IlanVer.setText(_translate("MainPage", "İlan Ver"))
        self.Ilanlar.setText(_translate("MainPage", "İlanlar"))
        self.Veri_Etiket.setText(_translate("MainPage", "Veriseti Etiketle"))
        self.Verilen_Ilanlar.setText(_translate("MainPage", "Verilen İlanlar"))
        self.Cikis.setText(_translate("MainPage", "Çıkış"))
        self.label_4.setText(_translate("MainPage", "ALINAN İLANLAR"))
        self.A_I_Ara.setText(_translate("MainPage", "Seç"))
        self.Upload.setText(_translate("MainPage", "İlanı Tamamla"))
        self.label_7.setText(_translate("MainPage", "Ad:           "))
        self.label_8.setText(_translate("MainPage", "Soyad:"))
        self.label_10.setText(_translate("MainPage", "Mail:         "))
        self.label_9.setText(_translate("MainPage", "İLETİŞİM BİLGİLERİ"))
        self.Verilmis_Ilan_Gor.setText(_translate("MainPage", "Verilmiş İlanlar"))
        self.Alinmis_Ilan_Gor.setText(_translate("MainPage", "Alınmış İlanlar"))
        self.label_11.setText(_translate("MainPage", "PROFİL"))
        self.Change_Profile.setText(_translate("MainPage", "Profil Fotoğrafı Değiştir"))
        self.label_6.setText(_translate("MainPage", "Hakkımda:"))
        self.AboutMe.setText(_translate("MainPage", "Onayla"))
        self.label_12.setText(_translate("MainPage", "İLAN VER"))
        self.label_13.setText(_translate("MainPage", "İlan:"))
        self.Ilan_bilgi.setHtml(_translate("MainPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:14px; font-weight:600; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400;\"><br /></p></body></html>"))
        self.label_14.setText(_translate("MainPage", "Resim Başına Ödenecek Ücret:"))
        self.label_15.setText(_translate("MainPage", "Son Teslim Tarihi                    :"))
        self.label_16.setText(_translate("MainPage", "Veri Seti                                  :"))
        self.Ilan_btn.setText(_translate("MainPage", "İlanı Ver"))
        self.label_17.setText(_translate("MainPage", "İLANLAR"))
        self.Yenile.setText(_translate("MainPage", "Yenile"))
        self.Ilan_Al1.setText(_translate("MainPage", "İlan Al"))
        self.Ilan_Al2.setText(_translate("MainPage", "İlan Al"))
        self.Ilan_Al3.setText(_translate("MainPage", "İlan Al"))
        self.Ilan_Al4.setText(_translate("MainPage", "İlan Al"))
        self.Ilan_Al5.setText(_translate("MainPage", "İlan Al"))
        self.label_18.setText(_translate("MainPage", "VERİ ETİKET"))
        self.label_20.setText(_translate("MainPage", "Labelimg ile veri etiketlemeye hemen başlayın!"))
        self.labelimg_btn.setText(_translate("MainPage", "Labelimg"))
        self.label_36.setText(_translate("MainPage", "VERİLEN İLANLAR"))
        self.V_I_Ara.setText(_translate("MainPage", "Seç"))
        self.Download.setText(_translate("MainPage", "İlanı Tamamla"))
        self.label.setText(_translate("MainPage", "LABELLAB"))
        self.label_2.setText(_translate("MainPage", "Mail"))
        self.Giris_btn.setText(_translate("MainPage", "Giriş"))
        self.label_3.setText(_translate("MainPage", "Şifre:"))
        self.KayitOl_btn.setText(_translate("MainPage", "Kayit Ol"))
        self.label_5.setText(_translate("MainPage", "LABELLAB"))
        self.GeriDon_btn.setText(_translate("MainPage", "Geri Dön"))
        self.Ad.setText(_translate("MainPage", "Ad:"))
        self.Soyad.setText(_translate("MainPage", "Soyad:"))
        self.Mail.setText(_translate("MainPage", "Mail:"))
        self.Sifre.setText(_translate("MainPage", "Sifre:"))
        self.SifreConfirm.setText(_translate("MainPage", "Sifreyi Onayla:"))
        self.Onay.setText(_translate("MainPage", "Onay"))

import images_rc
