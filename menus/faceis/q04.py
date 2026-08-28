import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q04 - Menu Ajuda com Separador")

        menuAjuda = self.menuBar().addMenu("Ajuda")

        acaoSobre = QAction("Sobre", self)
        menuAjuda.addAction(acaoSobre)

        menuAjuda.addSeparator()

        acaoDocumentacao = QAction("Documentação", self)
        menuAjuda.addAction(acaoDocumentacao)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
