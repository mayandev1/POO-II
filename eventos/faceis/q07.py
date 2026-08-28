import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt, QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("leaveEvent")
        self.setFixedSize(QSize(400, 200))

        self.label = QLabel("Saia da janela para restaurar o cursor")
        self.setCentralWidget(self.label)

    def enterEvent(self, event):
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def leaveEvent(self, event):
        self.setCursor(Qt.CursorShape.ArrowCursor)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
