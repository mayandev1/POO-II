import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QToolBar
from PySide6.QtGui import QAction

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        winget = QWidget()
        self.setCentralWidget(winget)
        
        layout = QVBoxLayout(winget)
        
        self.label = QLabel("Nenhuma ação realizada!")
        layout.addWidget(self.label)
        
        self.acaoSalvar = QAction("Salvar", self)
        
        toolbar = QToolBar()
        toolbar.addAction(self.acaoSalvar)
        self.addToolBar(toolbar)
        
        menu = self.menuBar().addMenu("Arquivo")
        
        acaoNovo = QAction("Novo", self)
        menu.addAction(acaoNovo)
        
        self.acaoSalvar.triggered.connect(self.atualizarLabel)
        
    def atualizarLabel(self):
        self.label.setText("Arquivo salvo!")
    
app = QApplication(sys.argv)

janela = mainWindow()
janela.show()

sys.exit(app.exec())       