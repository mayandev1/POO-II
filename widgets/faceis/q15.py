import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolButton
from PySide6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QToolButton")

        tool_button = QToolButton()
        tool_button.setIcon(QIcon.fromTheme("document-open"))
        tool_button.setText("Abrir")
        self.setCentralWidget(tool_button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
