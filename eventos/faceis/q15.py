import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("showEvent")
        self.setFixedSize(QSize(400, 200))

        self.label = QLabel()
        self.setCentralWidget(self.label)

    def showEvent(self, event):
        self.label.setText("Dados inicializados ao mostrar a janela")
        super().showEvent(event)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
