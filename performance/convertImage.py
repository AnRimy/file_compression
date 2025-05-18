from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import fitz
from tkinter import filedialog
import os

def convertForMinuature(pdf_path, page_number=0, zoom=2.0):
    doc = fitz.open(pdf_path)
    if page_number >= doc.page_count:
        page_number = doc.page_count - 1
    
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


def convertPDFtoJPG(files, setting, zoom=2.0):
    path_folder = filedialog.askdirectory(title="Сохранить в")
    if not path_folder:
        return 0
    
    total_converted = 0
    
    for file_info in files:
        pdf_path = file_info['path']
        doc = fitz.open(pdf_path)
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        
        if setting['mode'] == 'single':
            page_num = min(setting['page'], doc.page_count - 1)
            save_path = f"{path_folder}/{base_name}_page{page_num + 1}.jpg"
            if convert_page(doc, page_num, zoom, save_path):
                total_converted += 1
                
        elif setting['mode'] == 'range':
            start_page = min(setting['start'], doc.page_count - 1)
            end_page = min(setting['end'], doc.page_count - 1)
            
            if start_page > end_page:
                start_page, end_page = end_page, start_page
            
            for page_num in range(start_page, end_page + 1):
                save_path = f"{path_folder}/{base_name}_page{page_num + 1}.jpg"
                if convert_page(doc, page_num, zoom, save_path):
                    total_converted += 1
            
    return total_converted


def convert_page(doc, page_num, zoom, save_path):
    page = doc.load_page(page_num)
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
    return qimage.save(save_path)
