# 7. Crie QDialog com QLineEdit, botao OK mostra QMessageBox e fecha, enviando texto
# via sinal para QLabel da principal.
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QLineEdit, QPushButton, QVBoxLayout,
    QMessageBox, QLabel
)
from PySide6.QtCore import Signal


class MeuDialogo(QDialog):
    texto_enviado = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Digite um texto")

        self.campo = QLineEdit()
        botao_ok = QPushButton("OK")
        botao_ok.clicked.connect(self.confirmar)

        layout = QVBoxLayout()
        layout.addWidget(self.campo)
        layout.addWidget(botao_ok)
        self.setLayout(layout)

    def confirmar(self):
        QMessageBox.information(self, "Confirmado", "Texto enviado com sucesso!")
        self.texto_enviado.emit(self.campo.text())
        self.accept()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        self.label = QLabel("Nenhum texto recebido ainda.")
        self.setCentralWidget(self.label)

        self.botao_abrir = QPushButton("Abrir diálogo", self)
        self.botao_abrir.move(0, 40)
        self.botao_abrir.clicked.connect(self.abrir_dialogo)

    def abrir_dialogo(self):
        dialogo = MeuDialogo(self)
        dialogo.texto_enviado.connect(self.label.setText)
        dialogo.exec()


app = QApplication(sys.argv)

window = MainWindow()
window.botao_abrir.show()
window.show()
app.exec()
