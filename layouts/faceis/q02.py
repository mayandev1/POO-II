import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QHBoxLayout")

        layout = QHBoxLayout()
        layout.addWidget(QLabel("Label 1"))
        layout.addWidget(QLabel("Label 2"))
        layout.addWidget(QLabel("Label 3"))

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
