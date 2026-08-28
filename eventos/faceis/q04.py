import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("closeEvent")
        self.resize(400, 200)

        self.label = QLabel("Feche a janela para ver a confirmação")
        self.setCentralWidget(self.label)

    def closeEvent(self, event):
        resposta = QMessageBox.question(
            self,
            "Confirmar saída",
            "Tem certeza que deseja fechar a janela?"
        )

        if resposta == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
