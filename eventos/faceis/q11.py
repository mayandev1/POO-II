import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("dropEvent")
        self.setFixedSize(QSize(400, 200))
        self.setAcceptDrops(True)

        self.label = QLabel("Solte um texto aqui")
        self.setCentralWidget(self.label)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        texto = event.mimeData().text()
        self.label.setText(f"Texto dropado: {texto}")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
