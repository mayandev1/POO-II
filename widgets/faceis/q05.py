import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QRadioButton,
    QButtonGroup
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QRadioButton")

        radio1 = QRadioButton("Opção 1")
        radio2 = QRadioButton("Opção 2")
        radio3 = QRadioButton("Opção 3")
        radio1.setChecked(True)

        grupo = QButtonGroup(self)
        grupo.addButton(radio1)
        grupo.addButton(radio2)
        grupo.addButton(radio3)

        layout = QVBoxLayout()
        layout.addWidget(radio1)
        layout.addWidget(radio2)
        layout.addWidget(radio3)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
