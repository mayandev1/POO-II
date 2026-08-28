import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTextEdit")

        text_edit = QTextEdit()
        text_edit.setPlaceholderText("Digite um texto com múltiplas linhas")
        self.setCentralWidget(text_edit)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
