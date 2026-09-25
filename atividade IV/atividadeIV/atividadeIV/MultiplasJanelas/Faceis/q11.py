# 11. Crie janela com setWindowModality(Qt.ApplicationModal).
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import Qt


class JanelaModal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Modal")
        self.setWindowModality(Qt.WindowModality.ApplicationModal)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        self.modal = JanelaModal()

        botao = QPushButton("Abrir janela modal")
        botao.clicked.connect(self.modal.show)
        self.setCentralWidget(botao)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
