from PyQt5.QtWidgets import QWidget, QFrame, QPushButton, QHBoxLayout
from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtGui import QIcon, QPixmap
import configparser

from performance.compress_files import compress
from performance.createCommonPDF import createOnePDF
from performance.convertImage import convertForMinuature, convertPDFtoJPG
from upBar.subCompressWindow import SubCompressingSetting
from upBar.subCreatePDFWindow import SubCreatePDFSetting
from style.styleWidgets import style_buttonProccessing, style_frame_workBar
from openMessageBox import messageBox

class MyButton(QPushButton):
    def __init__(self, workbar_instance, workFunc):
        super().__init__(workbar_instance)
        self.workbar_instance = workbar_instance
        self.workFunc = workFunc

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.workFunc()
        super().mousePressEvent(event)


class WorkBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        settingPerfomance = configparser.ConfigParser().read('settingPerfomance.ini')

        self.widgets()

    def widgets(self):
        # label work bar
        self.frame_workBar = QFrame(self.parent.main_widget)
        self.frame_workBar.setFixedHeight(70)
        self.frame_workBar.setStyleSheet(style_frame_workBar)

        # layout
        layout = QHBoxLayout(self.frame_workBar)

        # button for compress files
        sBtnCom = 50
        self.button_compressFiles = MyButton(self.frame_workBar, self.openSettingCompress)
        self.button_compressFiles.setFixedSize(sBtnCom, sBtnCom)
        self.button_compressFiles.setIcon(QIcon('icon/compression.png'))
        self.button_compressFiles.setIconSize(QSize(sBtnCom - 4, sBtnCom - 4))
        self.button_compressFiles.setStyleSheet(style_buttonProccessing)

        # button create PDF
        self.button_createPDF = MyButton(self.frame_workBar, self.openSettingCreatePDF)
        self.button_createPDF.setFixedSize(sBtnCom, sBtnCom)
        self.button_createPDF.setIcon(QIcon('icon/pdf.png'))
        self.button_createPDF.setIconSize(QSize(sBtnCom - 10, sBtnCom - 10))
        self.button_createPDF.setStyleSheet(style_buttonProccessing)

        # button convert
        self.button_convert = MyButton(self.frame_workBar, self.openSettingCreatePDF)
        self.button_convert.setFixedSize(sBtnCom, sBtnCom)
        self.button_convert.setIcon(QIcon('icon/noneImage.png'))
        self.button_convert.setIconSize(QSize(sBtnCom - 4, sBtnCom - 4))
        self.button_convert.setStyleSheet(style_buttonProccessing)

        # add layout
        layout.addWidget(self.button_compressFiles, alignment=Qt.AlignCenter)
        layout.addWidget(self.button_createPDF, alignment=Qt.AlignCenter)
        layout.addWidget(self.button_convert, alignment=Qt.AlignCenter)

        # connect button
        self.button_compressFiles.clicked.connect(self.startCompress)
        self.button_createPDF.clicked.connect(self.startCreatePDF)
        self.button_convert.clicked.connect(self.stertConvertFiles)

        # create setting windows
        QTimer.singleShot(0, self.get_button_position)

    def get_button_position(self):
        self.subCompressSetting = SubCompressingSetting(self.parent, 
                    (self.button_compressFiles.pos().x()+10, 
                    self.button_compressFiles.pos().y()+85, 
                    200, 
                    100))
        self.subCreatePDFSetting = SubCreatePDFSetting(self.parent, 
                    (self.button_createPDF.pos().x()+10, 
                    self.button_createPDF.pos().y()+85, 
                    200, 
                    100))
    
    # compress files
    def startCompress(self):
        files = self.parent.getFiles()
        setting = self.subCompressSetting.returnSetting()
        if files:
            if setting['autoReplace']:
                compress(files=files, 
                        quality=setting['quality'],
                        autoReplace=True)
            else:
                compress(files=files,
                        quality=setting['quality'])
        else:
            messageBox(image_path='icon/information.png', title='Отсутствие изображений', text='Выберите изображения')

    def openSettingCompress(self):
        if self.subCompressSetting.frame_main.isVisible():
            self.subCompressSetting.frame_main.hide()
        else:
            self.subCompressSetting.frame_main.show()

    # create PDF
    def startCreatePDF(self):
        files = self.parent.getFiles()
        if files:
            createOnePDF(files)
        else:
            messageBox(image_path='icon/information.png', title='Отсутствие изображений', text='Выберите изображения')

    def openSettingCreatePDF(self):
        if self.subCreatePDFSetting.frame_main.isVisible():
            self.subCreatePDFSetting.frame_main.hide()
        else:
            self.subCreatePDFSetting.frame_main.show()

    # convert files
    def stertConvertFiles(self):
        files = self.parent.getFiles()
        if files:   
            convertPDFtoJPG(files)
        else:
            messageBox(image_path='icon/information.png', title='Отсутствие изображений', text='Выберите изображения')


            


