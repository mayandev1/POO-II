import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt, QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("enterEvent")
        self.setFixedSize(QSize(400, 200))

        self.label = QLabel("Passe o mouse sobre a janela")
        self.setCentralWidget(self.label)

    def enterEvent(self, event):
        self.setCursor(Qt.CursorShape.PointingHandCursor)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
