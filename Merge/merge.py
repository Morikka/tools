import os
from PyPDF2 import PdfFileMerger

items = os.listdir(".")
filelist = []
for names in items:
    if names.endswith(".pdf"):
        filelist.append(names)
filelist.sort()
print filelist

merger = PdfFileMerger()
for pdf in filelist:
    merger.append(open(pdf, 'rb'))

merger.write("result.pdf")    