# 9. Use show() (nao modal) em um QDialog com um QCheckBox.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QCheckBox, QVBoxLayout, QPushButton


class DialogoNaoModal(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Diálogo não modal")
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("Aceito os termos"))
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        self.dialogo = DialogoNaoModal(self)

        botao = QPushButton("Abrir diálogo não modal")
        botao.clicked.connect(self.dialogo.show)
        self.setCentralWidget(botao)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
