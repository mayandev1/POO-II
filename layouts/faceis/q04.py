import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout, QLabel, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QStackedLayout")

        layout = QStackedLayout()
        layout.addWidget(QLabel("Sou um QLabel"))
        layout.addWidget(QPushButton("Sou um QPushButton"))

        layout.setCurrentIndex(0)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
