import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtGui import QAction
from PySide6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q06 - Toolbar com IconSize")

        toolbar = QToolBar()
        toolbar.setIconSize(QSize(32, 32))
        self.addToolBar(toolbar)

        acaoAbrir = QAction("Abrir", self)
        toolbar.addAction(acaoAbrir)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
