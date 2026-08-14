from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

count = 0

class myClass:
    @Slot()
    def increment(self):
        global count
        
        count += 1
        print(count)

app = QApplication([])

button = QPushButton("+1")

obj = myClass()

button.clicked.connect(obj.increment)
button.show()
app.exec()