import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QStackedLayout, QComboBox, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QStackedLayout com QComboBox")

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(QLabel("Página 0"))
        self.stacked_layout.addWidget(QLabel("Página 1"))
        self.stacked_layout.addWidget(QLabel("Página 2"))

        combo = QComboBox()
        combo.addItems(["Página 0", "Página 1", "Página 2"])
        combo.currentIndexChanged.connect(self.stacked_layout.setCurrentIndex)

        layout_principal = QVBoxLayout()
        layout_principal.addWidget(combo)
        layout_principal.addLayout(self.stacked_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout_principal)
        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
