# 4. Crie duas janelas independentes que aparecem ao mesmo tempo.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class JanelaA(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela A")
        self.setCentralWidget(QLabel("Eu sou a Janela A"))


class JanelaB(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela B")
        self.setCentralWidget(QLabel("Eu sou a Janela B"))


app = QApplication(sys.argv)

janela_a = JanelaA()
janela_b = JanelaB()

janela_a.show()
janela_b.show()

app.exec()
