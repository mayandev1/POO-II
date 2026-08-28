import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSpinBox")

        spinbox = QSpinBox()
        spinbox.setRange(0, 100)
        self.setCentralWidget(spinbox)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
