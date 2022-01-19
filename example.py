from PySide6.QtWidgets import QApplication, QMainWindow, \
    QLabel, QLineEdit, QWidget, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


app = QApplication()
window = MainWindow()
window.show()
app.exec_()