# 5. Adicione um QLabel "Digite seu nome" dentro de um QDialog.
import sys
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QVBoxLayout


class DialogoNome(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nome")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Digite seu nome"))
        layout.addWidget(QLineEdit())
        self.setLayout(layout)


app = QApplication(sys.argv)

dialogo = DialogoNome()
dialogo.exec()
