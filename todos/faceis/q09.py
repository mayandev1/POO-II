import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QStackedLayout,
    QLabel,
    QToolBar
)
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        layout = QVBoxLayout(widget)

        self.stacked = QStackedLayout()
        layout.addLayout(self.stacked)

        pagina1 = QWidget()
        layout1 = QVBoxLayout(pagina1)
        layout1.addWidget(QLabel("Página 1"))

        pagina2 = QWidget()
        layout2 = QVBoxLayout(pagina2)
        layout2.addWidget(QLabel("Página 2"))

        self.stacked.addWidget(pagina1)
        self.stacked.addWidget(pagina2)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        acaoPagina1 = QAction("Página 1", self)
        toolbar.addAction(acaoPagina1)

        menu = self.menuBar().addMenu("Navegação")
        menu.addAction(acaoPagina1)

        acaoPagina1.triggered.connect(self.irPagina1)

    def irPagina1(self):
        self.stacked.setCurrentIndex(0)

    def resizeEvent(self, event):
        self.stacked.setGeometry(self.centralWidget().rect())
        event.accept()


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())