import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QComboBox")

        combo = QComboBox()
        combo.addItems(["Item 1", "Item 2", "Item 3"])
        self.setCentralWidget(combo)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
