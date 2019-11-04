##################################################################
#Challenge 12: http://www.pythonchallenge.com/pc/return/evil.html#
##################################################################

# Hint: dealing evil

# The image is called evil1.jpg so let's try evil2.jpg
# this brings us a hint to use .gfx instead of .jpg
# using .gfx gives a file to work with

import os
from PIL import Image

cwd = os.path.dirname(__file__)

data = open(cwd+'/resources/evil2.gfx', 'rb').read()
print(type(data))

# for i in range(len(data)):
#     print(data[i])

# This gives us a large bytestring. There's 5 stacks of cards in 
# the original hint, so we'll "deal" into 5 stacks using bytes
# instead of cards

data1 = open(cwd+'/resources/evil21.jpg','wb')
data2 = open(cwd+'/resources/evil22.jpg','wb')
data3 = open(cwd+'/resources/evil23.jpg','wb')
data4 = open(cwd+'/resources/evil24.jpg','wb')
data5 = open(cwd+'/resources/evil25.jpg','wb')

for i in range(len(data)):
    if i % 5 == 0:
        data1.write(b'%c' % data[i])
    elif i % 5 == 1:
        data2.write(b'%c' % data[i])
    elif i % 5 == 2:
        data3.write(b'%c' % data[i])
    elif i % 5 == 3:
        data4.write(b'%c' % data[i])
    else:
        data5.write(b'%c' % data[i])

data1.close()
data2.close()
data3.close()
data4.close()
data5.close()

# Let's look at what we made

im1 = Image.open(cwd+'/resources/evil21.jpg')
im1.show()
im2 = Image.open(cwd+'/resources/evil22.jpg')
im2.show()
im3 = Image.open(cwd+'/resources/evil23.jpg')
im3.show()
im4 = Image.open(cwd+'/resources/evil24.jpg')
im4.show()
im5 = Image.open(cwd+'/resources/evil25.jpg')
im5.show()

# So this breaks with an 'image is truncated' error on evil24.jpg
# but we can just open these manually to get our keyword: disproportional




