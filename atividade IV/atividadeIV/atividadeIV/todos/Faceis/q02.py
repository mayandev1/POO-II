# 2. Use QHBoxLayout, QAction no menu "Ajuda > Sobre" que mostra QMessageBox,
# e botao que abre janela secundaria simples.
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton, QMessageBox, QLabel
)
from PySide6.QtGui import QAction


class JanelaSecundaria(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Secundária")
        self.setCentralWidget(QLabel("Janela secundária simples."))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        self.janela_secundaria = JanelaSecundaria()

        botao = QPushButton("Abrir janela secundária")
        botao.clicked.connect(self.janela_secundaria.show)

        layout = QHBoxLayout()
        layout.addWidget(botao)

        widget_central = QWidget()
        widget_central.setLayout(layout)
        self.setCentralWidget(widget_central)

        menu = self.menuBar()
        menu_ajuda = menu.addMenu("Ajuda")
        acao_sobre = QAction("Sobre", self)
        acao_sobre.triggered.connect(self.mostrar_sobre)
        menu_ajuda.addAction(acao_sobre)

    def mostrar_sobre(self):
        QMessageBox.about(self, "Sobre", "Aplicação de exemplo - POO II.")


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
