# 1. Crie uma classe que herde de QDialog e mostre uma janela vazia com titulo "Meu Dialogo".
import sys
from PySide6.QtWidgets import QApplication, QDialog


class MeuDialogo(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Meu Diálogo")


app = QApplication(sys.argv)

dialogo = MeuDialogo()
dialogo.exec()
