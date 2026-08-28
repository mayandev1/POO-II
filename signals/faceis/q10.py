from PySide6.QtCore import QObject, Signal

class myclass(QObject):
    signal = Signal(dict)
    
obj = myclass()
obj.signal.emit({"name": "Mayan"})