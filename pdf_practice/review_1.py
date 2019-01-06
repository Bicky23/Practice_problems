import os
from PyPDF2 import PdfFileReader, PdfFileWriter 

# root directory
path = 'practice_files'
# full file path
full_path = os.path.join(path, 'The Whistling Gypsy.pdf')

# open file
input_file = PdfFileReader(open(full_path, "rb"))
num_pages = input_file.getNumPages()
title =  input_file.getDocumentInfo().title
author = input_file.getDocumentInfo().author

# write to an empty text file
output_file_path = os.path.join(path, 'The Whistling Gypsy.txt')
output_file = open(output_file_path, "w")
output_file.write("Title of the book is {}".format(title) + "\n")
output_file.write("Author of the book is {}".format(author) + "\n")
output_file.write("Number of pages is: {}".format(num_pages) + "\n")


for page in range(num_pages):
    text = input_file.getPage(page).extractText()
    output_file.write(text)


# new pdf file without cover page
output_pdf = PdfFileWriter()

output_pdf.addPage(input_file.getPage(1))

output_file_name = os.path.join(path, "The Whistling Gypsy new.pdf")
output_file_pdf = open(output_file_name, "wb")
output_pdf.write(output_file_pdf)
output_file_pdf.close()


