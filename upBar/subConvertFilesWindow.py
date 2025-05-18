from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QFrame, QSpinBox, QLabel, QHBoxLayout, QVBoxLayout, QCheckBox, QButtonGroup, QRadioButton

class SubConvertFilesWindow(QFrame):
    def __init__(self, parent, args):
        super().__init__(parent)
        self.frame_main = QFrame(parent)
        self.frame_main.setGeometry(*args)
        self.frame_main.setStyleSheet('border-radius: 10px; background-color: rgba(0, 173, 181, 255)')
        self.frame_main.hide()

        self.widgets()


    def widgets(self):
        self.Vlayout = QVBoxLayout(self.frame_main)

        self.mode_group = QButtonGroup(self.frame_main)
        
        self.single_page_radio = QRadioButton("Одна страница")
        self.single_page_radio.setChecked(True)
        self.mode_group.addButton(self.single_page_radio)
        
        self.range_radio = QRadioButton("Диапазон")
        self.mode_group.addButton(self.range_radio)
        
        self.Vlayout.addWidget(self.single_page_radio)
        self.Vlayout.addWidget(self.range_radio)

        self.single_page_layout = QHBoxLayout()
        self.label_single_page = QLabel('Страница:')
        self.spinBox_single = QSpinBox()
        self.spinBox_single.setSingleStep(1)
        self.spinBox_single.setMinimum(1)
        self.spinBox_single.setValue(1)
        self.spinBox_single.setFixedSize(60, 30)
        self.spinBox_single.setStyleSheet('background-color:white')
        
        self.single_page_layout.addWidget(self.label_single_page)
        self.single_page_layout.addWidget(self.spinBox_single)
        self.Vlayout.addLayout(self.single_page_layout)

        self.range_layout = QHBoxLayout()
        self.label_range_start = QLabel('От:')
        self.spinBox_start = QSpinBox()
        self.spinBox_start.setSingleStep(1)
        self.spinBox_start.setMinimum(1)
        self.spinBox_start.setValue(1)
        self.spinBox_start.setFixedSize(60, 30)
        self.spinBox_start.setStyleSheet('background-color:white')
        
        self.label_range_end = QLabel('До:')
        self.spinBox_end = QSpinBox()
        self.spinBox_end.setSingleStep(1)
        self.spinBox_end.setMinimum(1)
        self.spinBox_end.setValue(1)
        self.spinBox_end.setFixedSize(60, 30)
        self.spinBox_end.setStyleSheet('background-color:white')
        
        self.range_layout.addWidget(self.label_range_start)
        self.range_layout.addWidget(self.spinBox_start)
        self.range_layout.addWidget(self.label_range_end)
        self.range_layout.addWidget(self.spinBox_end)
        self.Vlayout.addLayout(self.range_layout)

        self.range_layout.setEnabled(False)
        self.label_range_start.setVisible(False)
        self.spinBox_start.setVisible(False)
        self.label_range_end.setVisible(False)
        self.spinBox_end.setVisible(False)

        self.single_page_radio.toggled.connect(self.update_mode)
        self.spinBox_single.valueChanged.connect(self.sync_range_start)
        self.spinBox_start.valueChanged.connect(self.validate_range)
        self.spinBox_end.valueChanged.connect(self.validate_range)


    def update_mode(self, checked):
        if checked:
            self.single_page_layout.setEnabled(True)
            self.label_single_page.setVisible(True)
            self.spinBox_single.setVisible(True)
            
            self.range_layout.setEnabled(False)
            self.label_range_start.setVisible(False)
            self.spinBox_start.setVisible(False)
            self.label_range_end.setVisible(False)
            self.spinBox_end.setVisible(False)
        else:
            self.single_page_layout.setEnabled(False)
            self.label_single_page.setVisible(False)
            self.spinBox_single.setVisible(False)
            
            self.range_layout.setEnabled(True)
            self.label_range_start.setVisible(True)
            self.spinBox_start.setVisible(True)
            self.label_range_end.setVisible(True)
            self.spinBox_end.setVisible(True)
            
            self.spinBox_start.setValue(self.spinBox_single.value())


    def sync_range_start(self, value):
        if self.spinBox_start.value() < value:
            self.spinBox_start.setValue(value)
        if self.spinBox_end.value() < value:
            self.spinBox_end.setValue(value)


    def validate_range(self):
        if self.spinBox_start.value() > self.spinBox_end.value():
            self.spinBox_end.setValue(self.spinBox_start.value())


    def getSetting(self):
        if self.single_page_radio.isChecked():
            return {'mode': 'single', 'page': self.spinBox_single.value() - 1}
        else:
            return {
                'mode': 'range',
                'start': self.spinBox_start.value() - 1,
                'end': self.spinBox_end.value() - 1
            }