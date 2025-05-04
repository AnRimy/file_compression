from PyQt5.QtGui import QPixmap, QImage
from PIL import Image
import io
from tkinter import filedialog

from openMessageBox import messageBox

def compress(files, quality=70, autoReplace=False):
    if not autoReplace:
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
            if autoReplace:
                folder = oneImage['path'][::-1].split('/', maxsplit=1)[1][::-1]
                image.save(f"{folder}/{name}.{form}", quality=quality)
            else:
                image.save(f"{path_folder}/{name}.{form}", quality=quality)
    messageBox(image_path='icon/noneImage.png', text='Успешное сжатие', title='Успех')