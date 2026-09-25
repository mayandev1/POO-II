# 11. Adicione um QSpinBox dentro de um QDialog simples.
import sys
from PySide6.QtWidgets import QApplication, QDialog, QSpinBox, QVBoxLayout, QLabel


class DialogoSpinBox(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Escolha um número")

        spin = QSpinBox()
        spin.setRange(0, 100)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Quantidade:"))
        layout.addWidget(spin)
        self.setLayout(layout)


app = QApplication(sys.argv)

dialogo = DialogoSpinBox()
dialogo.exec()
