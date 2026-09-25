# 1. Mostre QMessageBox.information() com titulo "Sucesso" e texto "Operacao concluida".
import sys
from PySide6.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)

QMessageBox.information(None, "Sucesso", "Operação concluída")
