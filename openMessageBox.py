from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize

from style.styleWidgets import style_messageBox

def messageBox(image_path, title, text, scaled = (250, 250)):
    msg = QMessageBox()
    icon_pixmap = QPixmap(image_path)
    msg.setIconPixmap(icon_pixmap.scaled(QSize(*scaled)))
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setStyleSheet(style_messageBox)
    msg.exec_()