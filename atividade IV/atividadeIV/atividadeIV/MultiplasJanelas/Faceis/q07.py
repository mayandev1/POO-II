# 7. Adicione QAction "Abrir Janela Nova" no menu da principal que abre outra janela.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMenuBar
from PySide6.QtGui import QAction


class JanelaNova(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Nova")
        self.setCentralWidget(QLabel("Esta é a janela nova."))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        self.janela_nova = JanelaNova()

        menu = self.menuBar()
        menu_janela = menu.addMenu("Janela")

        acao_abrir = QAction("Abrir Janela Nova", self)
        acao_abrir.triggered.connect(self.janela_nova.show)
        menu_janela.addAction(acao_abrir)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
