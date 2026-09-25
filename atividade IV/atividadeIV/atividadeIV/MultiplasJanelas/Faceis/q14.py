# 14. Crie janela que recebe texto da principal via construtor.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


class JanelaComTexto(QMainWindow):
    def __init__(self, texto):
        super().__init__()
        self.setWindowTitle("Janela com texto recebido")
        self.setCentralWidget(QLabel(texto))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        botao = QPushButton("Abrir janela com texto")
        botao.clicked.connect(self.abrir_janela)
        self.setCentralWidget(botao)

    def abrir_janela(self):
        self.janela = JanelaComTexto("Texto enviado pela janela principal!")
        self.janela.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
