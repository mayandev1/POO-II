# 4. Crie QStackedLayout na principal, QAction "Janela 2" no toolbar abre janela
# secundaria que envia sinal para trocar pagina.
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QStackedLayout, QLabel, QPushButton, QVBoxLayout
)
from PySide6.QtGui import QAction
from PySide6.QtCore import Signal


class JanelaSecundaria(QMainWindow):
    trocar_pagina = Signal(int)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela 2")

        botao = QPushButton("Trocar para página 2")
        botao.clicked.connect(lambda: self.trocar_pagina.emit(1))
        self.setCentralWidget(botao)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        self.pagina1 = QLabel("Página 1")
        self.pagina2 = QLabel("Página 2")

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.pagina1)
        self.stacked_layout.addWidget(self.pagina2)

        widget_central = QWidget()
        widget_central.setLayout(self.stacked_layout)
        self.setCentralWidget(widget_central)

        self.janela2 = JanelaSecundaria()
        self.janela2.trocar_pagina.connect(self.stacked_layout.setCurrentIndex)

        toolbar = self.addToolBar("Ferramentas")
        acao_janela2 = QAction("Janela 2", self)
        acao_janela2.triggered.connect(self.janela2.show)
        toolbar.addAction(acao_janela2)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
