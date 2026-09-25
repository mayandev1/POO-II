# 8. Configure QVBoxLayout + QToolBar, menu "Arquivo > Sair" mostra QMessageBox.confirm
# e, se sim, fecha todas janelas.
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QMessageBox
)
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Aplicação principal"))

        widget_central = QWidget()
        widget_central.setLayout(layout)
        self.setCentralWidget(widget_central)

        self.addToolBar("Ferramentas")

        menu = self.menuBar()
        menu_arquivo = menu.addMenu("Arquivo")
        acao_sair = QAction("Sair", self)
        acao_sair.triggered.connect(self.confirmar_saida)
        menu_arquivo.addAction(acao_sair)

    def confirmar_saida(self):
        resposta = QMessageBox.question(
            self, "Sair", "Deseja realmente sair da aplicação?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if resposta == QMessageBox.StandardButton.Yes:
            QApplication.closeAllWindows()


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
