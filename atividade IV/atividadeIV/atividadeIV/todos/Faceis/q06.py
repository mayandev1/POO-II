# 6. Use menu "Janela > Nova" que abre QMainWindow secundaria com QToolBar e botao
# que dispara QMessageBox.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PySide6.QtGui import QAction


class JanelaSecundaria(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nova Janela")

        toolbar = self.addToolBar("Ferramentas")

        botao = QPushButton("Mostrar alerta")
        botao.clicked.connect(self.mostrar_alerta)
        self.setCentralWidget(botao)

    def mostrar_alerta(self):
        QMessageBox.information(self, "Alerta", "Este é um alerta da janela secundária.")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        self.janela_secundaria = JanelaSecundaria()

        menu = self.menuBar()
        menu_janela = menu.addMenu("Janela")
        acao_nova = QAction("Nova", self)
        acao_nova.triggered.connect(self.janela_secundaria.show)
        menu_janela.addAction(acao_nova)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
