from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtCore import QObject, Slot, QTimer, QTime

class myClass(QObject):
    def __init__(self, label):
        super().__init__()

        self.label = label

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateClock)
        self.timer.start(1000)

    @Slot()
    def updateClock(self):
        hour = QTime.currentTime()
        self.label.setText(hour.toString("HH:mm:ss"))

app = QApplication([])

label = QLabel()
obj = myClass(label)

label.show()
app.exec()