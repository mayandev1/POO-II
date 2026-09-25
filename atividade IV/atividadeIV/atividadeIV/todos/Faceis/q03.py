# 3. Configure QGridLayout, QToolBar com "Alert", menu "Editar",
# clique em QAction mostra QMessageBox.question e, se Yes, abre QDialog.
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QDialog, QMessageBox
)
from PySide6.QtGui import QAction


class DialogoConfirmado(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Confirmado")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        layout = QGridLayout()
        layout.addWidget(QLabel("Aplicação com QGridLayout"), 0, 0)

        widget_central = QWidget()
        widget_central.setLayout(layout)
        self.setCentralWidget(widget_central)

        toolbar = self.addToolBar("Ferramentas")
        acao_alert = QAction("Alert", self)
        acao_alert.triggered.connect(self.perguntar)
        toolbar.addAction(acao_alert)

        menu = self.menuBar()
        menu.addMenu("Editar")

    def perguntar(self):
        resposta = QMessageBox.question(
            self, "Confirmação", "Deseja continuar?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if resposta == QMessageBox.StandardButton.Yes:
            dialogo = DialogoConfirmado(self)
            dialogo.exec()


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
