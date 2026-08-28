import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtGui import QAction, QKeySequence


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q05 - Toolbar com Shortcut")

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        acaoNovo = QAction("Novo", self)
        acaoNovo.setShortcut(QKeySequence("Ctrl+N"))
        toolbar.addAction(acaoNovo)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
