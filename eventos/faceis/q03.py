import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("resizeEvent")
        self.resize(400, 300)

        self.label = QLabel()
        self.setCentralWidget(self.label)
        self.atualizar_label()

    def resizeEvent(self, event):
        self.atualizar_label()
        super().resizeEvent(event)

    def atualizar_label(self):
        self.label.setText(f"Tamanho: {self.width()} x {self.height()}")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
