import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q12 - Toolbar Fixa")

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        acaoNovo = QAction("Novo", self)
        toolbar.addAction(acaoNovo)

        acaoAbrir = QAction("Abrir", self)
        toolbar.addAction(acaoAbrir)

        acaoSalvar = QAction("Salvar", self)
        toolbar.addAction(acaoSalvar)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
