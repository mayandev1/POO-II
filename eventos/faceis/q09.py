import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("wheelEvent")
        self.setFixedSize(QSize(400, 200))

        self.label = QLabel("Use a roda do mouse")
        self.setCentralWidget(self.label)

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.label.setText("Roda para cima")
        else:
            self.label.setText("Roda para baixo")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
