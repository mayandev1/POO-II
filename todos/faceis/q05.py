import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QToolBar
from PySide6.QtGui import QAction
from PySide6.QtCore import Signal, QEvent

class MainWindow(QMainWindow):
    inserirSinal = Signal()

    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        layout = QVBoxLayout(widget)

        self.tabela = QTableWidget(0, 2)
        self.tabela.setHorizontalHeaderLabels(["Nome", "Valor"])
        layout.addWidget(self.tabela)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        acaoAdicionar = QAction("Adicionar", self)
        toolbar.addAction(acaoAdicionar)

        menu = self.menuBar().addMenu("Arquivo")
        menu.addAction(acaoAdicionar)

        acaoAdicionar.triggered.connect(self.inserir)
        self.inserirSinal.connect(self.inserir)

    def mousePressEvent(self, event):
        if event.type() == QEvent.MouseButtonPress:
            self.inserirSinal.emit()

    def inserir(self):
        linha = self.tabela.rowCount()
        self.tabela.insertRow(linha)
        self.tabela.setItem(linha, 0, QTableWidgetItem("Novo"))
        self.tabela.setItem(linha, 1, QTableWidgetItem("0"))


from PySide6.QtWidgets import QTableWidgetItem

app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())