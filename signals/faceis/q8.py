from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import Signal

class MainWindow(QMainWindow):
    meuSinal = Signal()
    
    def __init__(self):
        super().__init__()
        self.meuSinal.emit()
        
app = QApplication([])
window = MainWindow()
window.show()
app.exec()