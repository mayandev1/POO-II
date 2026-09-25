# 13. Use QMainWindow como popup com menuBar simples.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QAction


class PopupWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Popup")
        self.setCentralWidget(QLabel("Esta é uma janela popup com menuBar."))

        menu = self.menuBar()
        menu_arquivo = menu.addMenu("Arquivo")

        acao_fechar = QAction("Fechar", self)
        acao_fechar.triggered.connect(self.close)
        menu_arquivo.addAction(acao_fechar)


app = QApplication(sys.argv)

popup = PopupWindow()
popup.show()
app.exec()
