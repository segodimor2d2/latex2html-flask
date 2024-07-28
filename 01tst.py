from pdf2image import convert_from_path
import os

PDF_PATH = 'doctxt.pdf'
IMG_FOLDER = 'templates/images/'

def convert_pdf_to_images():
    images = convert_from_path(PDF_PATH)

    for i, image in enumerate(images):
        image_path = os.path.join(IMG_FOLDER, f'page_{i}.png')
        image.save(image_path, 'PNG')

convert_pdf_to_images()
