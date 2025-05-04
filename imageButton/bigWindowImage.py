from PyQt5.QtWidgets import QFrame, QLabel, QPushButton, QHBoxLayout, QSizePolicy, QVBoxLayout, QWidget, QSlider
from PyQt5.QtGui import QPixmap, QIcon, QPainter, QTransform
from PyQt5.QtCore import QSize, Qt
from tkinter import filedialog

from style.styleWidgets import style_bigWindow, style_editImageInBlock, style_labelImage, style_frameInstrum

class BigWindow(QWidget):
    def __init__(self, parent, mainWindow, image_path, image_pixmap):
        super().__init__ (parent)
        self.parent = parent
        self.mainWindow = mainWindow
        self.image_path = image_path
        self.image_pixmap = image_pixmap

        self.widgets()


    def widgets(self):
        # frame blur
        self.frame_blur = QFrame(self.mainWindow)
        self.frame_blur.setGeometry(0, 0, 1000, 700)
        self.setMinimumSize(1000, 700)
        self.frame_blur.setStyleSheet('background-color: rgba(57, 62, 70, 128)')
        self.frame_blur.show()

        # main widgets
        self.main_widget = QFrame(self.frame_blur)
        self.main_widget.setFixedWidth(700)
        self.main_widget.setStyleSheet(style_bigWindow)
        self.main_widget.show()

        # image label
        self.label_imageLabel = QLabel(self.main_widget)
        self.label_imageLabel.setFixedSize(500, 500)
        self.original_pixmap = QPixmap(self.image_pixmap)
        scaled_pixmap = self.original_pixmap.scaled(self.label_imageLabel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label_imageLabel.setPixmap(scaled_pixmap)
        self.label_imageLabel.setAlignment(Qt.AlignCenter)
        self.label_imageLabel.setStyleSheet(style_labelImage)
        self.label_imageLabel.show()

        #frame instrument
        self.frame_instrum = QFrame(self.main_widget)
        self.frame_instrum.setFixedHeight(70)
        self.frame_instrum.setStyleSheet(style_frameInstrum)
        self.frame_instrum.show()

        # frame slider widgets
        self.frame_sliders = QFrame(self.main_widget)
        self.frame_sliders.setGeometry(45, 33, 50, 500)
        self.frame_sliders.setStyleSheet(style_frameInstrum)
        self.frame_sliders.show()

        sBtnCom = 50
        # button save image bigWindow
        self.button_saveImageFrame = QPushButton()
        self.button_saveImageFrame.setFixedSize(sBtnCom, sBtnCom)
        self.button_saveImageFrame.setIcon(QIcon('icon/save.png'))
        self.button_saveImageFrame.setIconSize(QSize(sBtnCom-10, sBtnCom-10))
        self.button_saveImageFrame.setStyleSheet(style_editImageInBlock)

        # replace image
        self.button_changeImage = QPushButton()
        self.button_changeImage.setFixedSize(sBtnCom, sBtnCom)
        self.button_changeImage.setIcon(QIcon('icon/changeImage.png'))
        self.button_changeImage.setIconSize(QSize(sBtnCom-10, sBtnCom-10))
        self.button_changeImage.setStyleSheet(style_editImageInBlock)

        # close big window
        self.button_closeBigWindow = QPushButton(self.main_widget)
        self.button_closeBigWindow.setFixedSize(sBtnCom, sBtnCom)
        self.button_closeBigWindow.setIcon(QIcon('icon/close.png'))
        self.button_closeBigWindow.setIconSize(QSize(sBtnCom-10, sBtnCom-10))
        self.button_closeBigWindow.setGeometry(645, 5, 50, 50)
        self.button_closeBigWindow.show()
        
        # rotate slade
        self.slider_rotateAngle = QSlider(parent=self.frame_sliders, orientation=Qt.Vertical)
        self.slider_rotateAngle.setRange(-180, 180)
        self.slider_rotateAngle.setValue(0)
        self.slider_rotateAngle.setFixedHeight(450)
        self.label_valueSlider = QLabel(parent=self.frame_sliders)
        self.label_valueSlider.setText(str(self.slider_rotateAngle.value()))

        # layout
        layout_HForMainWidget = QHBoxLayout(self.frame_blur)
        layout_VForInstrumWidgets = QVBoxLayout(self.main_widget)
        layout_VForInstrumWidgets.setSpacing(50)
        layout_HForInstrumFrame = QHBoxLayout(self.frame_instrum)
        layout_VSlidersWidgets = QVBoxLayout(self.frame_sliders)

        # add layout
        layout_HForMainWidget.addWidget(self.main_widget, alignment=Qt.AlignLeft)
        layout_VForInstrumWidgets.addWidget(self.label_imageLabel, alignment=Qt.AlignCenter)
        layout_VForInstrumWidgets.addWidget(self.frame_instrum)
        layout_HForInstrumFrame.addWidget(self.button_saveImageFrame, alignment=Qt.AlignCenter)
        layout_HForInstrumFrame.addWidget(self.button_changeImage, alignment=Qt.AlignCenter)
        layout_VSlidersWidgets.addWidget(self.slider_rotateAngle, alignment=Qt.AlignTop| Qt.AlignCenter)
        layout_VSlidersWidgets.addWidget(self.label_valueSlider, alignment=Qt.AlignTop | Qt.AlignCenter)

        # connect button
        self.button_saveImageFrame.clicked.connect(self.saveImage)
        self.button_closeBigWindow.clicked.connect(self.closBigWindow)
        self.button_changeImage.clicked.connect(self.changeImage)
        self.slider_rotateAngle.valueChanged.connect(self.rotateImage)

        self.final_pixmap = self.original_pixmap


    def rotateImage(self, angle):
        self.label_valueSlider.setText(str(self.slider_rotateAngle.value()))

        scaled_pixmap = self.original_pixmap.scaled(
            self.label_imageLabel.size(), 
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation
        )
        
        rotated_pixmap = QPixmap(scaled_pixmap.size())
        rotated_pixmap.fill(Qt.transparent)
        
        painter = QPainter(rotated_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(rotated_pixmap.width() / 2, rotated_pixmap.height() / 2)
        painter.rotate(angle)
        painter.translate(-scaled_pixmap.width() / 2, -scaled_pixmap.height() / 2)
        painter.drawPixmap(0, 0, scaled_pixmap)
        painter.end()
        
        transform = QTransform().rotate(angle)
        bounding_rect = transform.mapRect(scaled_pixmap.rect())
        
        final_pixmap = QPixmap(bounding_rect.size())
        final_pixmap.fill(Qt.transparent)
        
        painter = QPainter(final_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(final_pixmap.width() / 2, final_pixmap.height() / 2)
        painter.rotate(angle)
        painter.translate(-scaled_pixmap.width() / 2, -scaled_pixmap.height() / 2)
        painter.drawPixmap(0, 0, scaled_pixmap)
        painter.end()
        
        self.final_pixmap = final_pixmap.scaled(
            self.label_imageLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        
        self.label_imageLabel.setPixmap(self.final_pixmap)
        self.label_imageLabel.setAlignment(Qt.AlignCenter)
        

    def saveImage(self):
        sendImage = self.final_pixmap if self.slider_rotateAngle.value() != 0 else self.original_pixmap
        self.parent.setImageInBlock(sendImage)
        self.closBigWindow()


    def closBigWindow(self):
        self.frame_blur.deleteLater()
        self.deleteLater()

    
    def changeImage(self):
        newImage = filedialog.askopenfilename(title="Выберите новое изображение", filetypes=[("Image Files", "*.jpg *.jpeg")])
        if not newImage:
            return 0
        self.original_pixmap = QPixmap(newImage)
        scaled_pixmap = self.original_pixmap.scaled(self.label_imageLabel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label_imageLabel.setPixmap(scaled_pixmap)
        self.label_imageLabel.setAlignment(Qt.AlignCenter)
        self.label_imageLabel.setStyleSheet(style_labelImage)
        self.slider_rotateAngle.setValue(0)
