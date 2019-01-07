import os
from PyPDF2 import PdfFileReader, PdfFileWriter 
import copy

# root directory
path = 'practice_files'
# original file path
full_path = os.path.join(path, 'The Emperor.pdf')
# original pdf
input_file = PdfFileReader(open(full_path, "rb"))
# cover file path
cover_path = os.path.join(path, 'Emperor cover sheet.pdf')
cover_pdf = PdfFileReader(open(cover_path, "rb"))
# output pdf
output_pdf = PdfFileWriter()

# add original pdf
for page_num in range(0, input_file.getNumPages()):
    page = input_file.getPage(page_num)
    output_pdf.addPage(page)

# add cover pdf
for page_num in range(cover_pdf.getNumPages()):
    page = cover_pdf.getPage(page_num)
    output_pdf.addPage(page)

# create new pdf
output_file_name = os.path.join(path, "The Covered Emperor.pdf")
output_file = open(output_file_name, "wb")
output_pdf.write(output_file)
output_file.close()