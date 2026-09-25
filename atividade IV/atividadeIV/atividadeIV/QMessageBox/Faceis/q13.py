# 13. Mostre alerta de confirmacao ao tentar fechar a janela.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.resize(300, 200)

    def closeEvent(self, event):
        resposta = QMessageBox.question(
            self, "Confirmar saída", "Deseja realmente fechar a janela?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if resposta == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
