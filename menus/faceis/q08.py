import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction, QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q08 - Menu Editar com Ícone")

        menuEditar = self.menuBar().addMenu("Editar")

        acaoColar = QAction(QIcon.fromTheme("edit-paste"), "Colar", self)
        menuEditar.addAction(acaoColar)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
