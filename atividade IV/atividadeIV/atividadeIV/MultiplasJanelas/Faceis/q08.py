# 8. Configure janela secundaria com tamanho fixo 400x300.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class JanelaSecundaria(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Secundária")
        self.setFixedSize(400, 300)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        self.secundaria = JanelaSecundaria()

        botao = QPushButton("Abrir janela secundária (400x300)")
        botao.clicked.connect(self.secundaria.show)
        self.setCentralWidget(botao)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
