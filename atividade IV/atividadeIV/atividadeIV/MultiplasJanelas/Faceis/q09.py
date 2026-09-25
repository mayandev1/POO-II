# 9. Crie tres janelas e feche todas com um botao na principal.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class JanelaExtra(QMainWindow):
    def __init__(self, titulo):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setCentralWidget(QLabel(titulo))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        self.janela1 = JanelaExtra("Janela 1")
        self.janela2 = JanelaExtra("Janela 2")
        self.janela3 = JanelaExtra("Janela 3")

        self.janela1.show()
        self.janela2.show()
        self.janela3.show()

        botao = QPushButton("Fechar todas as janelas")
        botao.clicked.connect(self.fechar_todas)
        self.setCentralWidget(botao)

    def fechar_todas(self):
        self.janela1.close()
        self.janela2.close()
        self.janela3.close()


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
