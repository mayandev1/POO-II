# 4. Configure QMessageBox.critical() com icone de erro.
import sys
from PySide6.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)

QMessageBox.critical(None, "Erro", "Ocorreu um erro crítico!")
