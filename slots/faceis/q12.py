from PySide6.QtCore import Slot, QObject

class myClass(QObject):
    @Slot(dict)
    def mySlot(self, data):
        print(data["name"])
        
obj = myClass()
obj.mySlot({"name": "Mayan", "years old": 20})