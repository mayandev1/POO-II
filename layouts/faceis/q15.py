import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QRadioButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QHBoxLayout com margin")

        layout = QHBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.addWidget(QRadioButton("Opção 1"))
        layout.addWidget(QRadioButton("Opção 2"))
        layout.addWidget(QRadioButton("Opção 3"))

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
