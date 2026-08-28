import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q05 - Menu Arquivo com Sair")

        menuArquivo = self.menuBar().addMenu("Arquivo")

        acaoSair = QAction("Sair", self)
        menuArquivo.addAction(acaoSair)

        acaoSair.triggered.connect(self.close)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
