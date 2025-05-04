from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PIL import Image

from performance.convertPDFtoPNG import convertPDFtoPNG
from imageButton.bigWindowImage import BigWindow
from style.styleWidgets import style_button_block, style_button_delete, style_label_expension

class CreateImageBlock(QWidget):
    def __init__(self, parent, imagePath):
        super().__init__(parent)
        self.parent = parent
        self.imagePath = imagePath
        self.widgets()

    def widgets(self):
        # main button widget
        self.button_block = QPushButton(self.parent.workZone)
        self.button_block.setFixedSize(80, 110)
        expen = self.imagePath.split('.')[-1]
        if expen == 'pdf':
            self.image_pixmap = convertPDFtoPNG(self.imagePath)
        else:
            self.image_pixmap = QPixmap(self.imagePath)

        self.button_block.setIcon(QIcon(self.image_pixmap))
        self.button_block.setIconSize(QSize(66, 96))
        self.button_block.setStyleSheet(style_button_block)

        # button remove object
        self.button_delete = QPushButton(self.button_block)
        self.button_delete.setGeometry(3, 3, 20, 20)
        self.button_delete.setStyleSheet(style_button_delete)

        # label form
        self.label_expension = QLabel(self.button_block)
        self.label_expension.setGeometry(57, 3, 20, 20)
        self.label_expension.setText(expen)
        self.label_expension.setStyleSheet(style_label_expension)

        # connect button
        self.button_block.clicked.connect(self.clickButton)
        self.button_delete.clicked.connect(self.destroy)


    def clickButton(self):
        BigWindow(self, self.parent, self.imagePath, self.image_pixmap) 


    def returnImageInfo(self):
        return {'pixmap': self.image_pixmap,
        'path': self.imagePath}


    def setImageInBlock(self, image_pixmap):
        self.button_block.setIcon(QIcon(image_pixmap))
        self.image_pixmap = image_pixmap


    def destroy(self):
        self.parent.list_imageBlock.remove(self)
        self.parent.layout().removeWidget(self.button_block)
        self.button_block.deleteLater()
        self.deleteLater()

