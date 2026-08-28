import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q01 - Menu Arquivo com Novo")

        menuBar = self.menuBar()
        menuArquivo = menuBar.addMenu("Arquivo")

        acaoNovo = QAction("Novo", self)
        menuArquivo.addAction(acaoNovo)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
