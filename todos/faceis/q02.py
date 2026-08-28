import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QToolBar
from PySide6.QtGui import QAction

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        winget = QWidget()
        self.setCentralWidget(winget)
        
        layout = QVBoxLayout(winget)
        
        self.lineEdit = QLineEdit()
        layout.addWidget(self.lineEdit)
        
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        acaoAbrir = QAction("Abrir", self)
        toolbar.addAction(acaoAbrir)
        
        menuEditar = self.menuBar().addMenu("Editar")
        
    def keyPressEvent(self, event):
        tecla = event.text()
        
        if tecla: 
            self.lineEdit.setText(tecla)
            
app = QApplication(sys.argv)

janela = mainWindow()
janela.show()

sys.exit(app.exec())       