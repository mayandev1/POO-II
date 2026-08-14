from PySide6.QtWidgets import QApplication, QComboBox
from PySide6.QtCore import Slot


class myClass:
    @Slot(int)
    def mySlot(self, index):
        print(index)


app = QApplication([])

combo = QComboBox()
combo.addItems(["Option 1", "Option 2", "Option 3"])

obj = myClass()

combo.currentIndexChanged.connect(obj.mySlot)

combo.show()

app.exec()