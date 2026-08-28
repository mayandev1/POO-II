import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q06 - Submenu Exportar")

        menuArquivo = self.menuBar().addMenu("Arquivo")

        submenuExportar = menuArquivo.addMenu("Exportar")

        acaoPdf = QAction("Exportar como PDF", self)
        submenuExportar.addAction(acaoPdf)

        acaoExcel = QAction("Exportar como Excel", self)
        submenuExportar.addAction(acaoExcel)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
