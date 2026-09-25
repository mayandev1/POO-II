# 9. Use QMessageBox.about() com informacoes da aplicacao.
import sys
from PySide6.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)

QMessageBox.about(None, "Sobre o Aplicativo", "Aplicativo de exemplo\nVersão 1.0\nDesenvolvido para a disciplina POO-II.")
