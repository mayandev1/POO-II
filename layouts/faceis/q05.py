import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QVBoxLayout com stretch")

        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Botão 1"))
        layout.addWidget(QPushButton("Botão 2"), stretch=1)
        layout.addWidget(QPushButton("Botão 3"))

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
