from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon, QPainter, QTransform

from style.styleWidgets import style_label_workZone

class WorkZone(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.widgets()

    def widgets(self):
        self.label_workZone = QLabel(self.parent.main_widget)
        pixmap_backgroundText = QPixmap('icon/background_text.png')
        self.label_workZone.setPixmap(pixmap_backgroundText)
        self.label_workZone.setAlignment(Qt.AlignCenter)
        self.label_workZone.setStyleSheet(style_label_workZone)
