from PIL import Image, ImageFont, ImageDraw
import os
import imageio

text = '你應該移民到：'
text_list = []
font = ImageFont.truetype('fonts/simsun.ttc', 40)
font_country = ImageFont.truetype('fonts/simsun.ttc', 80)

with open('list1.in', 'r') as f:
  for word in f:
    word = word.strip('\n')
    text_list.append(word)

print(text_list)

tmp = 0

for i in text_list:

  img = Image.new('RGBA', (500, 500))
  brush = ImageDraw.Draw(img)
  brush.text((20,10), text, fill='#000', font=font)
  l = len(i)
  #print(l)
  if l <= 6:
    tmp = 250-80*(len(i)/2)
    brush.text((tmp,190), i, fill='#000', font=font_country)
  elif l<=12:
    tmp = 250-80*(len(i)/2-3)
    brush.text((10,140), i[0:6], fill='#000', font=font_country)
    brush.text((tmp,230), i[6:], fill='#000', font=font_country)
  elif l<=18:
    tmp = 250-80*(len(i)/2-6)
    print(tmp)
    brush.text((10,100), i[0:6], fill='#000', font=font_country)
    brush.text((10,190), i[6:12], fill='#000', font=font_country)
    brush.text((tmp,280), i[12:], fill='#000', font=font_country)
  else:
    print('fuck')
  img.save('%s.png' % i)

images = []

tmp = 0
filenames=sorted((fn for fn in os.listdir('.') if fn.endswith('.png')))
for filename in filenames:
  im = Image.open(filename)
  bg = Image.new("RGB", im.size, (255,255,255))
  bg.paste(im,im)
  tmp = tmp+1
  bg.save(str(tmp)+'.jpg')

filenames=sorted((fn for fn in os.listdir('.') if fn.endswith('.jpg')))
print(filenames)

for filename in filenames:
  images.append(imageio.imread(filename))

imageio.mimsave('gif.gif',images)
