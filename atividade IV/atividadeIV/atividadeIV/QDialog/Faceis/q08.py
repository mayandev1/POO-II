# 8. Configure setFixedSize(300, 200) em um QDialog.
import sys
from PySide6.QtWidgets import QApplication, QDialog


class DialogoTamanhoFixo(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tamanho fixo")
        self.setFixedSize(300, 200)


app = QApplication(sys.argv)

dialogo = DialogoTamanhoFixo()
dialogo.exec()
