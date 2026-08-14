from PySide6.QtWidgets import QApplication, QLabel, QLineEdit
from PySide6.QtCore import Slot


class myclass():
    def __init__(self, label):
        self.label = label
    
    @Slot(str)
    
    def mySlot(self, text):
        self.label.setText(text)

app = QApplication([])


camp = QLineEdit()
label = QLabel("Digit something...")
obj = myclass(label)

camp.textChanged.connect(obj.mySlot)

camp.show()
label.show()
app.exec()