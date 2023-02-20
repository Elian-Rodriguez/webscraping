from PIL import Image
from pdf2image import convert_from_path

# Nombre del archivo PDF que se desea convertir
pdf_path = 'ruta/del/archivo.pdf'

# Crea una lista de imágenes a partir del archivo PDF
pages = convert_from_path(pdf_path)

# Recorre la lista de imágenes y guarda cada una en formato JPEG
for i, page in enumerate(pages):
    jpeg_path = f'ruta/del/archivo_{i+1}.jpeg' # Nombre del archivo JPEG
    page.save(jpeg_path, 'JPEG')