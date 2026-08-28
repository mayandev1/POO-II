import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QStackedLayout, QLabel, QToolBar
from PySide6.QtGui import QAction

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        winget = QWidget()
        self.setCentralWidget(winget)
        
        layout = QVBoxLayout(winget)
        
        self.stacked = QStackedLayout()
        layout.addLayout(self.stacked)
        
        pagina1 = QWidget()
        layout1 = QVBoxLayout(pagina1)
        layout1.addWidget(QLabel("Página 1"))
        
        pagina2 = QWidget()
        layout2 = QVBoxLayout(pagina2)
        layout2.addWidget(QLabel("Página 2"))
        
        pagina3 = QWidget()
        layout3 = QVBoxLayout(pagina3)
        layout3.addWidget(QLabel("Página 3"))
        
        self.stacked.addWidget(pagina1)
        self.stacked.addWidget(pagina2)
        self.stacked.addWidget(pagina3)
        
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        acaoProxima = QAction("Próxima", self)
        toolbar.addAction(acaoProxima)
        
        menuNav = self.menuBar().addMenu("Navegação")
        menuNav.addAction(acaoProxima)
        
        acaoProxima.triggered.connect(self.proximaPag)
        self.stacked.currentChanged.connect(self.trocarPag)
        
    def proximaPag(self):
        atual = self.stacked.currentIndex()
        proxima = (atual + 1) % self.stacked.count()
        self.stacked.setCurrentIndex(proxima)
        
    def trocarPag(self, index):
        print("Página atual:", index)
        
        
app = QApplication(sys.argv)

janela = mainWindow()
janela.show()

sys.exit(app.exec())       