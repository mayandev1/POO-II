# 10. Use QHBoxLayout, menu "Ver > Alerta", clique mostra QMessageBox e abre janela
# secundaria com QLabel atualizado via slot.
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel, QMessageBox
)
from PySide6.QtGui import QAction
from PySide6.QtCore import Signal


class JanelaSecundaria(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Secundária")
        self.label = QLabel("Aguardando atualização...")
        self.setCentralWidget(self.label)

    def atualizar(self, texto):
        self.label.setText(texto)


class MainWindow(QMainWindow):
    atualizar_secundaria = Signal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        layout = QHBoxLayout()
        layout.addWidget(QLabel("Aplicação principal"))

        widget_central = QWidget()
        widget_central.setLayout(layout)
        self.setCentralWidget(widget_central)

        self.janela_secundaria = JanelaSecundaria()
        self.atualizar_secundaria.connect(self.janela_secundaria.atualizar)

        menu = self.menuBar()
        menu_ver = menu.addMenu("Ver")
        acao_alerta = QAction("Alerta", self)
        acao_alerta.triggered.connect(self.mostrar_alerta)
        menu_ver.addAction(acao_alerta)

    def mostrar_alerta(self):
        QMessageBox.information(self, "Alerta", "Alerta exibido! Abrindo janela secundária.")
        self.janela_secundaria.show()
        self.atualizar_secundaria.emit("Atualizado pela janela principal!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
