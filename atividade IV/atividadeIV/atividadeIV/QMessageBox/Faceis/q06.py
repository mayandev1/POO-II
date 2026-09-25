# 6. Adicione QMessageBox com texto formatado em HTML simples.
import sys
from PySide6.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)

caixa = QMessageBox()
caixa.setWindowTitle("Texto HTML")
caixa.setText("<h3>Título em HTML</h3><p>Este é um texto em <b>negrito</b> e <i>itálico</i>.</p>")
caixa.exec()
