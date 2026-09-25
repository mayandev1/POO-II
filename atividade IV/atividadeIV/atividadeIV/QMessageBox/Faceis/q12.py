# 12. Use QMessageBox com botao "Sim", "Nao" e "Cancelar".
import sys
from PySide6.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)

caixa = QMessageBox()
caixa.setWindowTitle("Salvar alterações")
caixa.setText("Deseja salvar as alterações antes de sair?")
caixa.setStandardButtons(
    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel
)
caixa.setButtonText(QMessageBox.StandardButton.Yes, "Sim")
caixa.setButtonText(QMessageBox.StandardButton.No, "Não")
caixa.setButtonText(QMessageBox.StandardButton.Cancel, "Cancelar")

resultado = caixa.exec()
print("Resultado:", resultado)
