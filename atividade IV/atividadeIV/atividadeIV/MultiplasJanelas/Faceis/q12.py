# 12. Adicione QToolBar na janela secundaria com QAction "Fechar".
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QAction


class JanelaSecundaria(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Secundária")

        toolbar = self.addToolBar("Ferramentas")
        acao_fechar = QAction("Fechar", self)
        acao_fechar.triggered.connect(self.close)
        toolbar.addAction(acao_fechar)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        self.secundaria = JanelaSecundaria()

        botao = QPushButton("Abrir janela secundária")
        botao.clicked.connect(self.secundaria.show)
        self.setCentralWidget(botao)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
