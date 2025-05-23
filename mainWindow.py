from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QFrame, QLineEdit, QWidget, QPushButton, QDesktopWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from tkinter import filedialog

from imageButton.createImageBlock import CreateImageBlock
from upBar.workBar import WorkBar
from workZone import WorkZone
from flowLayout import FlowLayout
from performance.archive_files import CreateArchive


class MainWindow(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Zim')
        self.setGeometry(100, 100, 1000, 700)
        self.setMinimumSize(1000, 700)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.list_imageBlock = []
        self.files = []
    
    def initUI(self):
        # main widget
        self.main_widget = QWidget(self)
        self.main_widget.setStyleSheet('background-color: rgba(0, 173, 181, 150)')
        self.setCentralWidget(self.main_widget)

        # work bar
        self.workBar = WorkBar(self).frame_workBar

        # work zone
        self.workZone = WorkZone(self).label_workZone

        # layout
        self.Vlayout = QVBoxLayout(self.main_widget)
        self.flowLayout = FlowLayout(self.workZone)  

        # menu bar
        self.menu = self.menuBar()  
        file_menu = self.menu.addMenu('Файл')
        file_action = self.menu.addMenu('Выполнить')
        # file
        open_file = QAction('Открыть', self)
        open_file.triggered.connect(self.openFileWindow)
        self.open_compress = QAction('Создать архив', self)
        self.open_compress.triggered.connect(self.createArchive)
        self.open_compress.setEnabled(False)

        # action
        file_menu.addAction(open_file)
        file_action.addAction(self.open_compress)

        # add layout
        self.Vlayout.addWidget(self.workBar)
        self.Vlayout.addWidget(self.workZone)
       

    def openFileWindow(self):
        files = filedialog.askopenfilenames(title="Выберите изображения", filetypes=[("Image Files", "*.jpg *.jpeg *.pdf"), ("PDF files", "*.pdf"), ("All Files", "*.*")])
        if files:
            for i in range(len(files)):
                block = CreateImageBlock(self, files[i])
                self.list_imageBlock.append(block)
                self.flowLayout.addWidget(block.button_container)
            self.open_compress.setEnabled(True)


    def createArchive(self):
        self.archive_window = CreateArchive(self)


    def getFiles(self):
        return [i.returnImageInfo() for i in self.list_imageBlock]


    def run(self):
        self.initUI()
        self.show()
        