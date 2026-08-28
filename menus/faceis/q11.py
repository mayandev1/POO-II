import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q11 - Menu Ferramentas")

        menuFerramentas = self.menuBar().addMenu("Ferramentas")

        acaoOpcoes = QAction("Opções", self)
        menuFerramentas.addAction(acaoOpcoes)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
