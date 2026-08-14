from PySide6.QtCore import Slot, QObject, Signal

class myClass(QObject):
    signal = Signal(list)
    
    @Slot(list)
    def slot(self, list):
        print(len(list))
        
obj = myClass()
obj.slot([6, 7, 67])