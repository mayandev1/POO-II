# 3. Crie QMessageBox.question() perguntando "Deseja sair?" com Yes/No.
import sys
from PySide6.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)

resposta = QMessageBox.question(
    None, "Sair", "Deseja sair?",
    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
)

if resposta == QMessageBox.StandardButton.Yes:
    print("Usuário deseja sair")
else:
    print("Usuário deseja continuar")
