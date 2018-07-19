import sys
from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    #buton tanımlamaları....
    tamam = QtWidgets.QPushButton("Tamam")
    iptal = QtWidgets.QPushButton("İptal")

    #horizantal layoutun belirlenmesi
    horitantalBox = QtWidgets.QHBoxLayout()

    #verticalbox layout tanımlama
    vertical = QtWidgets.QVBoxLayout()

    vertical.addStretch()

    vertical.addLayout(horitantalBox)

    #layout içinde kullanılacak butonların layouta yerleştirilmesi
    horitantalBox.addStretch()
    horitantalBox.addWidget(tamam)
    horitantalBox.addWidget(iptal)

    # çalışma alanımızı tanımlıyoruz....
    pencere = QtWidgets.QWidget()

    # pencere içerisinde kullanıcak olan layoutun tanıtılması
    pencere.setLayout(vertical)

    # pencere başlığını belirlemek için kullandık....
    pencere.setWindowTitle("Uygulama yapmaya başladık :D")

    # buton tanımlaması yapıyoruz
    buton = QtWidgets.QPushButton(pencere)
    buton.setText("TIKLAMA")
    buton.move(200,80)

    # yeni bir label ekledik ve labelin nerede gösterileceğini ayarladık...
    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("Burası bir yazıdır..")
    etiket1.move(200,30)

    # penceremizin nerede başlayacağını ve ilk boyutunu belirtiyoruz..
    pencere.setGeometry(100, 100, 500, 500)

    # pencereyi göstermek için gerekli olan cod satırı...
    pencere.show()

    # X tuşuna basınca programın kapanması için gerekli olan komut
    sys.exit(app.exec_())

Pencere()


