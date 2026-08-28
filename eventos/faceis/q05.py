import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QPen
from PySide6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("paintEvent")
        self.setFixedSize(QSize(400, 300))

        self.setCentralWidget(QWidget())

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen()
        pen.setWidth(3)
        painter.setPen(pen)
        painter.drawLine(50, 150, 350, 150)
        painter.end()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
