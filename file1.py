from PyPDF2 import PdfFileReader

f = open('CT1-All.pdf', 'rb')
reader = PdfFileReader(f)
contents = reader.getPage(0).extractText().split('\n')
f.close()