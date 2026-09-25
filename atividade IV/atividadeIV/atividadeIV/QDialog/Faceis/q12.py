# 12. Configure setWindowTitle("Configuracoes") em um QDialog.
import sys
from PySide6.QtWidgets import QApplication, QDialog


class DialogoConfiguracoes(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Configurações")


app = QApplication(sys.argv)

dialogo = DialogoConfiguracoes()
dialogo.exec()
