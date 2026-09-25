# 3. Configure setParent(janela_principal) em uma janela secundaria.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        self.janela_secundaria = QWidget()
        self.janela_secundaria.setWindowTitle("Janela Secundária")
        # setParent define este widget como filho da janela principal
        self.janela_secundaria.setParent(self)
        self.janela_secundaria.setWindowFlag(self.janela_secundaria.windowFlags())

        botao = QPushButton("Abrir janela secundária")
        botao.clicked.connect(self.janela_secundaria.show)
        self.setCentralWidget(botao)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
