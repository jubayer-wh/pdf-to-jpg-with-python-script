import os
from pdf2image import convert_from_path

# specify the PDF file path
pdf_path = 'example.pdf'

# convert PDF to images
images = convert_from_path(pdf_path)

# create a directory to save the images
if not os.path.exists('images'):
    os.makedirs('images')

# save each image as a JPEG file
for i, image in enumerate(images):
    image.save(f'images/page_{i+1}.jpg', 'JPEG')
