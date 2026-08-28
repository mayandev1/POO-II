from PySide6.QtWidgets import QApplication, QLabel, QDoubleSpinBox
from PySide6.QtCore import Slot


class myClass:
    def __init__(self, label):
        self.label = label

    @Slot(float)
    def mySlot(self, value):
        self.label.setText(f"{value:.2f}")


app = QApplication([])

label = QLabel("0.00")
spinBox = QDoubleSpinBox()

obj = myClass(label)

spinBox.valueChanged.connect(obj.mySlot)

label.show()
spinBox.show()

app.exec()