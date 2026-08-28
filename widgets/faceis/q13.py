import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGroupBox, QVBoxLayout, QCheckBox, QRadioButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QGroupBox")

        groupbox = QGroupBox("Opções")

        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("Opção A"))
        layout.addWidget(QRadioButton("Opção B"))
        layout.addWidget(QRadioButton("Opção C"))

        groupbox.setLayout(layout)
        self.setCentralWidget(groupbox)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
