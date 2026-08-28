import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QProgressBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QProgressBar")

        progress_bar = QProgressBar()
        progress_bar.setValue(75)
        self.setCentralWidget(progress_bar)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
