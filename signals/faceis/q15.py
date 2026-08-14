from PySide6.QtCore import QObject, Signal

class myObject:
    pass

class myClass(QObject):
    signal = Signal(myObject)
    
obj = myClass()
obj.signal.emit(myObject())