import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMenu
from PySide6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("contextMenuEvent")
        self.setFixedSize(QSize(400, 200))

        self.label = QLabel("Clique com o botão direito")
        self.setCentralWidget(self.label)

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction("Opção 1")
        menu.addAction("Opção 2")
        menu.addAction("Opção 3")
        menu.exec(event.globalPos())


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
