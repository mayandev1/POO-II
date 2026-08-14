from PySide6.QtWidgets import QApplication, QRadioButton
from PySide6.QtCore import Slot

class myClass:
    def __init__(self, radio):
        self.radio = radio
        
    @Slot(bool)
    def changeColor(self, state):
        if state:
            self.radio.setStyleSheet("background-color: blue;")
        else:
            self.radio.setStyleSheet("background-color: red;")
            
app = QApplication([])

radio = QRadioButton("Change color")

obj = myClass(radio)

radio.toggled.connect(obj.changeColor)
radio.show()
app.exec()