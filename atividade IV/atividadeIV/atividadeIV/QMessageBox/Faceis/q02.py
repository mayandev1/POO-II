# 2. Use QMessageBox.warning() com botao OK.
import sys
from PySide6.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)

QMessageBox.warning(None, "Atenção", "Isso é um aviso.", QMessageBox.StandardButton.Ok)
