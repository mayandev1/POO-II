# 15. Mostre janela secundaria como Qt.Tool (sem barra de titulo completa).
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PySide6.QtCore import Qt


class JanelaFerramenta(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.Tool)
        self.setWindowTitle("Ferramenta")
        self.setCentralWidget(QLabel("Janela do tipo Tool"))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        self.ferramenta = JanelaFerramenta()

        botao = QPushButton("Abrir janela Tool")
        botao.clicked.connect(self.ferramenta.show)
        self.setCentralWidget(botao)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
