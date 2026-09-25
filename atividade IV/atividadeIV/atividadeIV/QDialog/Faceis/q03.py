# 3. Configure exec() para abrir um QDialog modal simples.
import sys
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout


class DialogoModal(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Diálogo Modal")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Este é um diálogo modal simples."))
        self.setLayout(layout)


app = QApplication(sys.argv)

dialogo = DialogoModal()
# exec() torna o dialogo modal, bloqueando a aplicacao ate ser fechado
resultado = dialogo.exec()
print("Diálogo fechado. Resultado:", resultado)
