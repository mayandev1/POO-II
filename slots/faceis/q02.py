from PySide6.QtWidgets import QApplication, QSpinBox
from PySide6.QtCore import Slot


class myclass():
    @Slot(int)
    
    def mySlot(self, value):
        print(value)

app = QApplication([])

spinbox = QSpinBox()
obj = myclass()

spinbox.valueChanged.connect(obj.mySlot)

spinbox.show()
app.exec()