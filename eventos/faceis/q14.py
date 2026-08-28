import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QSize, QEvent


class AreaHover(QWidget):
    def __init__(self, label):
        super().__init__()
        self.label = label
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        self.setMouseTracking(True)

    def event(self, event):
        if event.type() == QEvent.Type.HoverMove:
            pos = event.position()
            self.label.setText(f"Posição: {int(pos.x())}, {int(pos.y())}")
        return super().event(event)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("hoverMoveEvent")
        self.setFixedSize(QSize(400, 200))

        label = QLabel("Mova o mouse sobre a área")
        area = AreaHover(label)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(area)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
