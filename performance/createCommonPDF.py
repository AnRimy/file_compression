import PyPDF2
import os
from tkinter import filedialog

from openMessageBox import messageBox

def createOnePDF(file_list):
    path_folder = filedialog.asksaveasfile(title="Сохранить в", defaultextension=".pdf")
    if not path_folder:
        return 0
    pdf_writer = PyPDF2.PdfWriter()
    for pdf in file_list:
        with open(pdf['path'], 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])

    with open(path_folder.name, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
    messageBox(image_path='icon/noneImage.png', text='Успешное создание pdf', title='Успех')




