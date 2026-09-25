# 6. Crie janela filha com Qt.Window flag e botao para fechar.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt


class JanelaFilha(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.WindowType.Window)  # forca ser uma janela independente
        self.setWindowTitle("Janela Filha")

        botao_fechar = QPushButton("Fechar")
        botao_fechar.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(botao_fechar)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        self.filha = JanelaFilha(self)

        botao = QPushButton("Abrir janela filha")
        botao.clicked.connect(self.filha.show)
        self.setCentralWidget(botao)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
