# 6. Use QDialogButtonBox com botoes OK e Cancel em um QDialog.
import sys
from PySide6.QtWidgets import QApplication, QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class DialogoOkCancel(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("OK ou Cancel")

        botoes = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        botoes.accepted.connect(self.accept)
        botoes.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Escolha uma opção:"))
        layout.addWidget(botoes)
        self.setLayout(layout)


app = QApplication(sys.argv)

dialogo = DialogoOkCancel()
if dialogo.exec():
    print("Usuário clicou em OK")
else:
    print("Usuário clicou em Cancel")
