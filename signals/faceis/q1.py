from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QObject, Signal

class myclass(QObject):
    meuSinal = Signal()