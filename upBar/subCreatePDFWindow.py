from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QFrame, QSlider, QLabel, QHBoxLayout, QVBoxLayout, QCheckBox


class SubCreatePDFSetting(QFrame):
    def __init__(self, parent, args):
        super().__init__(parent)
        self.frame_main = QFrame(parent)
        self.frame_main.setGeometry(*args)
        self.frame_main.setStyleSheet('border-radius: 10px; background-color: rgb(200, 200, 100)')
        self.frame_main.hide()

        self.widgets()

    def widgets(self):
        # layout for quality
        self.Hlayout_quality = QHBoxLayout()
        self.Hlayout_autoReplace = QHBoxLayout()

        self.Vlayout = QVBoxLayout(self.frame_main)

        # widgets for quality 
        self.slider_quality = QSlider()
        self.slider_quality.setOrientation(Qt.Horizontal)
        self.slider_quality.setRange(0, 100)
        self.slider_quality.setValue(70)
        self.slider_quality.setFixedSize(160, 25)

        self.label_valueSlider = QLabel()
        self.label_valueSlider.setText(str(self.slider_quality.value()))

        # checkBox for create folder
        self.label_textAutoReplace = QLabel()
        self.label_textAutoReplace.setText('ssss')
        self.checkBox_autoReplace = QCheckBox()

        # add layout
        self.Hlayout_quality.addWidget(self.slider_quality)
        self.Hlayout_quality.addWidget(self.label_valueSlider)

        self.Hlayout_autoReplace.addWidget(self.label_textAutoReplace, alignment=Qt.AlignCenter)
        self.Hlayout_autoReplace.addWidget(self.checkBox_autoReplace, alignment=Qt.AlignCenter)

        self.Vlayout.addLayout(self.Hlayout_quality)
        self.Vlayout.addLayout(self.Hlayout_autoReplace)


        # connect widgets
        self.slider_quality.valueChanged.connect(lambda value: self.label_valueSlider.setText(str(value)))

    def returnSetting(self):
        return {'quality': self.slider_quality.value(), 
        'autoReplace': self.checkBox_autoReplace.isChecked()}





