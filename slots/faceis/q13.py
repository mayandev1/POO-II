from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtCore import QObject, Slot, QDate


class myClass(QObject):
    def __init__(self, label):
        super().__init__()
        self.label = label

    @Slot()
    def updateData(self):
        data = QDate.currentDate()
        self.label.setText(data.toString("dd/MM/yyyy"))


app = QApplication([])

label = QLabel()
obj = myClass(label)

obj.updateData()

label.show()

app.exec()