import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import QSize


class MeuLineEdit(QLineEdit):
    def focusInEvent(self, event):
        self.setStyleSheet("border: 2px solid blue;")
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self.setStyleSheet("")
        super().focusOutEvent(event)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("focusInEvent")
        self.setFixedSize(QSize(400, 200))

        self.setCentralWidget(MeuLineEdit())


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
