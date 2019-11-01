##################################################################
#Challenge 11: http://www.pythonchallenge.com/pc/return/5808.html#
##################################################################

# "odd even" hints leads me to believe this image is interlaced somehow

import os

from PIL import Image, ImageEnhance

cwd = os.path.dirname(__file__)
im = Image.open(cwd+'/resources/cave.jpg')

im1 = Image.new(mode='RGB',size=(int(im.width/2),int(im.height/2)))

for i in range(im.width):
    for j in range(im.height):
        if i % 2 == 0 and j % 2 == 0:
            im1.putpixel((int(i/2),int(j/2)),im.getpixel((i,j)))

im1.show()

