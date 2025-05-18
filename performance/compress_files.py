from PyQt5.QtGui import QPixmap, QImage
from PIL import Image
import io
from tkinter import filedialog
import os

from openMessageBox import messageBox


def compress(files, setting):
    if not setting['autoReplace']:
        path_folder = filedialog.askdirectory(title="Сохранить в")
        if not path_folder:
            return 0
    for oneImage in files:
        qimage = oneImage['pixmap'].toImage()
        buffer = qimage.bits().asstring(qimage.byteCount())
        width = qimage.width()
        height = qimage.height()
        bytes_per_line = qimage.bytesPerLine()
        format = qimage.format()
        img = Image.frombytes("RGBA", (width, height), buffer, "raw", "BGRA").convert('RGB')
        with img as image:
            name = oneImage['path'].split('/')[-1].split('.')[0]
            form = oneImage['path'].split('.')[-1]
            if setting['autoReplace']:
                folder = oneImage['path'][::-1].split('/', maxsplit=1)[1][::-1]
                image.save(f"{folder}/{name}.{form}", quality=setting['quality'])
            else:
                image.save(f"{path_folder}/{name}.{form}", quality=setting['quality'])
    messageBox(image_path='icon/noneImage.png', text='Успешное сжатие', title='Успех')


def compressForArhive(files, quality):
    temp_files = []
    for file_info in files:
        if file_info['path'].lower().endswith(('.png', '.jpg', '.jpeg')):
            qimage = file_info['pixmap'].toImage()
            buffer = qimage.bits().asstring(qimage.byteCount())
            img = Image.frombytes(
                "RGBA", 
                (qimage.width(), qimage.height()), 
                buffer, 
                "raw", 
                "BGRA"
            ).convert('RGB')
            
            temp_path = f"/tmp/{file_info['path'].split('/')[-1]}"
            img.save(temp_path, quality=quality)
            temp_files.append(temp_path)
        else:
            temp_files.append(file_info['path'])

    return temp_files
