import win32print
import win32ui
from PIL import Image, ImageWin

def print_image(file_path):
    printer_name = win32print.GetDefaultPrinter()

    hdc = win32ui.CreateDC("WINSPOOL", printer_name, None)
    hdc.StartDoc(file_path)
    hdc.StartPage()

    img = Image.open(file_path)
    img_width, img_height = img.size

    scale_x = float(hdc.GetDeviceCaps(8)) / img_width
    scale_y = float(hdc.GetDeviceCaps(10)) / img_height
    scale = min(scale_x, scale_y)
    img_width = int(scale * img_width)
    img_height = int(scale * img_height)

    dib = ImageWin.BITMAPHANDLE(img)
    hdc.DrawBitmap((0, 0, img_width, img_height), dib, (0, 0, img.size[0], img.size[1]))

    hdc.EndPage()
    hdc.EndDoc()
    hdc.DeleteDC()

print_image("path_to_your_image.jpg")