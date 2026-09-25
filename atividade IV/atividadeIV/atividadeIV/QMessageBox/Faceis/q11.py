# 11. Crie QMessageBox com titulo vazio e apenas texto.
import sys
from PySide6.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)

caixa = QMessageBox()
caixa.setWindowTitle("")
caixa.setText("Apenas uma mensagem, sem título.")
caixa.exec()
