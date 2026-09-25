# 9. Adicione QAction "Dialogo" na toolbar que abre QDialog modal com alert dentro
# e evento closeEvent que atualiza statusBar.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PySide6.QtGui import QAction


class MeuDialogo(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Diálogo")

    def closeEvent(self, event):
        if self.parent() is not None:
            self.parent().statusBar().showMessage("Diálogo fechado.", 3000)
        event.accept()

    def showEvent(self, event):
        QMessageBox.information(self, "Alerta", "Diálogo aberto com sucesso!")
        super().showEvent(event)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.statusBar().showMessage("Pronto.")

        toolbar = self.addToolBar("Ferramentas")
        acao_dialogo = QAction("Diálogo", self)
        acao_dialogo.triggered.connect(self.abrir_dialogo)
        toolbar.addAction(acao_dialogo)

    def abrir_dialogo(self):
        dialogo = MeuDialogo(self)
        dialogo.exec()


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
