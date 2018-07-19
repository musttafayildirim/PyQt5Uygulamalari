import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.yaziAlani = QtWidgets.QLabel("Bana henüz tıklanmadı...")

        self.buton = QtWidgets.QPushButton("TIKLA")

        self.say = 0


        verticalBox = QtWidgets.QVBoxLayout()
        verticalBox.addWidget(self.buton)
        verticalBox.addWidget(self.yaziAlani)
        verticalBox.addStretch()

        horizantalBox = QtWidgets.QHBoxLayout()
        horizantalBox.addStretch()
        horizantalBox.addLayout(verticalBox)
        horizantalBox.addStretch()

        self.setLayout(horizantalBox)
        self.buton.clicked.connect(self.click)

        self.show()

    def click(self):
        self.say += 1
        self.yaziAlani.setText("Bana " + str(self.say) + " kere tıklandı....")

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()

sys.exit(app.exec_())
