# 15. Use information() com timeout simulado via QTimer.
import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import QTimer

app = QApplication(sys.argv)

caixa = QMessageBox()
caixa.setWindowTitle("Aviso temporário")
caixa.setText("Esta mensagem fechará automaticamente em 3 segundos.")
caixa.setStandardButtons(QMessageBox.StandardButton.Ok)

# QTimer dispara o fechamento automatico apos 3000 ms
QTimer.singleShot(3000, caixa.close)

caixa.exec()
