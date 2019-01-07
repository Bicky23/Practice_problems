import os
from PyPDF2 import PdfFileReader, PdfFileWriter 
import copy

# root directory
path = 'practice_files'
# full file path
full_path = os.path.join(path, 'half and half.pdf')

# open file
input_file = PdfFileReader(open(full_path, "rb"))
output_pdf = PdfFileWriter()

for page_num in range(0, input_file.getNumPages()):
    page_left = input_file.getPage(page_num)
    page_right = copy.copy(page_left)
    upper_right = page_left.mediaBox.upperRight # get original page corner
    # crop and add left-side page
    page_left.mediaBox.upperRight = (upper_right[0]/2, upper_right[1])
    output_pdf.addPage(page_left)
    # crop and add right-side page
    page_right.mediaBox.upperLeft = (upper_right[0]/2, upper_right[1])
    output_pdf.addPage(page_right)
output_file_name = os.path.join(path, "The Little Mermaid.pdf")
output_file = open(output_file_name, "wb")
output_pdf.write(output_file)
output_file.close()