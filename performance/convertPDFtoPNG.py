from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import fitz

def convertPDFtoPNG(pdf_path, page_number=0, zoom=2.0):
    doc = fitz.open(pdf_path)
    if page_number >= doc.page_count:
        raise ValueError("Номер страницы превышает количество страниц в PDF.")

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
