from PyQt5.QtWidgets import QApplication
from mainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.run()
    app.exec()