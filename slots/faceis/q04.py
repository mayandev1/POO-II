from PySide6.QtWidgets import QApplication, QLabel, QCheckBox
from PySide6.QtCore import Slot


class myclass():
    def __init__(self, label):
        self.label = label
    
    @Slot(bool)
    
    def mySlot(self, state):
        self.label.setVisible(state)

app = QApplication([])

checkbox = QCheckBox("Show text")
label = QLabel("Flávio Bolsonaro 2027")
obj = myclass(label)

checkbox.stateChanged.connect(obj.mySlot)

checkbox.show()
label.show()
app.exec()