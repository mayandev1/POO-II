import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout aninhado simples")

        layout_principal = QHBoxLayout()
        layout_interno = QVBoxLayout()

        layout_interno.addWidget(QPushButton("Botão 1"))
        layout_interno.addWidget(QPushButton("Botão 2"))

        layout_principal.addLayout(layout_interno)
        layout_principal.addWidget(QPushButton("Botão 3"))

        central_widget = QWidget()
        central_widget.setLayout(layout_principal)
        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
