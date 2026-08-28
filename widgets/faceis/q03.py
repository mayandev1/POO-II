import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLineEdit")

        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Digite algo aqui")
        self.setCentralWidget(line_edit)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
