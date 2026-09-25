# 10. Use activateWindow() para trazer janela secundaria para frente.
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

        self.secundaria = JanelaSecundaria()
        self.secundaria.show()

        botao = QPushButton("Trazer janela secundária para frente")
        botao.clicked.connect(self.trazer_para_frente)
        self.setCentralWidget(botao)

    def trazer_para_frente(self):
        self.secundaria.show()
        self.secundaria.activateWindow()
        self.secundaria.raise_()


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
