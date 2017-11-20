import os
import re
from PyPDF2 import PdfFileMerger

items = os.listdir(".")
filelist = []
for names in items:
  if names.endswith(".pdf"):
    filelist.append(names)
filelist.sort()
print filelist

# file = open("merge.conf")

# while 1:
#   line = file.readline()
#   if not line:
#     break
#   pattern = '^1'
#   # print pattern
#   for names in filelist:
#     print re.match(pattern,names)
#       # print names


merger = PdfFileMerger()
for pdf in filelist:
    merger.append(open(pdf, 'rb'))

merger.write("result.pdf")