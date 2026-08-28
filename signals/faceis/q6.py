from PySide6.QtCore import QObject, Signal

class myclass(QObject):
    meuSinal = Signal(bool)
    
obj = myclass()
obj.meuSinal.emit(True)
obj.meuSinal.emit(False)