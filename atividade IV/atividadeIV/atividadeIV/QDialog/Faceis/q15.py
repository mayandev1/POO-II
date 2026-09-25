# 15. Mostre um QDialog com QTextEdit de uma linha.
import sys
from PySide6.QtWidgets import QApplication, QDialog, QTextEdit, QVBoxLayout


class DialogoTextEdit(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Texto")

        texto = QTextEdit()
        texto.setFixedHeight(30)  # comportamento de "uma linha"
        texto.setPlaceholderText("Digite uma linha de texto...")

        layout = QVBoxLayout()
        layout.addWidget(texto)
        self.setLayout(layout)


app = QApplication(sys.argv)

dialogo = DialogoTextEdit()
dialogo.exec()
