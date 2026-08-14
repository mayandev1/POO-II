from PySide6.QtWidgets import QApplication, QSlider
from PySide6.QtCore import Qt

app = QApplication([])

slider = QSlider(Qt.Horizontal)

slider.valueChanged.emit(67)