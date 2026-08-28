import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q09 - Toolbar com Copiar")

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        acaoCopiar = QAction("Copiar", self)
        toolbar.addAction(acaoCopiar)

        acaoCopiar.triggered.connect(self.copiar)

    def copiar(self):
        print("Texto copiado")


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
