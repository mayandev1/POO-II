# 4. Crie QDialog com QLineEdit e botao "Confirmar".
import sys
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout


class DialogoConfirmar(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Confirmar dados")

        self.campo = QLineEdit()
        self.campo.setPlaceholderText("Digite algo...")

        botao_confirmar = QPushButton("Confirmar")
        botao_confirmar.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.campo)
        layout.addWidget(botao_confirmar)
        self.setLayout(layout)


app = QApplication(sys.argv)

dialogo = DialogoConfirmar()
if dialogo.exec():
    print("Texto digitado:", dialogo.campo.text())
