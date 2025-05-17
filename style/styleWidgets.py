# workBar.py
style_frame_workBar = """
background-color:rgba(34, 40, 49, 1); border-radius: 10px;
"""

style_buttonProccessing = """
QToolButton {
                background-color: rgba(0, 173, 181, 255);
                font-family: "Segoe UI", "SF Pro Display", -apple-system, sans-serif;
                font-size: 10px;
                font-weight: 500;
                color: #2a2a2a;
            }
QToolButton:hover {
                background-color: rgba(0, 150, 255, 200);
            }
QToolButton:pressed {
                background-color: gray;
            }
        """


# workZone.py
style_label_workZone = """
background-color:rgba(57, 62, 70, 1); 
border-radius: 10px;
"""


# openMessageBox.py
style_messageBox = """
QMessageBox {
    background-color: rgba(57, 62, 75, 1);
    font-size: 16px;
    color: white;
}

QMessageBox QLabel {
    color: white;
    alignment: alignCenter;
    margin: 10px;
}

QMessageBox QPushButton {
    background-color: rgba(0, 173, 181, 1);
    color: white;
    border: none;
    padding: 5px 15px;
    font-size: 14px;
    border-radius: 4px;
    min-width: 80px;
}

QMessageBox QPushButton:hover {
    background-color: rgba(0, 193, 201, 1);
}

QMessageBox QPushButton:pressed {
    background-color: rgba(0, 153, 161, 1);
}
"""

style_button_block = """
QPushButton {
                background-color:rgba(0, 128, 255, 255);
                text-align: center;
            }
QPushButton:hover {
                background-color: rgba(0, 150, 255, 200);
            }
"""

style_button_delete = """
QPushButton {
                background-color: red;
                border-radius: 10px;
            }
QPushButton:hover {
                background-color: #373B41;
            }
QPushButton:pressed {
                background-color: red;
            }
"""

style_label_textInfoImage = """
    color: yellow;
    font-size: 8px;
    font-weight: bold;
    text-align: left;
    padding-left: 2px;
    background-color: rgba(125, 125, 125, 0);
    border: 1px solid white;
"""

style_label_minuature = """
    background: transparent;
    border: none;
"""


# bigWindowImage.py
style_bigWindow = """
background-color:qlineargradient(x1: 1, y1: 1, 
                                x2: 0, y2: 0,
                                stop: 0 #00AEB8, 
                                stop: 0.35 #00BEF7,
                                stop: 1 #00FBFF);
                                border-radius: 10px;
"""

style_editImageInBlock ="""
QPushButton {
                background-color: rgba(0, 173, 181, 2);
                border: 1px solid white;
            }
QPushButton:hover {
                background-color: rgba(0, 150, 255, 200);
            }
QPushButton:pressed {
                background-color: gray;
            }
"""

style_labelImage = """
background-color:rgba(125, 125, 12, 20);
border: 1px solid white;
"""

style_frameInstrum = """
background-color:rgba(125, 125, 12, 20);
"""


# archive_files.py
style_frame_mainFrame = """
background-color:rgba(57, 62, 70, 1); 
border-radius: 10px;
"""

style_label_nameArch = """
    background-color: transparent;
    border: 1px solid white;
    border-radius: 5px;
    font-size: 14px;
    color: white;
"""

style_lineEdit_nameArch = """
    background-color: transparent;
    border: 1px solid white;
    border-radius: 5px;
    font-size: 14px;
    color: white;
"""

style_checkbox_compress_files = """
QCheckBox{
    background-color: transparent;
    color: white;
    font-size: 14px;
}
QCheckBox::indicator{
    border: 1px solid white;
    border-radius: 3px;
}
QCheckBox::indicator:unchecked:hover {
    border: 1px solid blue;
}
QCheckBox::indicator:checked {
    background-color: gray;
    border: 1px solid blue;
}
"""

style_checkbox_setPassword = """
QCheckBox{
    background-color: transparent;
    color: white;
    font-size: 14px;
}
QCheckBox::indicator{
    border: 1px solid white;
    border-radius: 3px;
}
QCheckBox::indicator:unchecked:hover {
    border: 1px solid blue;
}
QCheckBox::indicator:checked {
    background-color: gray;
    border: 1px solid blue;
}
"""

style_button_startArchive = """
QPushButton{
    background-color: transparent;
    border: 1px solid white;
    border-radius: 5px;
    font-size: 14px;
    color: white;
}
QPushButton::pressed{
    background-color: gray;
}
"""
