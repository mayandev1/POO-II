import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q09 - Menu Ver com Modo Escuro")

        menuVer = self.menuBar().addMenu("Ver")

        acaoModoEscuro = QAction("Modo Escuro", self)
        acaoModoEscuro.setCheckable(True)
        menuVer.addAction(acaoModoEscuro)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
