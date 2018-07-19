import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.yaziAlani = QtWidgets.QLineEdit()
        self.yazdir = QtWidgets.QPushButton("Yazdır")
        self.temizle = QtWidgets.QPushButton("Temizle")

        self.setWindowTitle("Buton Uygulaması")
        self.setGeometry(600,300,300,300)

        verticalBox = QtWidgets.QVBoxLayout()
        verticalBox.addWidget(self.yaziAlani)
        verticalBox.addWidget(self.temizle)
        verticalBox.addWidget(self.yazdir)
        verticalBox.addStretch()

        horizantalBox = QtWidgets.QHBoxLayout()
        horizantalBox.addStretch()
        horizantalBox.addLayout(verticalBox)
        horizantalBox.addStretch()

        self.setLayout(horizantalBox)

        self.temizle.clicked.connect(self.click)
        self.yazdir.clicked.connect(self.click)

        self.show()


    def click(self):
        sender = self.sender()

        if sender.text() == "Temizle":
            self.yaziAlani.clear()
        else:
            print(self.yaziAlani.text())



app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()

sys.exit(app.exec_())