import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtGui import QAction, QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q13 - Toolbar com Imprimir")

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        acaoImprimir = QAction(QIcon.fromTheme("document-print"), "Imprimir", self)
        toolbar.addAction(acaoImprimir)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
