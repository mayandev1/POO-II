import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q13 - Submenu Recente")

        menuArquivo = self.menuBar().addMenu("Arquivo")

        submenuRecente = menuArquivo.addMenu("Recente")

        arquivosRecentes = ["documento1.txt", "documento2.txt", "documento3.txt"]

        for nomeArquivo in arquivosRecentes:
            acaoArquivo = QAction(nomeArquivo, self)
            submenuRecente.addAction(acaoArquivo)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
