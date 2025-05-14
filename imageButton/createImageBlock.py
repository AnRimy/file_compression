from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QLabel, QGraphicsBlurEffect, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QPainterPath, QRegion
from PIL import Image
from pathlib import Path

from performance.convertImage import convertForMinuature, convertPDFtoJPG
from imageButton.bigWindowImage import BigWindow
from style.styleWidgets import style_button_block, style_button_delete, style_label_textInfoImage,style_label_minuature


class ClickableWidget(QWidget):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)



class CreateImageBlock(QWidget):
    def __init__(self, parent, imagePath):
        super().__init__(parent)
        self.parent = parent
        self.imagePath = imagePath
        self.widgets()


    def widgets(self):
        # button container
        self.button_container = ClickableWidget(self.parent.workZone)
        self.button_container.setFixedSize(150, 100)
        path = QPainterPath()
        path.addRoundedRect(0, 0, 150, 100, 10, 10)
        self.button_container.setMask(QRegion(path.toFillPolygon().toPolygon()))

        # background 
        self.label_background = QLabel(self.button_container)
        self.label_background.setGeometry(0, 0, 150, 100)
        
        infoImage = self.getInfoImage(self.imagePath)
        if infoImage['expen'] == 'pdf':
            self.image_pixmap = convertForMinuature(self.imagePath)
        else:
            self.image_pixmap = QPixmap(self.imagePath)
        
        self.label_background.setPixmap(self.image_pixmap.scaled(200, 150))
        
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(10)
        self.label_background.setGraphicsEffect(blur_effect)
        
        # layout 
        HLayout = QHBoxLayout(self.button_container)
        HLayout.setContentsMargins(2, 2, 2, 2)  # Отступы: left, top, right, bottom
        HLayout.setSpacing(8)  # Равное расстояние между виджетами
        
        # Добавляем растягивающий элемент слева
        HLayout.addStretch(1)

        # miniature image 
        self.label_minuature = QLabel()
        self.label_minuature.setPixmap(self.image_pixmap.scaled(75, 70, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.label_minuature.setFixedSize(75, 70)
        self.label_minuature.setStyleSheet(style_label_minuature)
        
        # text info 
        self.label_textInfoImage = QLabel()
        self.label_textInfoImage.setFixedSize(68, 96)
        self.label_textInfoImage.setText(f"""name: {infoImage['name']+'.'+infoImage['expen']}\n
    size: {infoImage['size']:.2f}""")
        self.label_textInfoImage.setWordWrap(True)
        self.label_textInfoImage.setStyleSheet(style_label_textInfoImage)
        
        # add widgets
        HLayout.addWidget(self.label_minuature)
        HLayout.addWidget(self.label_textInfoImage)
        
        # Добавляем растягивающий элемент справа
        HLayout.addStretch(1)
        
        # delete button 
        self.button_delete = QPushButton(self.label_textInfoImage)
        self.button_delete.setFixedSize(20, 20)
        self.button_delete.move(45, 3)
        self.button_delete.setStyleSheet(style_button_delete)

        # connect button
        self.button_container.clicked.connect(self.clickButton)
        self.button_delete.clicked.connect(self.destroy)


    def clickButton(self):
        BigWindow(self, self.parent, self.imagePath, self.image_pixmap) 


    def returnImageInfo(self):
        return {'pixmap': self.image_pixmap,
        'path': self.imagePath}


    def setImageInBlock(self, image_pixmap, image_path):
        self.label_background.setPixmap(image_pixmap.scaled(200, 150))
        self.label_minuature.setPixmap(image_pixmap.scaled(75, 70, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.image_pixmap = image_pixmap
        infoImage = self.getInfoImage(image_path)
        self.label_textInfoImage.setText(f"""name: {infoImage['name']+'.'+infoImage['expen']}\n
    size: {infoImage['size']:.2f}""")


    def destroy(self):
        self.parent.list_imageBlock.remove(self)
        self.parent.layout().removeWidget(self.button_container)
        if len(self.parent.list_imageBlock) == 0:
            self.parent.open_compress.setEnabled(False)
        self.button_container.deleteLater()
        self.deleteLater()


    def getInfoImage(self, imagePath):
        file_path = Path(imagePath)
        stat_info = file_path.stat()

        infoImage = {'name': imagePath.split('/')[-1].split('.')[0],
        'expen': imagePath.split('.')[-1],
        'size': stat_info.st_size / (1024 ** 2)}
        return infoImage

