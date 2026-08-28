import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QHBoxLayout com spacing")

        layout = QHBoxLayout()
        layout.setSpacing(20)
        layout.addWidget(QCheckBox("Opção 1"))
        layout.addWidget(QCheckBox("Opção 2"))
        layout.addWidget(QCheckBox("Opção 3"))

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
