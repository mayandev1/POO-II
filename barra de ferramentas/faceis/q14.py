import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q14 - Toolbar com Ação que Muda Texto")

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.acaoAlternar = QAction("Ativar", self)
        toolbar.addAction(self.acaoAlternar)

        self.acaoAlternar.triggered.connect(self.alternarTexto)

    def alternarTexto(self):
        if self.acaoAlternar.text() == "Ativar":
            self.acaoAlternar.setText("Desativar")
        else:
            self.acaoAlternar.setText("Ativar")


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())
