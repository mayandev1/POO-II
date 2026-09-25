# 10. Configure setIconPixmap com um icone personalizado em QMessageBox.
import sys
from PySide6.QtWidgets import QApplication, QMessageBox, QStyle

app = QApplication(sys.argv)

caixa = QMessageBox()
caixa.setWindowTitle("Ícone personalizado")
caixa.setText("Esta mensagem usa um ícone customizado.")
# Usando um icone padrao do Qt como "personalizado", para nao depender de arquivo externo
icone = caixa.style().standardIcon(QStyle.StandardPixmap.SP_DialogApplyButton)
caixa.setIconPixmap(icone.pixmap(48, 48))
caixa.exec()
