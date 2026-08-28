import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QToolBar
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        layout = QVBoxLayout(widget)

        self.label = QLabel("Janela aberta")
        layout.addWidget(self.label)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        acaoImprimir = QAction("Imprimir", self)
        toolbar.addAction(acaoImprimir)

        menu = self.menuBar().addMenu("Arquivo")
        menu.addAction(acaoImprimir)

    def closeEvent(self, event):
        print("Janela fechada")
        event.accept()


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

sys.exit(app.exec())