from PySide6.QtCore import QObject, Signal

class myclass(QObject):
    signal = Signal(float)
    
obj = myclass()
obj.signal.emit(3.14)