import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q15 - Menu Janela com Minimizar")

        menuJanela = self.menuBar().addMenu("Janela")

        acaoMinimizar = QAction("Minimizar", self)
        menuJanela.addAction(acaoMinimizar)

        acaoMinimizar.triggered.connect(self.showMinimized)


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
