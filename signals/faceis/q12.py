from PySide6.QtWidgets import QApplication, QComboBox

app = QApplication([])

combo = QComboBox()
combo.currentIndexChanged.emit(0)

app.exec()