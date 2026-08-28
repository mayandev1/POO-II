import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q12 - Menu com Ação que Imprime")

        menuArquivo = self.menuBar().addMenu("Arquivo")

        acaoNovo = QAction("Novo", self)
        menuArquivo.addAction(acaoNovo)

        acaoNovo.triggered.connect(self.criarNovo)

    def criarNovo(self):
        print("Novo arquivo criado")


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
