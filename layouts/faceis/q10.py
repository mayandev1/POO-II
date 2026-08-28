import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QProgressBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QGridLayout com QProgressBar")

        layout = QGridLayout()
        layout.addWidget(QProgressBar(), 0, 2)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
