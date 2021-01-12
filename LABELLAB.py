from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from LABELLAB_python import Ui_MainPage
import subprocess
import mysql.connector

mydb = mysql.connector.connect(host="34.70.195.155", user="fatih", password="bp2label", database="labellab")
ilan_ids = []
id = 0
al_ilanid = -1
ver_ilanid = -1
def id_belirle(e_posta):  # tamamlandı
    global id
    mycursor = mydb.cursor()
    sql = "SELECT user_id FROM user WHERE mail = %s"
    arama = (e_posta,)
    mycursor.execute(sql, arama, )
    id = mycursor.fetchall()
    id = id[0][0]
    id= int(id)
    return id
def ad_gor():# tamamlandı
    global id
    try:
        mycursor = mydb.cursor()
        sql = "SELECT name FROM user WHERE user_id = %s"
        temp_id = str(id)
        arama = (temp_id,)
        mycursor.execute(sql,arama)
        isim = mycursor.fetchall()
        isim= isim[0][0]
        return isim
    except(mysql.connector.errors.ProgrammingError):
        print("Aranan kişi bulunamadı.")
def soyad_gor():# tamamlandı
    global id
    try:
        mycursor = mydb.cursor()
        sql = "SELECT name FROM user WHERE user_id = %s"
        temp_id = str(id)
        arama = (temp_id,)
        mycursor.execute(sql, arama)
        s_isim= mycursor.fetchall()
        s_isim= s_isim[0][0]
        return s_isim
    except(mysql.connector.errors.ProgrammingError):
        print("Aranan kişi bulunamadı.")
def mail_gor():# tamamlandı
    global id
    try:
        mycursor = mydb.cursor()
        sql = "SELECT name FROM user WHERE user_id = %s"
        temp_id = str(id)
        arama = (temp_id,)
        mycursor.execute(sql, arama)
        mail = mycursor.fetchall()
        mail = mail[0][0]
        return mail
    except(mysql.connector.errors.ProgrammingError):
        print("Aranan kişi bulunamadı.")
def alinan_ilan_gor():#sayfaya eklenecek
    global id
    try:
        mycursor= mydb.cursor()
        sql = "SELECT taskmaster_id FROM taskmaster WHERE us_id = %s"
        temp_id = str(id)
        val = (temp_id,)
        mycursor.execute(sql,val)
        taskm = mycursor.fetchall()
        taskm = taskm[0][0]
        if(taskm != None ):
            sql = "SELECT deadline ,dataset_link ,cash_per_pic ,notice_text FROM notice WHERE tm_id = %s"
            s_taskm = str(taskm)
            arama = (s_taskm,)
            mycursor.execute(sql, arama)
            ilan= mycursor.fetchall()
            return ilan
        else :
            return "İlanınız bulunmamaktadır. "
    except(mysql.connector.errors.ProgrammingError):
        print("Size ait ilan bulunamadı.")#message box gelebilir
def verilen_ilan_gor():#sayfaya eklenecek
    global id
    try:
        mycursor= mydb.cursor()
        sql = "SELECT deadline ,dataset_link ,cash_per_pic ,notice_text FROM notice WHERE u_id = %s"
        temp_id = str(id)
        val = (temp_id,)
        mycursor.execute(sql,val)
        ilans = mycursor.fetchall()
        return ilans
    except(mysql.connector.errors.ProgrammingError):
        print("Size ait ilan bulunamadı.")#message box gelebilir

def ilan_gor():
    global id

    mycursor = mydb.cursor()
    sql ="SELECT  (notice_id) FROM notice"
    mycursor.execute(sql,)
    sayac = mycursor.fetchall()
    uzunluk = len(sayac)
    if (uzunluk == None):
        return -1
    else:
        sql = "SELECT  deadline ,dataset_link ,cash_per_pic ,notice_text,notice_id FROM notice ORDER BY notice_id DESC "
        mycursor.execute(sql)
        ilanlar = mycursor.fetchall()
        ilanlar = ilanlar[:5]
        return ilanlar
def ilan_al(ilan_id,kisi_id):
    global id
    mycursor= mydb.cursor()
    sql = " INSERT INTO taskmaster (not_id, us_id ) VALUES (%s, %s)"
    temp_id = str(kisi_id)
    ilan_id = str(ilan_id)
    val = (ilan_id, temp_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor_2 = mydb.cursor()
    sql = "SELECT taskmaster_id FROM taskmaster WHERE us_id= %s"
    arama = (id,)
    mycursor_2.execute(sql, arama)
    task_id = mycursor_2.fetchall()
    task_id=task_id[0][0]
    sql= "UPDATE notice SET tm_id = %s WHERE notice_id= %s"
    task_id= str(task_id)
    val = (task_id,ilan_id,)
    mycursor_2.execute(sql, val)
    mydb.commit()

class Window(QMainWindow):


    def __init__(self):
        global id
        super().__init__()
        self.ui = Ui_MainPage()
        self.ui.setupUi(self)
        self.setFixedSize(815,756)
        self.ui.App.setCurrentIndex(1)
        self.ui.Sayfalar.setCurrentIndex(0)



    def AnaSayfaGit(self):
        self.ui.Sayfalar.setCurrentIndex(0)
    def AlinanIlanlarGit(self):
        global al_ilanid
        texts = []
        alinan_ilanlar = list(alinan_ilan_gor())
        for i in range(len(alinan_ilanlar)):
            alinan_ilanlar[i] = list(alinan_ilanlar[i])

        textas  = str(alinan_ilanlar[0][-1])
        textas2 = str(alinan_ilanlar[1][-1])
        self.ui.comboBox.addItem(textas)
        self.ui.comboBox.addItem(textas2)
        self.ui.Sayfalar.setCurrentIndex(1)




    def ProfilGit(self):

        self.ui.ad_bilgi.setText(ad_gor())
        self.ui.soyad_bilgi.setText(soyad_gor())
        self.ui.mail_bilgi.setText(mail_gor())
        self.ui.Sayfalar.setCurrentIndex(2)
    def ilan_sec(self):
        global al_ilanid
        al_ilanid = self.ui.comboBox.currentIndex()
        print(al_ilanid)
        alinan_ilanlar = alinan_ilan_gor()
        alinan_ilanlar[al_ilanid] = list(alinan_ilanlar[al_ilanid])
        textas = "Son teslim tarihi: "+str(alinan_ilanlar[al_ilanid][-1]) +"  veriseti link:  "+ str(alinan_ilanlar[al_ilanid][-2])+"  resim başı ücret:  " + str(alinan_ilanlar[al_ilanid][-3]) +"  Açıklama:  "+ str(alinan_ilanlar[al_ilanid][-4])
        print(alinan_ilanlar)
        self.ui.Sonuc_2.setText(textas)
    def ilan_sec2(self):
        global ver_ilanid
        ver_ilanid = self.ui.VerIlCombobox.currentIndex()
        print(ver_ilanid)
        verilen_ilanlar = verilen_ilan_gor()
        verilen_ilanlar[ver_ilanid] = list(verilen_ilanlar[ver_ilanid])
        textas = "Son teslim tarihi: " + str(verilen_ilanlar[ver_ilanid][-1]) + "  veriseti link:  " + str(
            verilen_ilanlar[ver_ilanid][-2]) + "  resim başı ücret:  " + str(
            verilen_ilanlar[ver_ilanid][-3]) + "  Açıklama:  " + str(verilen_ilanlar[ver_ilanid][-4])

        print(verilen_ilanlar)
        self.ui.Sonuc_3.setText(textas)
    def ilan_tamamlandi(self):
        QMessageBox.about(self, "Başarılı", "İlan Tamamlandı!!!")


    def ilan_ver(self):
        global id
        if(self.ui.STT.text() == None or self.ui.RBU_bilgi.text() == None or self.ui.Ilan_bilgi.toPlainText() == None or
        self.ui.VeriSeti_bilgi.text() == None):
            QMessageBox.about(self, "Warning!", "Boşluk Var!!!")
        else:
            try:
                mycursor = mydb.cursor()
                sql = "INSERT INTO notice (notice_text, deadline, cash_per_pic, dataset_link, u_id) VALUES (%s, %s, %s, %s, %s)"
                veri_text = self.ui.Ilan_bilgi.toPlainText()
                stt = self.ui.STT.text()
                date = stt.split(".")
                ma_date = ""
                ma_date = date[-1] + "-" + date[-2] + "-" + date[-3]
                para = self.ui.RBU_bilgi.text()
                link = self.ui.VeriSeti_bilgi.text()
                #temp_id = str(id)
                val = (veri_text, ma_date, para, link, id,)
                mycursor.execute(sql, val)
                mydb.commit()
            except(mysql.connector.errors.ProgrammingError):
                QMessageBox.about(self, "Warning!", "Giriş Başarısız!!!")

    def IlanVerGit(self):
        self.ui.Sayfalar.setCurrentIndex(3)
    def IlanlarGit(self):
        ilan_id=[]
        object_array = [self.ui.Ilan_1,self.ui.Ilan_2,self.ui.Ilan_3,self.ui.Ilan_4,self.ui.Ilan_5]
        ilanlar = ilan_gor()
        for j in ilanlar:
            ilan_id.append(j[4])
        object_array = iter(object_array)
        x = next(object_array)
        for ilan in ilanlar:
            try:
                text = "son teslim tarihi:  "+str(ilan[0]) +"  ilan linki:  "+ str(ilan[1]) +"  resim başı ucret:  "+str(ilan[2]) +"  ilan:  "+ str(ilan[3])
                ilan_ids.append(ilan[-1])
                x.setText(text)
                x = next(object_array)
            except StopIteration:
                pass

        self.ui.Sayfalar.setCurrentIndex(4)

    def Ilan_Al1(self):
        global id
        global ilan_ids
        asil_id = ilan_ids[0]
        ilan_al(asil_id,id)
        QMessageBox.about(self, "Başarılı", "İlan Alındı!!!")

    def Ilan_Al2(self):
        global id
        global ilan_ids
        asil_id = ilan_ids[1]
        ilan_al(asil_id, id)
        QMessageBox.about(self, "Başarılı", "İlan Alındı!!!")

    def Ilan_Al3(self):
        global id
        global ilan_ids
        asil_id = ilan_ids[2]
        ilan_al(asil_id, id)
        QMessageBox.about(self, "Başarılı", "İlan Alındı!!!")

    def Ilan_Al4(self):
        global id
        global ilan_ids
        asil_id = ilan_ids[3]
        ilan_al(asil_id, id)
        QMessageBox.about(self, "Başarılı", "İlan Alındı!!!")

    def Ilan_Al5(self):
        global id
        global ilan_ids
        asil_id = ilan_ids[4]
        ilan_al(asil_id, id)
        QMessageBox.about(self, "Başarılı", "İlan Alındı!!!")


    def VerisetiEtiketGit(self):
        self.ui.Sayfalar.setCurrentIndex(5)
    def VerilenIlanlarGit(self):
        global ver_ilanid
        verilen_ilanlar = list(verilen_ilan_gor())
        for i in range(len(verilen_ilanlar)):
            verilen_ilanlar[i] = list(verilen_ilanlar[i])

        textas = str(verilen_ilanlar[0][-1])
        textas2 = str(verilen_ilanlar[1][-1])
        self.ui.VerIlCombobox.addItem(textas)
        self.ui.VerIlCombobox.addItem(textas2)

        self.ui.Sayfalar.setCurrentIndex(6)
    def KayitOlGit(self):
        self.ui.App.setCurrentIndex(2)
    def GiriseGit(self):
        self.ui.App.setCurrentIndex(1)


    def Giris_clicked(self):
        global id
        try:
            sifre = self.ui.sifre_ledit.text()
            e_posta = self.ui.mail_ledit.text()
            mycursor = mydb.cursor()
            sql = "SELECT password FROM user WHERE mail= %s"
            arama = (e_posta,)
            mycursor.execute(sql, arama,)
            myresult = mycursor.fetchall()
            myresult=myresult[0][0]
            if (sifre == myresult):
                id = id_belirle(e_posta)
                print(id)
                self.ui.App.setCurrentIndex(0)
                self.AnaSayfaGit()
            else:
                QMessageBox.about(self, "Warning!", "Giriş Başarısız!!!")
        except(mysql.connector.errors.ProgrammingError):
            QMessageBox.about(self, "Warning!", "Giriş Başarısız!!!")

    def Labelimg(self):
        subprocess.Popen("python labelimg.py")
    def Cikis(self):
        self.ui.App.setCurrentIndex(1)

    def kayit_ol(self):
        isim = self.ui.ad_linedit.text()
        s_isim = self.ui.soyad_linedit.text()
        e_posta = self.ui.mail_linedit.text()
        s_onay = self.ui.sifreonay_linedit.text()
        sifre = self.ui.sifre_linedit.text()
        if (s_onay != sifre):
            QMessageBox.about(self, "Warning!", "Şifreler Farklı!!!")
        elif (isim == None or s_isim == None or e_posta == None or s_onay == None or sifre == None):
            QMessageBox.about(self, "Warning!", "Alanlar Boş!!!")
        else:
            try:
                mycursor = mydb.cursor()
                sql = "INSERT INTO user ( name, s_name, mail, password) VALUES (%s, %s, %s, %s)"
                val = (isim,s_isim,e_posta,sifre,)
                mycursor.execute(sql,val,)
                mydb.commit()
                self.ui.App.setCurrentIndex(1)
            except(mysql.connector.errors.ProgrammingError):
                pass

    def Fonksiyon(self):
        pass

    def hakkimda_gir(self):  # tamamlandı
        global id
        try:
            mycursor = mydb.cursor()
            sql = "UPDATE user SET about_me= %s WHERE user_id = %s"
            temp_id = str(id)
            text = self.ui.Hakkimda.text()
            arama = (text, temp_id,)
            mycursor.execute(sql, arama)
            mydb.commit()
        except(mysql.connector.errors.ProgrammingError):
            print("Aranan kişi bulunamadı.")


app = QApplication([])
window = Window()
window.show()
app.exec()

