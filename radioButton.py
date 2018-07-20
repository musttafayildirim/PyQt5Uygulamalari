import sys
from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton,  QLabel, QPushButton, QVBoxLayout, QHBoxLayout


class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(250,250,300,150)
        self.setWindowTitle("Radio Button")
        self.radioYazisi = QLabel("Bugün nasılsın ?")
        self.neseli = QRadioButton("Neşeli")
        self.yorgun = QRadioButton("Yorgun")
        self.uzgun = QRadioButton("Üzgün")
        self.mutsuz = QRadioButton("Mutsuz")
        self.mutlu = QRadioButton("Mutlu")
        self.yaziAlani = QLabel("")
        self.buton = QPushButton("Gönder")
        vBox = QVBoxLayout()

        vBox.addWidget(self.radioYazisi)
        vBox.addWidget(self.neseli)
        vBox.addWidget(self.yorgun)
        vBox.addWidget(self.uzgun)
        vBox.addWidget(self.mutsuz)
        vBox.addWidget(self.mutlu)
        vBox.addStretch()
        vBox.addWidget(self.yaziAlani)
        vBox.addWidget(self.buton)

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addLayout(vBox)
        hbox.addStretch()
        self.setLayout(hbox)

        self.buton.clicked.connect(lambda : self.click(self.neseli.isChecked(), self.yorgun.isChecked(), self.uzgun.isChecked(), self.mutsuz.isChecked(), self.mutlu.isChecked(), self.yaziAlani))


        self.show()

    def click(self, neseli, yorgun, uzgun, mutsuz, mutlu, yaziAlani):
        if neseli:
            yaziAlani.setText("Neşelisin :D")
        if yorgun:
            yaziAlani.setText("Niye bu kadar yordun ki kendini ?")
        if uzgun:
            yaziAlani.setText("Üzülme Dünya senin üzülmene değecek kadar güzel bir yer değil.")
        if mutsuz:
            yaziAlani.setText("Mutlu olmaya çalış çünkü mutsuz olmak sana hiç yakışmıyor.")
        if mutlu:
            yaziAlani.setText("Ne kadar güzel hep mutlu ol :D:D:D")








app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())