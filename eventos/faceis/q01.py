import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("keyPressEvent")
        self.setFixedSize(QSize(400, 200))

        self.label = QLabel("Pressione uma tecla")
        self.setCentralWidget(self.label)

    def keyPressEvent(self, event):
        self.label.setText(f"Tecla pressionada: {event.text()}")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
