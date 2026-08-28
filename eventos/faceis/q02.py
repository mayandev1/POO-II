import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("mousePressEvent")
        self.setFixedSize(QSize(400, 200))

        self.label = QLabel("Clique para mudar a cor de fundo")
        self.label.setAutoFillBackground(True)
        self.setCentralWidget(self.label)

    def mousePressEvent(self, event):
        palette = self.label.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("lightblue"))
        self.label.setPalette(palette)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
