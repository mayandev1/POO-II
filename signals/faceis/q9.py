from PySide6.QtWidgets import QApplication, QLineEdit

app = QApplication([])

msg = QLineEdit()
msg.textChanged.emit("")