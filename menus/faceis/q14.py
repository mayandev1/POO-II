import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction, QKeySequence


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q14 - Menu Editar com Desfazer")

        menuEditar = self.menuBar().addMenu("Editar")

        acaoDesfazer = QAction("Desfazer", self)
        acaoDesfazer.setShortcut(QKeySequence("Ctrl+Z"))
        menuEditar.addAction(acaoDesfazer)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
