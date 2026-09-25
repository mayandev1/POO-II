# 14. Crie QDialog com icone via setWindowIcon.
import sys
from PySide6.QtWidgets import QApplication, QDialog, QStyle


class DialogoComIcone(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Diálogo com ícone")
        # Usando um icone padrao do proprio Qt, para nao depender de arquivo externo
        icone = self.style().standardIcon(QStyle.StandardPixmap.SP_MessageBoxInformation)
        self.setWindowIcon(icone)


app = QApplication(sys.argv)

dialogo = DialogoComIcone()
dialogo.exec()
