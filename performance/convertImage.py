from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import fitz
from tkinter import filedialog

# minuature
def convertForMinuature(pdf_path, page_number=0, zoom=2.0):
    doc = fitz.open(pdf_path)
    if page_number >= doc.page_count:
        pass

    page = doc.load_page(page_number)
    
    mat = fitz.Matrix(zoom, zoom)
    
    pix = page.get_pixmap(matrix=mat)
    
    image_format = QImage.Format_RGB888
    if pix.alpha:
        image_format = QImage.Format_RGBA8888
    
    qimage = QImage(
        pix.samples, 
        pix.width, 
        pix.height, 
        pix.stride, 
        image_format
    )
    return QPixmap.fromImage(qimage)

# PDF to JPG
def convertPDFtoJPG(files, page_number=0, zoom=2.0):
    path_folder = filedialog.askdirectory(title="Сохранить в")
    if not path_folder:
        return 0
    for i in files:
        name = i['path'].split('/')[-1].split('.')[0]
        doc = fitz.open(i['path'])
        page = doc.load_page(page_number)
    
        mat = fitz.Matrix(zoom, zoom)
        
        pix = page.get_pixmap(matrix=mat)
        
        image_format = QImage.Format_RGB888
        if pix.alpha:
            image_format = QImage.Format_RGBA8888
        
        qimage = QImage(
            pix.samples, 
            pix.width, 
            pix.height, 
            pix.stride, 
            image_format
        )
        qimage.save(f"{path_folder}/{name}.jpg")
        page_number+=1

