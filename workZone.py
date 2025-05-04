from PyQt5.QtWidgets import QWidget, QFrame

from style.styleWidgets import style_frame_workZone

class WorkZone(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.widgets()

    def widgets(self):
        self.frame_workZone = QFrame(self.parent.main_widget)
        self.frame_workZone.setStyleSheet(style_frame_workZone)
