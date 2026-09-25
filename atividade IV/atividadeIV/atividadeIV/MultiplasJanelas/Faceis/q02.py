# 2. Use QMainWindow secundaria com titulo "Janela 2" e um QLabel.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


class Janela2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela 2")
        self.setCentralWidget(QLabel("Eu sou a Janela 2"))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        self.janela2 = Janela2()

        botao = QPushButton("Abrir Janela 2")
        botao.clicked.connect(self.janela2.show)
        self.setCentralWidget(botao)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
