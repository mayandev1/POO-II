# 1. QMainWindow com QVBoxLayout, QToolBar ("Nova Janela"), menu "Arquivo > Abrir Dialogo",
# ao clicar abre QDialog com QMessageBox de boas-vindas e sinal que atualiza QLabel da principal.
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QLabel, QVBoxLayout, QWidget,
    QPushButton, QMessageBox
)
from PySide6.QtGui import QAction
from PySide6.QtCore import Signal


class MeuDialogo(QDialog):
    dados_confirmados = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Diálogo de boas-vindas")

        botao = QPushButton("Confirmar")
        botao.clicked.connect(self.confirmar)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Bem-vindo(a)!"))
        layout.addWidget(botao)
        self.setLayout(layout)

    def confirmar(self):
        QMessageBox.information(self, "Boas-vindas", "Seja bem-vindo(a) à aplicação!")
        self.dados_confirmados.emit("Diálogo confirmado com sucesso!")
        self.accept()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        self.label_status = QLabel("Aguardando ação...")

        layout = QVBoxLayout()
        layout.addWidget(self.label_status)

        widget_central = QWidget()
        widget_central.setLayout(layout)
        self.setCentralWidget(widget_central)

        toolbar = self.addToolBar("Barra de ferramentas")
        acao_nova_janela = QAction("Nova Janela", self)
        toolbar.addAction(acao_nova_janela)

        menu = self.menuBar()
        menu_arquivo = menu.addMenu("Arquivo")
        acao_abrir_dialogo = QAction("Abrir Diálogo", self)
        acao_abrir_dialogo.triggered.connect(self.abrir_dialogo)
        menu_arquivo.addAction(acao_abrir_dialogo)

    def abrir_dialogo(self):
        dialogo = MeuDialogo(self)
        dialogo.dados_confirmados.connect(self.atualizar_label)
        dialogo.exec()

    def atualizar_label(self, texto):
        self.label_status.setText(texto)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
