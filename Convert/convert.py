import re
import os

items = os.listdir(".")
filelist = []
for names in items:
  if names.endswith(".ppt"):
    filelist.append(names)
filelist.sort()

for names in filelist:
  powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
  powerpoint.Visible = 1
  outputFileName = names[0,len(names)-4] + ".pdf"
  print(outputFileName)
  deck = powerpoint.Presentations.Open(names)
  deck.SaveAs(outputFileName, formatType) # formatType = 32 for ppt to pdf
  deck.Close()
  powerpoint.Quit()