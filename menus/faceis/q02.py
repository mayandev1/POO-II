import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q02 - Menu Arquivo com Abrir")

        menuArquivo = self.menuBar().addMenu("Arquivo")

        acaoAbrir = QAction("Abrir", self)
        menuArquivo.addAction(acaoAbrir)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
