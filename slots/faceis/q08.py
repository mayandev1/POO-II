from PySide6.QtWidgets import QApplication, QTextEdit, QPushButton
from PySide6.QtCore import Slot


class myClass:
    def __init__(self, textEdit):
        self.textEdit = textEdit
        
    
    @Slot(int)
    def clearText(self):
        self.textEdit.clear()


app = QApplication([])

textEdit = QTextEdit()
button = QPushButton("Clear")

obj = myClass(textEdit)

button.clicked.connect(obj.clearText)

textEdit.show()
button.show()
app.exec()