import os
from PyPDF2 import PdfFileReader, PdfFileWriter 

# root directory
path = 'practice_files'
# original file path
full_path = os.path.join(path, 'The Emperor.pdf')
# original pdf
input_file = PdfFileReader(open(full_path, "rb"))
# watermark file path
watermark_path = os.path.join(path, 'top secret.pdf')
# watermark pdf
watermark_file = PdfFileReader(open(watermark_path, "rb"))
# output pdf
output_pdf = PdfFileWriter()

# loop over every page in original pdf and add watermark to its every page
for page_num in range(0, input_file.getNumPages()):
    page = input_file.getPage(page_num)
    page.mergePage(watermark_file.getPage(0))
    output_pdf.addPage(page)

# encrypt pdf
output_pdf.encrypt("Wxyz1@23")
output_file_name = os.path.join(path, "Encrypted.pdf")
output_file = open(output_file_name, "wb")
output_pdf.write(output_file)
output_file.close()
