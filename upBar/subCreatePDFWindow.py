from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QFrame, QSpinBox, QLabel, QHBoxLayout, QVBoxLayout, QCheckBox


class SubCreatePDFSetting(QFrame):
    def __init__(self, parent, args):
        super().__init__(parent)
        self.frame_main = QFrame(parent)
        self.frame_main.setGeometry(*args)
        self.frame_main.setStyleSheet('border-radius: 10px; background-color: rgba(0, 173, 181, 255)')
        self.frame_main.hide()

        self.widgets()


    def widgets(self):

        self.Hlayout_spinBox = QHBoxLayout()

        self.Vlayout = QVBoxLayout(self.frame_main)


    def returnSetting(self):
        return {}





