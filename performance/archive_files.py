from PyQt5.QtWidgets import QWidget, QFrame, QMainWindow, QLineEdit, QLabel, QVBoxLayout, QCheckBox, QSlider, QPushButton
from PyQt5.QtCore import Qt
from tkinter import filedialog
import pyminizip

from style.styleWidgets import style_frame_mainFrame, style_label_nameArch, style_lineEdit_nameArch, style_checkbox_compress_files, style_checkbox_setPassword, style_button_startArchive

class CreateArchive(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowModality(Qt.ApplicationModal)  
        self.setWindowTitle("Создание архива")
        self.setFixedSize(400, 210)
        self.setStyleSheet('background-color: rgba(0, 173, 181, 150)')
        self.widgets()
        self.show()

    def widgets(self):
        # central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # layouts
        layout_Vmain = QVBoxLayout(central_widget)

        # main frame
        self.frame_mainFrame = QFrame()
        self.frame_mainFrame.setStyleSheet(style_frame_mainFrame)

        # label name archive
        label_nameArch = QLabel(self.frame_mainFrame)
        label_nameArch.setText('Имя архива:')
        label_nameArch.setGeometry(10, 10, 100, 25)
        label_nameArch.setStyleSheet(style_label_nameArch)

        self.lineEdit_nameArch = QLineEdit(self.frame_mainFrame)
        self.lineEdit_nameArch.setGeometry(10, 40, 360, 25)
        self.lineEdit_nameArch.setStyleSheet(style_lineEdit_nameArch)

        # checkBox for quality
        self.checkbox_compress_files = QCheckBox(self.frame_mainFrame)
        self.checkbox_compress_files.setText('Уменьшить размер')
        self.checkbox_compress_files.setChecked(False) 
        self.checkbox_compress_files.setGeometry(10, 70, 170, 25)
        self.checkbox_compress_files.setStyleSheet(style_checkbox_compress_files)

        # widgets quality
        self.slider_quality = QSlider(self.frame_mainFrame,
        orientation=Qt.Horizontal)
        self.slider_quality.setRange(0, 100)
        self.slider_quality.setValue(100)
        self.slider_quality.setGeometry(10, 100, 150, 25)
        self.slider_quality.setStyleSheet('background-color: transparent;')
        self.slider_quality.hide()

        self.label_valueSlider = QLabel(self.frame_mainFrame)
        self.label_valueSlider.setText(str(self.slider_quality.value()))
        self.label_valueSlider.setGeometry(165, 100, 150, 25)
        self.label_valueSlider.setStyleSheet('color: white; background: transparent')
        self.label_valueSlider.hide()

        # checkBox for password
        self.checkbox_setPassword = QCheckBox(self.frame_mainFrame)
        self.checkbox_setPassword.setText('Установить пароль')
        self.checkbox_setPassword.setChecked(False) 
        self.checkbox_setPassword.setGeometry(205, 70, 160, 25)
        self.checkbox_setPassword.setStyleSheet(style_checkbox_setPassword)

        # lineEdit password
        self.lineEdit_password = QLineEdit(self.frame_mainFrame)
        self.lineEdit_password.setPlaceholderText('Пароль')
        self.lineEdit_password.setGeometry(200, 100, 160, 25)
        self.lineEdit_password.setStyleSheet(style_lineEdit_nameArch)
        self.lineEdit_password.hide()

        # button start
        self.button_startArchive = QPushButton(self.frame_mainFrame)
        self.button_startArchive.setText('Архивировать')
        self.button_startArchive.setGeometry(115, 155, 160, 25)
        self.button_startArchive.setStyleSheet(style_button_startArchive)

        # add layout
        layout_Vmain.addWidget(self.frame_mainFrame)

        # connect
        self.slider_quality.valueChanged.connect(lambda value: self.label_valueSlider.setText(str(value)))
        self.checkbox_compress_files.stateChanged.connect(self.correctQuality)
        self.checkbox_setPassword.stateChanged.connect(self.setPassword)
        self.button_startArchive.pressed.connect(self.startArchive)

    
    def startArchive(self):
        path_folder = filedialog.askdirectory(title="Сохранить в")
        if not path_folder:
            return 0 
        full_path = path_folder+'/'+self.lineEdit_nameArch.text()+'.zip'
        files = [i['path'] for i in self.parent.getFiles()]
        if self.checkbox_setPassword.isChecked():
            pyminizip.compress_multiple(files, [], full_path, self.lineEdit_password.text(), 5)
        else:
            pyminizip.compress_multiple(files, [], full_path, None, 5)


    def correctQuality(self, state):
        if state == Qt.Checked:
            self.slider_quality.show()
            self.label_valueSlider.show()
        elif state == Qt.Unchecked:
            self.slider_quality.hide()
            self.label_valueSlider.hide()


    def setPassword(self, state):
        if state == Qt.Checked:
            self.lineEdit_password.show()
        elif state == Qt.Unchecked:
            self.lineEdit_password.hide()



