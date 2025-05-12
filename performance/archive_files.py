from PyQt5.QtWidgets import QWidget, QFrame, QMainWindow, QLineEdit, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class CreateArchive(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint)
        self.setWindowModality(Qt.ApplicationModal)  
        self.setWindowTitle("Создание архива")
        self.setFixedSize(400, 500)
        self.widgets()
        self.show()

    def widgets(self):
        # central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # main layout 
        layout_main = QVBoxLayout(central_widget)
        self.frame_mainFrame = QFrame()
        self.frame_mainFrame.setStyleSheet("""
    background: qlineargradient(
        x1:0, y1:0, x2:1, y2:1,
        stop:0 #ffaf4b, 
        stop:1 #ff7b54
    );
    border-radius: 8px;
""")
        label_nameArch = QLabel(self.frame_mainFrame)
        label_nameArch.setText('Имя архива:')
        label_nameArch.setStyleSheet("""
            background-color: transparent;
            border: 1px solid white;
            border-radius: 5px;
            font-size: 14px;
            color: white;
        """)
        label_nameArch.setGeometry(10, 5, 150, 25)

        lineEdit_nameArch = QLineEdit(self.frame_mainFrame)
        lineEdit_nameArch.setStyleSheet("""
            background-color: transparent;
            border: 1px solid white;
            border-radius: 5px;
            font-size: 14px;
            color: white;
        """)
        lineEdit_nameArch.setGeometry(10, 35, 360, 25)
        layout_main.addWidget(self.frame_mainFrame)