import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QGridLayout com stretch")

        layout = QGridLayout()
        layout.addWidget(QPushButton("Botão 1"), 0, 0)
        layout.addWidget(QPushButton("Botão 2"), 0, 1)
        layout.addWidget(QPushButton("Botão 3"), 1, 0)
        layout.addWidget(QPushButton("Botão 4"), 1, 1)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
