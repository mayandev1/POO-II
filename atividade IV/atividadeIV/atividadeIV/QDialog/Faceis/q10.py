# 10. Crie QDialog com QComboBox contendo 3 opcoes.
import sys
from PySide6.QtWidgets import QApplication, QDialog, QComboBox, QVBoxLayout


class DialogoComboBox(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Escolha uma opção")

        combo = QComboBox()
        combo.addItems(["Opção 1", "Opção 2", "Opção 3"])

        layout = QVBoxLayout()
        layout.addWidget(combo)
        self.setLayout(layout)


app = QApplication(sys.argv)

dialogo = DialogoComboBox()
dialogo.exec()
