# 5. Use hide() e show() para alternar entre janela principal e secundaria.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class JanelaSecundaria(QMainWindow):
    def __init__(self, principal):
        super().__init__()
        self.setWindowTitle("Janela Secundária")
        self.principal = principal

        botao = QPushButton("Voltar para a principal")
        botao.clicked.connect(self.voltar)
        self.setCentralWidget(botao)

    def voltar(self):
        self.hide()
        self.principal.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        self.secundaria = JanelaSecundaria(self)

        botao = QPushButton("Ir para a secundária")
        botao.clicked.connect(self.ir_para_secundaria)
        self.setCentralWidget(botao)

    def ir_para_secundaria(self):
        self.hide()
        self.secundaria.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
