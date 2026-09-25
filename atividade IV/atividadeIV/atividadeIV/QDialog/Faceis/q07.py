# 7. Crie QDialog que aparece ao clicar em um botao da janela principal.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel, QVBoxLayout


class MeuDialogo(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Diálogo")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Olá! Eu sou o diálogo."))
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        botao = QPushButton("Abrir diálogo")
        botao.clicked.connect(self.abrir_dialogo)
        self.setCentralWidget(botao)

    def abrir_dialogo(self):
        dialogo = MeuDialogo(self)
        dialogo.exec()


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
