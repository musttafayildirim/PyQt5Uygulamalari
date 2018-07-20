import sys
from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox,  QLabel, QPushButton, QVBoxLayout


class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.checkBox = QCheckBox("Python kodlamaya başladım.")
        self.label = QLabel("")
        self.buton = QPushButton("TIKLA")

        vBox = QVBoxLayout()
        vBox.addWidget(self.checkBox)
        vBox.addWidget(self.label)
        vBox.addWidget(self.buton)

        self.setLayout(vBox)
        self.setWindowTitle("CheckBox Uygulaması")
        self.setGeometry(300,200,300,150)

        self.buton.clicked.connect(lambda : self.click(self.checkBox.isChecked(), self.label))
        self.show()

    def click(self, check, yazi):
        if check:
            yazi.setText("Evet aynen böyle devam et.")
        else:
            yazi.setText("Ne duruyorsun kendini topla ve hedeflerine odaklan!!!!!")






app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())



