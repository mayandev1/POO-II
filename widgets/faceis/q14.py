import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTabWidget")

        tabs = QTabWidget()
        tabs.addTab(QLabel("Conteúdo da aba 1"), "Aba 1")
        tabs.addTab(QLabel("Conteúdo da aba 2"), "Aba 2")
        self.setCentralWidget(tabs)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
