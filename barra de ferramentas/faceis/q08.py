import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q08 - Toolbar com Ação Marcável")

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        acaoNegrito = QAction("Negrito", self)
        acaoNegrito.setCheckable(True)
        toolbar.addAction(acaoNegrito)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
