import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QToolBar
from PySide6.QtGui import QAction

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        winget = QWidget()
        self.setCentralWidget(winget)
        
        layout = QGridLayout(winget)
        
        self.label = QLabel("Widget visível!")
        layout.addWidget(self.label, 0, 0)
        
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        self.acaoVer = QAction("Mostrar Widget", self)
        self.acaoVer.setCheckable(True)
        self.acaoVer.setChecked(True)
        
        toolbar.addAction(self.acaoVer)
        
        menuVer = self.menuBar().addMenu("Ver")
        menuVer.addAction(self.acaoVer)
        
        self.acaoVer.toggled.connect(self.mostrarWidget)
        
    def mostrarWidget(self, estado):
        self.label.setVisible(estado) 
        
app = QApplication(sys.argv)

janela = mainWindow()
janela.show()

sys.exit(app.exec())       