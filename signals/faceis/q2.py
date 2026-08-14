from PySide6.QtWidgets import QPushButton, QApplication

app =  QApplication([])

botao = QPushButton("Click Here")

botao.click()

botao.show()
app.exec()
