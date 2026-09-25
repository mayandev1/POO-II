# 14. Crie QMessageBox com setDetailedText("Log completo...").
import sys
from PySide6.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)

caixa = QMessageBox()
caixa.setWindowTitle("Detalhes")
caixa.setText("Ocorreu um problema durante a execução.")
caixa.setDetailedText("Log completo...\nLinha 1: erro X\nLinha 2: erro Y")
caixa.exec()
