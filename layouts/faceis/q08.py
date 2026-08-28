import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QStackedLayout com três páginas")

        layout = QStackedLayout()
        layout.addWidget(QLabel("Página 0"))
        layout.addWidget(QLabel("Página 1"))
        layout.addWidget(QLabel("Página 2"))

        layout.setCurrentIndex(2)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
