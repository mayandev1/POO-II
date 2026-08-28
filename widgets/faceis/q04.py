import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QCheckBox")

        checkbox = QCheckBox("Marcado por padrão")
        checkbox.setChecked(True)
        self.setCentralWidget(checkbox)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
