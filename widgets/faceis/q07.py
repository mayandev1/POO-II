import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSlider
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSlider")

        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(50)
        self.setCentralWidget(slider)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
