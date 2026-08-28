import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton, QLineEdit, QToolBar
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        layout = QHBoxLayout(widget)

        self.lineEdit = QLineEdit()
        layout.addWidget(self.lineEdit)

        botao = QPushButton("Limpar")
        layout.addWidget(botao)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        acaoLimpar = QAction("Limpar", self)
        toolbar.addAction(acaoLimpar)

        menu = self.menuBar().addMenu("Editar")
        menu.addAction(acaoLimpar)

        botao.clicked.connect(self.limpar)
        acaoLimpar.triggered.connect(self.limpar)

    def limpar(self):
        self.lineEdit.clear()


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())