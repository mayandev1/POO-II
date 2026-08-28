from PySide6.QtCore import QObject, Signal

class myclass(QObject):
    meuSinal = Signal(list)
    
obj = myclass()
obj.meuSinal.emit([])