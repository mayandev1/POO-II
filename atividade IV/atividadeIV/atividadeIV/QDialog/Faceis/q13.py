# 13. Use accept() e reject() manualmente em botoes de QDialog.
import sys
from PySide6.QtWidgets import QApplication, QDialog, QPushButton, QHBoxLayout


class DialogoManual(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Aceitar ou Rejeitar")

        botao_aceitar = QPushButton("Aceitar")
        botao_aceitar.clicked.connect(self.accept)

        botao_rejeitar = QPushButton("Rejeitar")
        botao_rejeitar.clicked.connect(self.reject)

        layout = QHBoxLayout()
        layout.addWidget(botao_aceitar)
        layout.addWidget(botao_rejeitar)
        self.setLayout(layout)


app = QApplication(sys.argv)

dialogo = DialogoManual()
if dialogo.exec():
    print("Diálogo aceito")
else:
    print("Diálogo rejeitado")
