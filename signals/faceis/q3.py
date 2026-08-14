from PySide6.QtCore import QObject, Signal

class myclass(QObject):
    meuSinal = Signal(str)

obj = myclass()
obj.meuSinal.emit(42)