# 8. Mostre QMessageBox a partir de um slot de botao na janela principal.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        botao = QPushButton("Clique aqui")
        botao.clicked.connect(self.botao_clicado)
        self.setCentralWidget(botao)

    def botao_clicado(self):
        QMessageBox.information(self, "Aviso", "Você clicou no botão!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
