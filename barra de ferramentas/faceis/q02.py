import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtGui import QAction, QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q02 - Toolbar com Ícone")

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        acaoAbrir = QAction(QIcon.fromTheme("document-open"), "Abrir", self)
        toolbar.addAction(acaoAbrir)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
