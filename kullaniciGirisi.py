import sys
from PyQt5 import QtWidgets
import sqlite3

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()
        self.baglantiOlustur()
    def baglantiOlustur(self):
        baglanti = sqlite3.connect("database.db")

        self.cursor = baglanti.cursor()

        self.cursor.execute("Create Table If not exists uyeler(kullaniciAdi TEXT, parola TEXT)")
        baglanti.commit()


    def login(self):

        sender = self.sender()

        adi = self.kullaniciAdi.text()
        par = self.parola.text()

        if sender.text() == "Giris":

            self.cursor.execute("select * from uyeler where kullaniciAdi = ? and parola = ?", (adi, par))

            data = self.cursor.fetchall()

            if len(data) == 0:
                self.yaziAlani.setText("Böyle bir kullanıcı yok\n Lütfen tekrar deneyin")

            else:
                self.yaziAlani.setText("Giriş yapıldı..." + adi)

        else:
            baglanti = sqlite3.connect("database.db")

            self.cursor = baglanti.cursor()

            self.cursor.execute("insert into uyeler(kullaniciAdi, parola) values(?,?)", (adi, par))
            baglanti.commit()



    def init_ui(self):

        self.kullaniciAdi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giris")
        self.register = QtWidgets.QPushButton("Kayıt Ol")
        self.yaziAlani = QtWidgets.QLabel()


        verticalBox = QtWidgets.QVBoxLayout()
        verticalBox.addWidget(self.kullaniciAdi)
        verticalBox.addWidget(self.parola)
        verticalBox.addWidget(self.yaziAlani)
        verticalBox.addStretch()
        verticalBox.addWidget(self.register)
        verticalBox.addWidget(self.giris)


        horizantalBox = QtWidgets.QHBoxLayout()
        horizantalBox.addStretch()
        horizantalBox.addLayout(verticalBox)
        horizantalBox.addStretch()

        #uygulamamızın başlığını belirliyoruz..
        self.setWindowTitle("Kullanıcı Girişi")
        #başlayacağı konumu ve başlangıç boyutunu belirliyoruz..
        self.setGeometry(300,200,250,200)

        #butonlara tıklanıldığı zaman yapılacak işlemleri belirliyoruz..
        self.giris.clicked.connect(self.login)
        self.register.clicked.connect(self.login)
        self.setLayout(horizantalBox)

        self.show()


app  = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())