import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QGridLayout 2x2")

        layout = QGridLayout()
        layout.addWidget(QLineEdit(), 0, 0)
        layout.addWidget(QLineEdit(), 0, 1)
        layout.addWidget(QLineEdit(), 1, 0)
        layout.addWidget(QLineEdit(), 1, 1)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
