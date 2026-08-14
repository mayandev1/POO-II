from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import Slot

class myWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.botton = QPushButton("Exit", self)
        self.botton.clicked.connect(self.closeWindow)
        
    @Slot()
    def closeWindow(self):
        self.close()
        
app = QApplication([])

window = myWindow()
window.show()

app.exec()