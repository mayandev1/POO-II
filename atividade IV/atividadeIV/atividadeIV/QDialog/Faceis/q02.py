# 2. Use QDialog com QPushButton "OK" que fecha o dialogo ao clicar.
import sys
from PySide6.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout


class MeuDialogo(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Diálogo com botão OK")

        botao_ok = QPushButton("OK")
        botao_ok.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(botao_ok)
        self.setLayout(layout)


app = QApplication(sys.argv)

dialogo = MeuDialogo()
dialogo.exec()
