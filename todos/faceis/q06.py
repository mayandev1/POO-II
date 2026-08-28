import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QTextEdit, QToolBar
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        layout = QHBoxLayout(widget)

        self.textEdit = QTextEdit()
        layout.addWidget(self.textEdit)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        acaoCopiar = QAction("Copiar", self)
        toolbar.addAction(acaoCopiar)

        menu = self.menuBar().addMenu("Editar")
        menu.addAction(acaoCopiar)

        self.textEdit.textChanged.connect(self.atualizarTexto)
        acaoCopiar.triggered.connect(self.copiarTexto)

    def atualizarTexto(self):
        print(self.textEdit.toPlainText())

    def copiarTexto(self):
        self.textEdit.copy()


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())