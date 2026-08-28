import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QSlider, QLabel, QToolBar
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        layout = QGridLayout(widget)

        self.label = QLabel("Zoom: 50%")
        layout.addWidget(self.label, 0, 0)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.setValue(50)
        layout.addWidget(self.slider, 1, 0)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        acaoZoom = QAction("Zoom", self)
        toolbar.addAction(acaoZoom)

        menu = self.menuBar().addMenu("Ver")
        menu.addAction(acaoZoom)

        self.slider.valueChanged.connect(self.atualizarZoom)

    def atualizarZoom(self, valor):
        self.label.setText(f"Zoom: {valor}%")


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())