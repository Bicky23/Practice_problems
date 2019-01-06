# import packages
import os
from PyPDF2 import PdfFileReader, PdfFileWriter 

# root directory
path = 'practice_files'
# full file path
full_path = os.path.join(path, 'Pride and Prejudice.pdf')

# open file
input_file = PdfFileReader(open(full_path, "rb"))

print("Number of pages:", input_file.getNumPages())
print('*'*100)
print("Title:", input_file.getDocumentInfo().title)
print('*'*100)
print("Information about the PDF file:", input_file.getDocumentInfo())
print('*'*100)
print(input_file.getPage(25).extractText())

# write to an empty text file
output_file_path = os.path.join(path, 'Pride and Prejudice.txt')
output_file = open(output_file_path, "w")

title = input_file.getDocumentInfo().title
total_pages = input_file.getNumPages()

output_file.write(title + "\n")
output_file.write("Number of pages is: {}".format(total_pages))

for page_num in range(total_pages):
    text = input_file.getPage(page_num).extractText()
    text = text.replace(" ", "\n")
    output_file.write(text)

output_file.close()


# write to an empty PDF file
output_pdf = PdfFileWriter()

for page_num in range(10,15):
    output_pdf.addPage(input_file.getPage(page_num))

output_file_name = os.path.join(path, "Portion.pdf")
output_file_pdf = open(output_file_name, "wb")
output_pdf.write(output_file_pdf)
output_file_pdf.close()