from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot


class myclass():
    @Slot()
    
    def mySlot(self):
        print("Botton Clicked!")

app = QApplication([])
botton = QPushButton("Click here")
obj = myclass()

botton.clicked.connect(obj.mySlot)

botton.show()
app.exec()