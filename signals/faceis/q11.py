from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QObject, Signal, QTimer

class myclass(QObject):
    signal = Signal()
    
    def __init__(self):
        super().__init__()
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.emitSignal)
        self.timer.start(5000)
        
    def emitSignal(self):
        self.signal.emit()
        
app = QApplication([])
obj = myclass()
app.exec()