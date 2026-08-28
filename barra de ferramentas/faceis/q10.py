import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q10 - Toolbar Flutuante")

        toolbar = QToolBar()
        toolbar.setFloatable(True)
        self.addToolBar(toolbar)

        acaoAbrir = QAction("Abrir", self)
        toolbar.addAction(acaoAbrir)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
