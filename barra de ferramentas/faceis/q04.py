import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q04 - Toolbar com Novo e Fechar")

        toolbar = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, toolbar)

        acaoNovo = QAction("Novo", self)
        toolbar.addAction(acaoNovo)

        acaoFechar = QAction("Fechar", self)
        toolbar.addAction(acaoFechar)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
