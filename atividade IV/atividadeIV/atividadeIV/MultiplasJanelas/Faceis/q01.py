# 1. Crie uma segunda QMainWindow e mostre-a com show() ao clicar em um botao da principal.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class JanelaSecundaria(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Secundária")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        self.janela2 = JanelaSecundaria()

        botao = QPushButton("Abrir segunda janela")
        botao.clicked.connect(self.janela2.show)
        self.setCentralWidget(botao)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
