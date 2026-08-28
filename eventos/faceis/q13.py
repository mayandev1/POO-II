import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("tabletEvent")
        self.setFixedSize(QSize(400, 200))

        self.label = QLabel("Use uma caneta/tablet, se disponível")
        self.setCentralWidget(self.label)

    def tabletEvent(self, event):
        self.label.setText(f"Pressão da caneta: {event.pressure()}")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
