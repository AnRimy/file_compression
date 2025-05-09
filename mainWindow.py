from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QFrame, QLineEdit, QWidget, QPushButton, QDesktopWidget, QVBoxLayout, QHBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from tkinter import filedialog

from imageButton.createImageBlock import CreateImageBlock
from upBar.workBar import WorkBar
from workZone import WorkZone


class MainWindow(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Zim')
        self.setGeometry(100, 100, 1000, 700)
        self.setMinimumSize(1000, 700)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.list_imageBlock = []
        self.files = None
    
    def initUI(self):
        # main widget
        self.main_widget = QWidget(self)
        self.main_widget.setStyleSheet('background-color: rgba(0, 173, 181, 150)')
        self.setCentralWidget(self.main_widget)

        # work bar
        self.workBar = WorkBar(self).frame_workBar

        # work zone
        self.workZone = WorkZone(self).frame_workZone

        # layout
        self.Vlayout = QVBoxLayout(self.main_widget)
        self.Hlayout = QHBoxLayout(self.workZone)

        # menu bar
        self.menu = self.menuBar()  
        file_menu = self.menu.addMenu('Файл')
        open_file = QAction('Открыть', self)
        open_file.triggered.connect(self.openFileWindow)
        send_print = QAction('Печать', self)
        send_print.triggered.connect(self.sendPrint)
        open_setting = QAction('Настройки', self)
        open_setting.triggered.connect(self.openSetting)

        file_menu.addAction(open_file)
        file_menu.addAction(send_print)
        file_menu.addAction(open_setting)

        # add layout
        self.Vlayout.addWidget(self.workBar)
        self.Vlayout.addWidget(self.workZone)
       

    def openFileWindow(self):
        files = filedialog.askopenfilenames(title="Выберите изображения", filetypes=[("Image Files", "*.jpg *.jpeg *.pdf"), ("All Files", "*.*")])
        if files:
            for i in range(len(files)):
                block = CreateImageBlock(self, files[i])
                self.list_imageBlock.append(block)
                self.Hlayout.addWidget(block.button_container, alignment=Qt.AlignTop | Qt.AlignLeft)


    def openSetting(self):
        pass


    def sendPrint(self):
        pass


    def returnFiles(self):
        return [i.returnImageInfo() for i in self.list_imageBlock]


    def run(self):
        self.initUI()
        self.show()
        