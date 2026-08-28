import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction, QKeySequence


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q03 - Menu Editar com Copiar")

        menuEditar = self.menuBar().addMenu("Editar")

        acaoCopiar = QAction("Copiar", self)
        acaoCopiar.setShortcut(QKeySequence("Ctrl+C"))
        menuEditar.addAction(acaoCopiar)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
