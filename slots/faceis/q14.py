from PySide6.QtCore import QObject, Slot, Qt

class myClass(QObject):
    @Slot(Qt.AlignmentFlag)
    def mySlot(self, value):
        print(value.name)

obj = myClass()
obj.mySlot(Qt.AlignmentFlag.AlignCenter)