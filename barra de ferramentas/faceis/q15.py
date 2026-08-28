import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q15 - Toolbar Vazia")

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        acaoSair = QAction("Sair", self)
        toolbar.addAction(acaoSair)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
