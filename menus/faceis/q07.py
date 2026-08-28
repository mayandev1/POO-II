import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q07 - Menu com Sobre")

        menuAjuda = self.menuBar().addMenu("Ajuda")

        acaoSobre = QAction("Sobre", self)
        menuAjuda.addAction(acaoSobre)

        acaoSobre.triggered.connect(self.mostrarSobre)

    def mostrarSobre(self):
        QMessageBox.information(self, "Sobre", "Aplicação feita com PySide6.")


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
