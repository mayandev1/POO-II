import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTableWidget")

        table = QTableWidget(2, 2)
        self.setCentralWidget(table)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
