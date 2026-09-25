# 5. Adicione QPushButton em QDialog, ao aceitar mostra QMessageBox e emite sinal
# para QTableWidget na janela principal.
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QPushButton, QVBoxLayout,
    QMessageBox, QTableWidget, QTableWidgetItem
)
from PySide6.QtCore import Signal


class MeuDialogo(QDialog):
    linha_adicionada = Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Adicionar item")

        botao = QPushButton("Adicionar")
        botao.clicked.connect(self.adicionar)

        layout = QVBoxLayout()
        layout.addWidget(botao)
        self.setLayout(layout)

    def adicionar(self):
        QMessageBox.information(self, "Sucesso", "Item adicionado com sucesso!")
        self.linha_adicionada.emit("Item Exemplo", "Categoria Exemplo")
        self.accept()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        self.tabela = QTableWidget(0, 2)
        self.tabela.setHorizontalHeaderLabels(["Nome", "Categoria"])
        self.setCentralWidget(self.tabela)

        self.botao_abrir = QPushButton("Abrir diálogo", self)
        self.botao_abrir.clicked.connect(self.abrir_dialogo)

    def abrir_dialogo(self):
        dialogo = MeuDialogo(self)
        dialogo.linha_adicionada.connect(self.adicionar_linha)
        dialogo.exec()

    def adicionar_linha(self, nome, categoria):
        linha = self.tabela.rowCount()
        self.tabela.insertRow(linha)
        self.tabela.setItem(linha, 0, QTableWidgetItem(nome))
        self.tabela.setItem(linha, 1, QTableWidgetItem(categoria))


app = QApplication(sys.argv)

window = MainWindow()
window.botao_abrir.show()
window.show()
app.exec()
