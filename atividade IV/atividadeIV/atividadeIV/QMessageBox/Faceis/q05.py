# 5. Use exec() em QMessageBox e verifique o botao clicado.
import sys
from PySide6.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)

caixa = QMessageBox()
caixa.setWindowTitle("Confirmação")
caixa.setText("Deseja continuar?")
caixa.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

botao_clicado = caixa.exec()

if botao_clicado == QMessageBox.StandardButton.Yes:
    print("Botão clicado: Yes")
else:
    print("Botão clicado: No")
