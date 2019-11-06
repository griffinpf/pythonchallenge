###################################################################
#Challenge 14: http://www.pythonchallenge.com/pc/return/italy.html#
###################################################################

# Hint is "walk around" and there's a .png file provided

import os
from PIL import Image

cwd = os.path.dirname(__file__)
im = Image.open(cwd+'/resources/wire.png')

# The png is 1 pixel in height and 10000 pixels wide. The hint is 
# "walk around" with a picture of a spiral pastry. So let's arrange
# our pixels in the same pattern (spiral matrix). 10000 pixels makes
# a 100x100 square (sqrt(10000) = 100)

im1 = Image.new('RGB',(100,100))

dxdy = [(1,0),(0,1),(-1,0),(0,-1)]
x,y = -1,0
i = 0
for j in range(200):
    direction = dxdy[j % 4]
    for k in range(100 - (j + 1) // 2):
        x += direction[0]
        y += direction[1]
        im1.putpixel((x,y),im.getpixel((i,0)))
        i += 1

im1.show()
