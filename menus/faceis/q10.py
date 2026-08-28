import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q10 - Menu Arquivo com Imprimir")

        menuArquivo = self.menuBar().addMenu("Arquivo")

        acaoImprimir = QAction("Imprimir", self)
        menuArquivo.addAction(acaoImprimir)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
