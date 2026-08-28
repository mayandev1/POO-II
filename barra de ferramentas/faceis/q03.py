import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q03 - Toolbar com Salvar")

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        acaoSalvar = QAction("Salvar", self)
        toolbar.addAction(acaoSalvar)

        acaoSalvar.triggered.connect(self.salvar)

    def salvar(self):
        print("Salvo")


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
