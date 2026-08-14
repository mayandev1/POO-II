from PySide6.QtCore import QObject, Signal

class myclass(QObject):
    valueChanged = Signal(int)
    
    def __init(self):
        super().__init__()
        self.value = 0
    
    def changeValue(self, newValue):
        self.value = newValue
        self.valueChanged.emit(newValue)
    
obj = myclass()
obj.changeValue.emit(67)