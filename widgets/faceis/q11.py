import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QCalendarWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QCalendarWidget")

        calendar = QCalendarWidget()
        self.setCentralWidget(calendar)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
