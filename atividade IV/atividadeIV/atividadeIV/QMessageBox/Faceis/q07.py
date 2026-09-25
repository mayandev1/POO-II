# 7. Crie alerta com setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel).
import sys
from PySide6.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)

caixa = QMessageBox()
caixa.setWindowTitle("Alerta")
caixa.setText("Confirma a ação?")
caixa.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
caixa.exec()
